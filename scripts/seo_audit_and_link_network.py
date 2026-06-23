#!/usr/bin/env python3
"""
SmrtDesk SEO Optimization Suite v3 - Preserves file encoding & line endings
"""
import os, re, glob, sys
from datetime import datetime, timezone
from collections import defaultdict

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_URL = "https://smrtdesk.xyz"

def read_raw(path):
    with open(path, 'rb') as f:
        return f.read()

def write_raw(path, data):
    with open(path, 'wb') as f:
        f.write(data)

def extract_title(content):
    m = re.search(rb'<title>(.*?)</title>', content, re.DOTALL)
    return m.group(1).decode('utf-8').strip() if m else ""

def extract_first_image(content):
    m = re.search(rb'<img[^>]+src=["\']([^"\']+)["\']', content)
    return m.group(1).decode('utf-8') if m else ""

def extract_og_image(content):
    m = re.search(rb'<meta\s+property=["\']og:image["\']\s+content=["\']([^"\']+)["\']', content)
    return m.group(1).decode('utf-8') if m else ""

def get_page_type(filename):
    if filename.startswith('article-'): return 'article'
    elif filename.startswith('product-'): return 'product'
    elif filename.startswith('category-'): return 'category'
    elif filename.startswith('page-'): return 'page'
    elif filename == 'index.html': return 'index'
    return 'other'

def extract_article_date(content):
    m = re.search(rb'"datePublished":\s*"(\d{4}-\d{2}-\d{2})"', content)
    return m.group(1).decode('utf-8') if m else ""


# ============================================================
# ACTION 1: Internal Link Analysis
# ============================================================
def analyze_internal_links():
    print("=" * 70)
    print("ACTION 1: INTERNAL LINK NETWORK ANALYSIS")
    print("=" * 70)
    
    results = []
    for fname in sorted(os.listdir(SITE_DIR)):
        if not fname.endswith('.html'): continue
        content = read_raw(os.path.join(SITE_DIR, fname))
        links = re.findall(rb'href=["\']([^"\']+)["\']', content)
        internal = [l for l in links if not l.startswith((b'#', b'http', b'mailto:', b'javascript:'))]
        ptype = get_page_type(fname)
        results.append({'file': fname, 'type': ptype, 'count': len(internal)})
    
    content_results = [r for r in results if r['type'] not in ('page', 'other')]
    for label, ptype in [("Articles", "article"), ("Products", "product"), ("Categories", "category")]:
        group = [r for r in results if r['type'] == ptype]
        if group:
            avg = sum(r['count'] for r in group) / len(group)
            print(f"  {label}: {len(group)} pages, avg {avg:.1f} internal links")
    
    print(f"  Total content pages: {len(content_results)}")
    return results


# ============================================================
# ACTION 2: Related Products in Articles
# ============================================================
def build_category_product_map():
    cat_to_products = defaultdict(list)
    product_info = {}
    
    for fname in sorted(os.listdir(SITE_DIR)):
        if not fname.endswith('.html'): continue
        ptype = get_page_type(fname)
        content = read_raw(os.path.join(SITE_DIR, fname))
        
        if ptype == 'category':
            product_links = re.findall(rb'href="(product-[^"]+\.html)"', content)
            for pl in set(product_links):
                cat_to_products[fname].append(pl.decode('utf-8'))
        
        if ptype == 'product':
            title = extract_title(content).replace(' | SmrtDesk', '').strip()
            img = extract_first_image(content) or extract_og_image(content) or ''
            product_info[fname] = {'title': title, 'image': img}
    
    return cat_to_products, product_info

def generate_related_block(article_fname, cat_to_products, product_info):
    content = read_raw(os.path.join(SITE_DIR, article_fname))
    # Extract article title raw bytes for keyword matching
    title_match = re.search(rb'<title>(.*?)</title>', content, re.DOTALL)
    article_title = title_match.group(1).decode('utf-8').lower() if title_match else ""
    
    keyword_map = {
        'office': ['office-furniture', 'standing-desk', 'office-chair', 'executive-desk', 'monitor-stand', 'desk-accessories', 'computer-accessories'],
        'desk': ['standing-desk', 'office-furniture', 'executive-desk', 'monitor-stand', 'desk-accessories', 'computer-accessories'],
        'chair': ['office-chair', 'office-furniture'],
        'camping': ['camping-outdoors'],
        'outdoor': ['camping-outdoors', 'home-garden'],
        'garden': ['home-garden', 'camping-outdoors'],
        'grill': ['bbq-grilling-tools', 'camping-outdoors'],
        'kitchen': ['kitchen', 'kitchen-storage-organization', 'cookware-bakeware', 'kitchen-utensils-gadgets', 'small-appliances'],
        'bluetooth': ['audio-headphones', 'portable-devices'],
        'audio': ['audio-headphones'],
        'earbud': ['audio-headphones', 'wearable-tech'],
        'headphone': ['audio-headphones'],
        'noise': ['audio-headphones'],
        'speaker': ['audio-headphones', 'smart-home'],
        'smartwatch': ['wearable-tech', 'smart-home-gadgets'],
        'fitness': ['wearable-tech'],
        'charging': ['phone-accessories', 'computer-accessories'],
        'phone': ['cell-phones', 'phone-accessories'],
        'patio': ['home-garden', 'camping-outdoors'],
        'furniture': ['office-furniture', 'home-garden'],
        'planter': ['home-garden'],
        'plant': ['home-garden'],
        'beach': ['camping-outdoors'],
        'cano': ['camping-outdoors'],
        'sup': ['camping-outdoors'],
        'paddle': ['camping-outdoors'],
        'dutch': ['cookware-bakeware', 'kitchen'],
        'oven': ['cookware-bakeware', 'kitchen'],
        'recipe': ['cookware-bakeware', 'kitchen'],
        'light': ['home-garden', 'smart-home'],
        'string': ['home-garden'],
        'water': ['home-garden'],
        'self': ['home-garden'],
        'monitor': ['monitor-stand', 'computer-accessories'],
        'computer': ['computers-tablets', 'computer-accessories'],
        'accessor': ['computer-accessories', 'desk-accessories'],
        'home': ['home-garden', 'office-furniture', 'smart-home'],
        'gadget': ['smart-home-gadgets', 'electronics'],
        'tech': ['electronics', 'computer-accessories'],
    }
    
    matched_cat_files = []
    for kw, cats in keyword_map.items():
        if kw in article_title:
            for c in cats:
                cat_file = f"category-{c}.html"
                if cat_file not in matched_cat_files:
                    matched_cat_files.append(cat_file)
    
    for fc in ['category-trending.html', 'category-deals.html', 'category-gifts.html']:
        if fc not in matched_cat_files:
            matched_cat_files.append(fc)
    
    candidates, seen = [], set()
    for cat_file in matched_cat_files:
        if cat_file in cat_to_products:
            for prod in cat_to_products[cat_file]:
                if prod not in seen and prod in product_info:
                    seen.add(prod)
                    candidates.append(prod)
        if len(candidates) >= 4:
            break
    
    if len(candidates) < 3:
        return "", []
    
    selected = candidates[:4]
    items_html, linked_prods = [], []
    for prod_file in selected:
        info = product_info[prod_file]
        title = info['title'][:70]
        img = info['image'] or ''
        items_html.append(f'          <div class="related-item"><a href="{prod_file}"><img src="{img}" alt="{title}" loading="lazy" width="200" height="150"><span class="related-item-title">{title}</span></a></div>')
        linked_prods.append(prod_file)
    
    block = f'\n    <section class="related-products-section">\n      <h2 class="related-title">Handpicked for You</h2>\n      <div class="related-grid">\n' + '\n'.join(items_html) + '\n      </div>\n    </section>'
    return block, linked_prods

def inject_related_products():
    print("\n" + "=" * 70)
    print("ACTION 2: INJECTING RELATED PRODUCTS INTO ARTICLES")
    print("=" * 70)
    
    cat_to_products, product_info = build_category_product_map()
    total = sum(len(v) for v in cat_to_products.values())
    print(f"Category-product map: {len(cat_to_products)} categories, {total} product links, {len(product_info)} products")
    
    modified, total_new_links = [], 0
    for fname in sorted(os.listdir(SITE_DIR)):
        if not fname.startswith('article-'): continue
        
        fpath = os.path.join(SITE_DIR, fname)
        content = read_raw(fpath)
        
        if b'related-products-section' in content:
            print(f"  SKIP {fname} (already has)")
            continue
        
        block, linked_prods = generate_related_block(fname, cat_to_products, product_info)
        if not block:
            print(f"  SKIP {fname} (not enough matches)")
            continue
        
        block_bytes = block.encode('utf-8')
        
        if b'<footer class="site-footer">' in content:
            new_content = content.replace(b'<footer class="site-footer">', block_bytes + b'\n\n<footer class="site-footer">')
            write_raw(fpath, new_content)
            modified.append(fname)
            total_new_links += len(linked_prods)
            print(f"  INJECTED: {fname} (+{len(linked_prods)} links)")
        elif b'</main>' in content:
            new_content = content.replace(b'</main>', block_bytes + b'\n</main>')
            write_raw(fpath, new_content)
            modified.append(fname)
            total_new_links += len(linked_prods)
            print(f"  INJECTED: {fname} (+{len(linked_prods)} links)")
    
    print(f"\nModified {len(modified)} articles, {total_new_links} new internal links.")
    return modified


# ============================================================
# ACTION 3: Add Related Products CSS
# ============================================================
def add_related_products_css():
    print("\n" + "=" * 70)
    print("ACTION 3: ADDING RELATED PRODUCTS CSS")
    print("=" * 70)
    
    css_path = os.path.join(SITE_DIR, 'main.css')
    content = read_raw(css_path)
    
    if b'related-products-section' in content:
        print("CSS already exists. Skipping.")
        return
    
    css_block = b"""
/* Related Products Section */
.related-products-section {
  max-width: 1200px;
  margin: 40px auto;
  padding: 0 20px;
}
.related-title {
  font-size: 1.4rem;
  font-weight: 700;
  color: #1a1a2e;
  margin-bottom: 20px;
  text-align: center;
}
.related-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 16px;
}
.related-item {
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  transition: transform 0.2s, box-shadow 0.2s;
}
.related-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.12);
}
.related-item a {
  text-decoration: none;
  color: inherit;
  display: flex;
  flex-direction: column;
}
.related-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  background: #f5f5f5;
}
.related-item-title {
  padding: 12px 14px;
  font-size: 0.85rem;
  font-weight: 600;
  color: #333;
  line-height: 1.3;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
"""
    new_content = content + css_block
    write_raw(css_path, new_content)
    print(f"CSS appended to main.css")


# ============================================================
# ACTION 4: Generate RSS Feed
# ============================================================
def generate_rss_feed():
    print("\n" + "=" * 70)
    print("ACTION 4: GENERATING RSS FEED")
    print("=" * 70)
    
    now = datetime.now(timezone.utc)
    rss_date = now.strftime("%a, %d %b %Y %H:%M:%S GMT")
    
    items = []
    for fname in sorted(os.listdir(SITE_DIR)):
        if not fname.endswith('.html'): continue
        ptype = get_page_type(fname)
        if ptype != 'article': continue
        
        content = read_raw(os.path.join(SITE_DIR, fname))
        title = extract_title(content) or fname.replace('.html', '').replace('-', ' ').title()
        
        # Get desc
        desc_m = re.search(rb'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
        desc = desc_m.group(1).decode('utf-8').strip() if desc_m else ""
        if not desc:
            fp_m = re.search(rb'<p[^>]*>(.*?)</p>', content, re.DOTALL)
            if fp_m:
                desc = re.sub(rb'<[^>]+>', b'', fp_m.group(1)).decode('utf-8').strip()[:300]
        
        url = f"{SITE_URL}/{fname}"
        pub_date = extract_article_date(content)
        item_date = rss_date
        if pub_date:
            try:
                dt = datetime.strptime(pub_date, "%Y-%m-%d")
                item_date = dt.strftime("%a, %d %b %Y 00:00:00 GMT")
            except:
                pass
        
        items.append(f"""    <item>
      <title>{escape_xml(title)}</title>
      <link>{url}</link>
      <guid isPermaLink="true">{url}</guid>
      <description>{escape_xml(desc)}</description>
      <pubDate>{item_date}</pubDate>
    </item>""")
    
    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>SmrtDesk - Honest Home &amp; Office Product Reviews</title>
  <link>{SITE_URL}</link>
  <atom:link href="{SITE_URL}/rss.xml" rel="self" type="application/rss+xml"/>
  <description>Expert reviews of office furniture, standing desks, storage solutions, bunk beds, and home products. Honest ratings, buying guides, and real user feedback.</description>
  <language>en-us</language>
  <lastBuildDate>{rss_date}</lastBuildDate>
  <image>
    <url>{SITE_URL}/favicon.ico</url>
    <title>SmrtDesk - Honest Home &amp; Office Product Reviews</title>
    <link>{SITE_URL}</link>
  </image>
{chr(10).join(items)}
</channel>
</rss>"""
    
    rss_path = os.path.join(SITE_DIR, 'rss.xml')
    write_raw(rss_path, rss.encode('utf-8'))
    print(f"RSS feed generated with {len(items)} articles")
    return rss_path

def escape_xml(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&apos;')


# ============================================================
# ACTION 5: Add RSS Discovery Link
# ============================================================
def add_rss_link_to_pages():
    print("\n" + "=" * 70)
    print("ACTION 5: ADDING RSS AUTO-DISCOVERY")
    print("=" * 70)
    
    rss_link = b'  <link rel="alternate" type="application/rss+xml" title="SmrtDesk RSS Feed" href="/rss.xml" />\n'
    modified = 0
    
    for fname in sorted(os.listdir(SITE_DIR)):
        if not fname.endswith('.html'): continue
        fpath = os.path.join(SITE_DIR, fname)
        content = read_raw(fpath)
        
        if b'application/rss+xml' in content:
            continue
        
        # Find position after canonical link
        canonical_match = re.search(rb'([^\n]*rel="canonical"[^\n]*\n)', content)
        if canonical_match:
            pos = canonical_match.end()
            new_content = content[:pos] + rss_link + content[pos:]
            write_raw(fpath, new_content)
            modified += 1
    
    print(f"Added RSS discovery to {modified} pages")
    return modified


# ============================================================
# ACTION 6: SEO Audit
# ============================================================
def run_seo_audit():
    print("\n" + "=" * 70)
    print("ACTION 6: SEO AUDIT REPORT")
    print("=" * 70)
    
    issues = []
    stats = {
        'total': 0, 'title_ok': 0, 'title_too_short': 0, 'title_too_long': 0, 'title_missing': 0,
        'desc_ok': 0, 'desc_too_short': 0, 'desc_too_long': 0, 'desc_missing': 0,
        'h1_ok': 0, 'h1_missing': 0, 'h1_multiple': 0,
        'canonical_ok': 0, 'canonical_missing': 0,
        'schema_ok': 0, 'schema_missing': 0,
        'og_title_ok': 0, 'og_title_missing': 0,
        'og_desc_ok': 0, 'og_desc_missing': 0,
        'og_image_ok': 0, 'og_image_missing': 0,
    }
    
    for fname in sorted(os.listdir(SITE_DIR)):
        if not fname.endswith('.html'): continue
        ptype = get_page_type(fname)
        if ptype in ('other', 'page'): continue
        
        content = read_raw(os.path.join(SITE_DIR, fname))
        stats['total'] += 1
        
        # Title
        title_m = re.search(rb'<title>(.*?)</title>', content, re.DOTALL)
        title = title_m.group(1).decode('utf-8').strip() if title_m else ""
        if not title:
            stats['title_missing'] += 1
            issues.append(f"[TITLE] {fname}: Missing")
        elif 30 <= len(title) <= 65:
            stats['title_ok'] += 1
        elif len(title) < 30:
            stats['title_too_short'] += 1
        else:
            stats['title_too_long'] += 1
        
        # Description
        desc_m = re.search(rb'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
        desc = desc_m.group(1).decode('utf-8').strip() if desc_m else ""
        if not desc:
            stats['desc_missing'] += 1
        elif 120 <= len(desc) <= 160:
            stats['desc_ok'] += 1
        elif len(desc) < 120:
            stats['desc_too_short'] += 1
        else:
            stats['desc_too_long'] += 1
        
        # H1
        h1_count = len(re.findall(rb'<h1[>\s]', content))
        if h1_count == 0:
            stats['h1_missing'] += 1
        elif h1_count == 1:
            stats['h1_ok'] += 1
        else:
            stats['h1_multiple'] += 1
        
        # Other
        if b'rel="canonical"' in content: stats['canonical_ok'] += 1
        else: stats['canonical_missing'] += 1
        
        if b'application/ld+json' in content: stats['schema_ok'] += 1
        else: stats['schema_missing'] += 1
        
        if b'og:title' in content: stats['og_title_ok'] += 1
        else: stats['og_title_missing'] += 1
        if b'og:description' in content: stats['og_desc_ok'] += 1
        else: stats['og_desc_missing'] += 1
        if b'og:image' in content: stats['og_image_ok'] += 1
        else: stats['og_image_missing'] += 1
    
    print(f"\nChecked {stats['total']} content pages")
    print(f"  Title:        OK:{stats['title_ok']} short:{stats['title_too_short']} long:{stats['title_too_long']} miss:{stats['title_missing']}")
    print(f"  Meta Desc:    OK:{stats['desc_ok']} short:{stats['desc_too_short']} long:{stats['desc_too_long']} miss:{stats['desc_missing']}")
    print(f"  H1:           OK:{stats['h1_ok']} multi:{stats['h1_multiple']} miss:{stats['h1_missing']}")
    print(f"  Canonical:    OK:{stats['canonical_ok']} miss:{stats['canonical_missing']}")
    print(f"  Schema:       OK:{stats['schema_ok']} miss:{stats['schema_missing']}")
    print(f"  OG Title:     OK:{stats['og_title_ok']} miss:{stats['og_title_missing']}")
    print(f"  OG Desc:      OK:{stats['og_desc_ok']} miss:{stats['og_desc_missing']}")
    print(f"  OG Image:     OK:{stats['og_image_ok']} miss:{stats['og_image_missing']}")
    
    print(f"\n{len(issues)} issues identified (see seo-audit-report.txt)")
    
    with open(os.path.join(SITE_DIR, 'seo-audit-report.txt'), 'w', encoding='utf-8') as f:
        f.write(f"SmrtDesk SEO Audit - {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")
        f.write(f"Content pages: {stats['total']}\n\n")
        f.write("=== SUMMARY ===\n")
        f.write(f"Title:       OK={stats['title_ok']} short={stats['title_too_short']} long={stats['title_too_long']} miss={stats['title_missing']}\n")
        f.write(f"Meta Desc:   OK={stats['desc_ok']} short={stats['desc_too_short']} long={stats['desc_too_long']} miss={stats['desc_missing']}\n")
        f.write(f"H1:          OK={stats['h1_ok']} multi={stats['h1_multiple']} miss={stats['h1_missing']}\n")
        f.write(f"Canonical:   OK={stats['canonical_ok']} miss={stats['canonical_missing']}\n")
        f.write(f"Schema:      OK={stats['schema_ok']} miss={stats['schema_missing']}\n")
        f.write(f"OG Title:    OK={stats['og_title_ok']} miss={stats['og_title_missing']}\n")
        f.write(f"OG Desc:     OK={stats['og_desc_ok']} miss={stats['og_desc_missing']}\n")
        f.write(f"OG Image:    OK={stats['og_image_ok']} miss={stats['og_image_missing']}\n")
        f.write(f"\n=== ISSUES ===\n")
        for issue in issues:
            f.write(f"  {issue}\n")
    
    return issues, stats


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print(f"SmrtDesk SEO Suite v3 (preserving file encoding)")
    print()
    
    analyze_internal_links()
    add_related_products_css()
    inject_related_products()
    rss_path = generate_rss_feed()
    add_rss_link_to_pages()
    issues, stats = run_seo_audit()
    
    print("\n" + "=" * 70)
    print("ALL DONE")
    print(f"  New:      rss.xml, seo-audit-report.txt, scripts/")
    print(f"  Modified: main.css (+CSS)")
    print(f"  Articles: 13 (+related products)")
    print(f"  All pages: +RSS discovery link")
    print("=" * 70)
