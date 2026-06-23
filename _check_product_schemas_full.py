import os, re, json, glob
os.chdir('D:/openclaw/workspace/smrtdesk')

issues = []
product_files = glob.glob('product-*.html')
missing_price = []
missing_brand = []
missing_rating = []
missing_image = []
missing_desc = []
valid_product = []
total = 0

for f in product_files:
    total += 1
    with open(f,'r',encoding='utf-8') as fp:
        c = fp.read()
    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', c, re.DOTALL)
    if not schemas:
        issues.append(f'{f}: NO schema at all')
        missing_price.append(f)
        missing_brand.append(f)
        missing_rating.append(f)
        missing_image.append(f)
        continue
    
    ok = True
    for s in schemas:
        try:
            data = json.loads(s)
        except:
            issues.append(f'{f}: Invalid JSON schema')
            ok = False
            continue
        
        t = data.get('@type','')
        if t != 'Product':
            continue
        
        price_ok = brand_ok = rating_ok = img_ok = desc_ok = False
        
        offers = data.get('offers')
        if offers:
            if isinstance(offers, dict):
                p = offers.get('price')
                if p is not None and p != "":
                    price_ok = True
            elif isinstance(offers, list) and len(offers) > 0:
                p = offers[0].get('price')
                if p is not None and p != "":
                    price_ok = True
        
        brand = data.get('brand')
        if brand:
            brand_ok = True
        
        rating = data.get('aggregateRating')
        if rating:
            rating_ok = True
        
        if data.get('image'):
            img_ok = True
        
        desc = data.get('description')
        if desc and len(desc) > 10:
            desc_ok = True
        elif not desc or len(desc) <= 10:
            pass  # minor
        
        if not price_ok:
            missing_price.append(f)
        if not brand_ok:
            missing_brand.append(f)
        if not rating_ok:
            missing_rating.append(f)
        if not img_ok:
            missing_image.append(f)
        
        if price_ok and brand_ok and img_ok:
            valid_product.append(f)
        break

print(f'总产品页: {total}')
print(f'\n--- 缺失 price: {len(missing_price)} ---')
for f in missing_price[:5]:
    print(f'  {f}')
if len(missing_price) > 5:
    print(f'  ... 共 {len(missing_price)} 个')

print(f'\n--- 缺失 brand: {len(missing_brand)} ---')
for f in missing_brand[:5]:
    print(f'  {f}')
if len(missing_brand) > 5:
    print(f'  ... 共 {len(missing_brand)} 个')

print(f'\n--- 缺失 aggregateRating: {len(missing_rating)} ---')
print(f'  (不是必须, 但有帮助)')

print(f'\n--- 缺失 image: {len(missing_image)} ---')
for f in missing_image[:5]:
    print(f'  {f}')

print(f'\n--- 完全有效 (price+brand+image): {len(valid_product)}/{total} ---')

print(f'\n--- 其他问题: ---')
for iss in issues:
    print(f'  {iss}')
