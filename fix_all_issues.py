#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix all critical issues in SmrtDesk website.
Runs in-place on all HTML + JS files in smrtdesk/.
"""
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

SMRTDESK_DIR = os.path.dirname(os.path.abspath(__file__))

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# ========================================================================
# FIX 1: Unify CSS version numbers → v=22
# ========================================================================
print("=== FIX 1: Unify CSS version numbers ===")
for fname in os.listdir(SMRTDESK_DIR):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(SMRTDESK_DIR, fname)
    content = read(fpath)
    old_content = content
    
    # Replace main.css?v=ANY_DIGITS → main.css?v=22
    content = re.sub(r'main\.css\?v=\d+', 'main.css?v=22', content)
    
    # Ensure every HTML file has a <link rel="stylesheet" href="main.css?v=22"> before </head>
    if 'main.css' not in content:
        content = content.replace('</head>', '<link rel="stylesheet" href="main.css?v=22">\n</head>')
    
    if content != old_content:
        write(fpath, content)
        print(f"  [OK] {fname}")

# ========================================================================
# FIX 2: Fix slug=kitchen → slug=kitchen-storage-organizer (navigation)
# ========================================================================
print("\n=== FIX 2: Fix invalid slug=kitchen in navigation ===")
for fname in os.listdir(SMRTDESK_DIR):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(SMRTDESK_DIR, fname)
    content = read(fpath)
    old_content = content
    
    # Fix any remaining slug=kitchen that's NOT already slug=kitchen-storage-organizer or slug=kitchen-utensils-gadgets
    # Match: category.html?slug=kitchen"  (exactly kitchen, not kitchen-*)
    content = re.sub(r'(category\.html\?slug=)kitchen(")', r'\1kitchen-storage-organizer\2', content)
    
    if content != old_content:
        write(fpath, content)
        print(f"  [OK] {fname}")

# ========================================================================
# FIX 3: Remove any old category-xxx.html links still present
# ========================================================================
print("\n=== FIX 3: Replace old category-xxx.html links ===")
for fname in os.listdir(SMRTDESK_DIR):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(SMRTDESK_DIR, fname)
    content = read(fpath)
    old_content = content
    
    # Find href="category-XXX.html" (old format, NOT category.html)
    old_links = re.findall(r'href="(category-\w[\w-]*\.html)"', content)
    if old_links:
        print(f"  Found old links in {fname}: {old_links}")
    
    # Replace: href="category-xxx.html" → href="category.html?slug=xxx"
    content = re.sub(
        r'href="category-(\w[\w-]*)\.html"',
        r'href="category.html?slug=\1"',
        content
    )
    
    if content != old_content:
        write(fpath, content)
        print(f"  [OK] {fname}")

# ========================================================================
# FIX 4: Fix product.html inline renderer — remove category- link format
# ========================================================================
print("\n=== FIX 4: Fix product.html inline renderer ===")
product_path = os.path.join(SMRTDESK_DIR, 'product.html')
content = read(product_path)

# Fix the catPage variable in product.html inline renderer
# Old: var catPage = 'category-' + p.categorySlug + '.html';
# New: var catPage = 'category.html?slug=' + p.categorySlug;
old_format = "var catPage = 'category-' + p.categorySlug + '.html';"
new_format = "var catPage = 'category.html?slug=' + p.categorySlug;"
if old_format in content:
    content = content.replace(old_format, new_format)
    write(product_path, content)
    print("  [OK] Fixed product.html catPage link format")
else:
    print("  [INFO] product.html catPage already fixed or not found")

# ========================================================================
# FIX 5: Fix smrtdesk.js breadcrumb links in rendering functions
# ========================================================================
print("\n=== FIX 5: Fix smrtdesk.js rendering functions ===")
js_path = os.path.join(SMRTDESK_DIR, 'smrtdesk.js')
content = read(js_path)
old_content = content
changes = 0

# 5a. Fix any 'category-' + XXX + '.html' in category page renderer breadcrumb
# The Category Page Renderer already uses 'category.html?slug=' format (verified).
# But product page renderer might have old format from smrtdesk.js
# Actually the product renderer at line 2586 already uses 'category.html?slug='
# Let's just be thorough and replace any remaining old format
content = content.replace(
    "'category-' + cat.parentSlug + '.html'",
    "'category.html?slug=' + cat.parentSlug"
)
content = content.replace(
    "'category-' + article.category + '.html'",
    "'category.html?slug=' + article.category"
)

# 5b. Add product detail page links to product cards in Category Page Renderer
# Current: '<h3 class="product-card__title">' + (p.title || 'Product') + '</h3>'
# New:     '<a href="product.html?asin=' + (p.asin || p.sku) + '" style="text-decoration:none;color:inherit;"><h3 class="product-card__title">' + (p.title || 'Product') + '</h3></a>'
old_title_pattern = "'<h3 class=\"product-card__title\">' + (p.title || 'Product') + '</h3>'"
new_title_pattern = "'<a href=\"product.html?asin=' + (p.asin || p.sku) + '\" style=\"text-decoration:none;color:inherit;\"><h3 class=\"product-card__title\">' + (p.title || 'Product') + '</h3></a>'"
if old_title_pattern in content:
    content = content.replace(old_title_pattern, new_title_pattern)
    changes += 1

# 5c. Same fix for the carousel product cards in smrtdesk.js (line 2526 area)
# The carousel uses a different pattern - check if it renders product cards
old_carousel_title = "'<h3 class=\"product-card__title\">' + (p.title || 'Product') + '</h3>' +"
new_carousel_title = "'<a href=\"product.html?asin=' + (p.asin || p.sku) + '\" style=\"text-decoration:none;color:inherit;\"><h3 class=\"product-card__title\">' + (p.title || 'Product') + '</h3></a>' +"
if old_carousel_title in content:
    content = content.replace(old_carousel_title, new_carousel_title)
    changes += 1

if content != old_content:
    write(js_path, content)
    print(f"  [OK] smrtdesk.js ({changes} changes)")

# ========================================================================
# FIX 6: Add missing SUBCATEGORIES entries to smrtdesk.js
# ========================================================================
print("\n=== FIX 6: Add missing SUBCATEGORIES entries ===")

# Read current SUBCATEGORIES block
# Find the closing }; of SUBCATEGORIES
su_match = re.search(r'(var SUBCATEGORIES = \{.*?\n\};)', content, re.DOTALL)
if su_match:
    su_block = su_match.group(1)
    missing_entries = [
        '"desk-accessories": { name: "Desk Accessories", parent: "Office Furniture", parentSlug: "office-furniture" }',
        '"cabinet-organizer": { name: "Cabinet Organizer", parent: "Office Furniture", parentSlug: "office-furniture" }',
        '"filing-cabinet": { name: "Filing Cabinet", parent: "Office Furniture", parentSlug: "office-furniture" }',
        '"monitor-stand": { name: "Monitor Stand", parent: "Office Furniture", parentSlug: "office-furniture" }',
        '"computer-accessories": { name: "Computer Accessories", parent: "Office Furniture", parentSlug: "office-furniture" }',
        '"laptop-accessories": { name: "Laptop Accessories", parent: "Office Furniture", parentSlug: "office-furniture" }',
        '"phone-accessories": { name: "Phone Accessories", parent: "Office Furniture", parentSlug: "office-furniture" }',
        '"home-garden": { name: "Home & Garden", parent: "Home", parentSlug: "" }',
        '"kitchen": { name: "Kitchen", parent: "Kitchen & Dining", parentSlug: "kitchen-storage-organizer" }',
        '"steel-lockers": { name: "Steel Lockers", parent: "Office Furniture", parentSlug: "office-furniture" }',
        '"garage-cabinets": { name: "Garage Cabinets", parent: "Office Furniture", parentSlug: "office-furniture" }',
        '"trending": { name: "Trending", parent: "Home", parentSlug: "" }',
        '"deals": { name: "Best Deals", parent: "Home", parentSlug: "" }',
        '"smart-home-gadgets": { name: "Smart Home Gadgets", parent: "Electronics", parentSlug: "electronics" }',
    ]
    
    # Only add entries that don't already exist
    existing_slugs = set(re.findall(r'"(\w[\w-]*)"\s*:', su_block))
    to_add = []
    for entry in missing_entries:
        slug = entry.split('":')[0].strip('"')
        if slug not in existing_slugs:
            to_add.append(entry)
    
    if to_add:
        # Insert before the closing }; of SUBCATEGORIES
        insert_text = '\n  ' + ',\n  '.join(to_add) + '\n'
        content = content.replace('\n};\n\n/* SmrtDesk Article Data */', insert_text + '};\n\n/* SmrtDesk Article Data */', 1)
        write(js_path, content)
        print(f"  [OK] Added {len(to_add)} missing SUBCATEGORIES: {[e.split('\":')[0].strip('\"') for e in to_add]}")
    else:
        print("  [INFO] All SUBCATEGORIES already present")
else:
    print("  [FAIL] Could not find SUBCATEGORIES block")

# ========================================================================
# VERIFICATION
# ========================================================================
print("\n=== VERIFICATION ===")

# V1: Check all CSS versions are v=22
print("\n--- CSS Version Check ---")
all_v22 = True
for fname in os.listdir(SMRTDESK_DIR):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(SMRTDESK_DIR, fname)
    content = read(fpath)
    versions = re.findall(r'main\.css\?v=(\d+)', content)
    if versions:
        if not all(v == '22' for v in versions):
            print(f"  [FAIL] {fname}: {versions}")
            all_v22 = False
    else:
        print(f"  [FAIL] {fname}: NO main.css reference!")
        all_v22 = False

if all_v22:
    print("  [OK] All CSS versions = v=22")

# V2: Check no old category-xxx.html links
print("\n--- Old Category Links Check ---")
found_old = False
for fname in os.listdir(SMRTDESK_DIR):
    if not fname.endswith('.html') and not fname.endswith('.js'):
        continue
    fpath = os.path.join(SMRTDESK_DIR, fname)
    content = read(fpath)
    old_links = re.findall(r'href="category-\w[\w-]*\.html"', content)
    # Also check JS string concatenation patterns
    old_js_links = re.findall(r"'category-' \+ \w+\.\w+ \+ '\.html'", content)
    if old_links or old_js_links:
        print(f"  [FAIL] {fname}: {old_links}{old_js_links}")
        found_old = True

if not found_old:
    print("  [OK] No old category-xxx.html links found")

# V3: Check no slug=kitchen (bare, without -storage-organizer etc)
print("\n--- Kitchen Slug Check ---")
bad_kitchen = False
for fname in os.listdir(SMRTDESK_DIR):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(SMRTDESK_DIR, fname)
    content = read(fpath)
    # Find slug=kitchen" that is NOT slug=kitchen-something"
    matches = re.findall(r'slug=(kitchen)["\&]', content)
    if matches:
        print(f"  [FAIL] {fname}: {matches}")
        bad_kitchen = True

if not bad_kitchen:
    print("  [OK] No bare slug=kitchen found")

# V4: Check product cards have product links
print("\n--- Product Card Link Check ---")
js_content2 = read(js_path)
if 'product.html?asin=' in js_content2:
    print("  [OK] Product card titles link to product.html?asin=")
else:
    print("  [FAIL] Product card links NOT found in smrtdesk.js")

print("\n=== ALL FIXES COMPLETE ===")
