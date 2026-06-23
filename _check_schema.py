import os, re, json, glob
os.chdir('D:/openclaw/workspace/smrtdesk')

# Check index.html
with open('index.html','r',encoding='utf-8') as f:
    c = f.read()
schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', c, re.DOTALL)
print('=== 首页 Schema 检查 ===')
print(f'Schema 数量: {len(schemas)}')
for i, s in enumerate(schemas):
    try:
        data = json.loads(s)
        print(f'  Schema #{i+1} @type: {data.get("@type","unknown")}')
        if '@graph' in data:
            for j, item in enumerate(data['@graph']):
                print(f'    子项 #{j+1}: {item.get("@type","unknown")}')
    except Exception as e:
        print(f'  Schema #{i+1} 解析失败: {e}')
        print(f'  原始内容(前200字符): {s[:200]}')

# Check product pages
print('\n=== 产品页 Schema 抽查 (前10个) ===')
product_files = glob.glob('product-*.html')[:10]
for f in product_files:
    with open(f,'r',encoding='utf-8') as fp:
        c = fp.read()
    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', c, re.DOTALL)
    print(f'\n{f}: {len(schemas)} schemas')
    for s in schemas[:1]:
        try:
            data = json.loads(s)
            t = data.get('@type','unknown')
            print(f'  @type: {t}')
            if isinstance(data, dict):
                name = data.get('name','MISSING')
                nd = data.get('description','MISSING')
                print(f'  name: {name[:60]}')
                offers = data.get('offers', None)
                if offers:
                    if isinstance(offers, dict):
                        print(f'  price: {offers.get("price","MISSING")}, currency: {offers.get("priceCurrency","MISSING")}')
                        print(f'  availability: {offers.get("availability","MISSING")}')
                    elif isinstance(offers, list) and len(offers)>0:
                        print(f'  price: {offers[0].get("price","MISSING")}')
                else:
                    print(f'  offers: MISSING')
                rating = data.get('aggregateRating', None)
                if rating:
                    print(f'  rating: {rating.get("ratingValue","MISSING")}/{rating.get("bestRating","?")} ({rating.get("reviewCount","?")} reviews)')
                else:
                    print(f'  aggregateRating: MISSING')
                brand = data.get('brand', None)
                if brand:
                    if isinstance(brand, dict):
                        print(f'  brand: {brand.get("name","?")}')
                    else:
                        print(f'  brand: {brand}')
                else:
                    print(f'  brand: MISSING')
                img = data.get('image', 'MISSING')
                print(f'  image: {"present" if img != "MISSING" else "MISSING"}')
        except Exception as e:
            print(f'  解析失败: {e}')

# Other pages
print('\n=== 其他页面 Schema 检查 ===')
pages = ['category-standing-desk.html', 'category-office-furniture.html', 'review.html', 'search.html', 'page-about.html', 'page-faq.html']
for f in pages:
    if os.path.exists(f):
        with open(f,'r',encoding='utf-8') as fp:
            c = fp.read()
        schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', c, re.DOTALL)
        print(f'{f}: {len(schemas)} schemas')
        for i, s in enumerate(schemas):
            try:
                data = json.loads(s)
                t = data.get('@type','unknown')
                if '@graph' in data:
                    types = [item.get('@type','?') for item in data['@graph']]
                    print(f'  Schema #{i+1}: @graph with {len(data["@graph"])} items: {types}')
                else:
                    print(f'  Schema #{i+1}: @type={t}')
            except:
                print(f'  Schema #{i+1}: 解析失败')
    else:
        print(f'{f}: 文件不存在')
