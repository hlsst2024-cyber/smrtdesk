import os, re, json, glob
os.chdir('D:/openclaw/workspace/smrtdesk')
pattern = r'<script type="application/ld\+json">(.*?)</script>'
product_files = glob.glob('product-*.html')
invalid = []
for f in product_files:
    with open(f,'r',encoding='utf-8') as fp:
        c = fp.read()
    schemas = re.findall(pattern, c, re.DOTALL)
    for s in schemas:
        try:
            json.loads(s)
        except:
            invalid.append(f)
            break
print(f'Total: {len(product_files)}, Invalid schemas: {len(invalid)}')
for f in invalid:
    print(f'  {f}')
if not invalid:
    print('All schemas now valid!')
