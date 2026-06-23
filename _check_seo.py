import os, re
os.chdir('D:/openclaw/workspace/smrtdesk')

# Check sitemap structure
with open('sitemap.xml','r',encoding='utf-8') as f:
    c = f.read()

# Check if sitemap has priority or changefreq
has_priority = '<priority>' in c
has_changefreq = '<changefreq>' in c
has_lastmod = '<lastmod>' in c
url_count = len(re.findall(r'<url>', c))
print(f'Sitemap stats:')
print(f'  URLs: {url_count}')
print(f'  has priority: {has_priority}')
print(f'  has changefreq: {has_changefreq}')
print(f'  has lastmod: {has_lastmod}')

# Check index page for OG tags
with open('index.html','r',encoding='utf-8') as f:
    idx = f.read()
og_tags = re.findall(r'<meta[^>]*property="og:[^"]*"[^>]*>', idx)
print(f'\nIndex page OG tags: {len(og_tags)}')
for t in og_tags:
    print(f'  {t[:120]}')

# Check a product page for favicon/canonical
with open('product-ergear-height-adjustable-electric-standing-desk-48x24.html','r',encoding='utf-8') as f:
    pc = f.read()
canonical = re.findall(r'<link[^>]*rel="canonical"[^>]*>', pc)
print(f'\nProduct page canonical: {canonical}')
