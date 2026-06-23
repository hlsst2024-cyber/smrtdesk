import os, re, json
os.chdir('D:/openclaw/workspace/smrtdesk')
bad_files = [
    'product-elegear-cumbrex-4-thick-self-inflating-sleeping-pad.html',
    'product-songmics-43-clothes-garment-rack-with-shelves-heavy-duty.html',
    'product-veradek-metallic-series-tall-tapered-planter-24.html'
]
for f in bad_files:
    with open(f,'r',encoding='utf-8') as fp:
        c = fp.read()
    pattern = r'<script type="application/ld\+json">(.*?)</script>'
    schemas = re.findall(pattern, c, re.DOTALL)
    print(f'=== {f} ===')
    for i, s in enumerate(schemas):
        print(f'  Schema #{i+1}:')
        try:
            json.loads(s)
            print('    OK')
        except json.JSONDecodeError as e:
            print(f'    INVALID at pos {e.pos}: {e}')
            pos = e.pos
            print(f'    Context: ...{s[max(0,pos-40):pos+40]}...')
    print()

# Also check full product schema structure
with open('product-ergear-height-adjustable-electric-standing-desk-48x24.html','r',encoding='utf-8') as f:
    c = f.read()
schemas = re.findall(pattern, c, re.DOTALL)
print('=== Sample product schema keys ===')
for s in schemas:
    try:
        data = json.loads(s)
        print('Top keys:', list(data.keys()))
        for k, v in data.items():
            if isinstance(v, (str, int, float, bool)):
                print(f'  {k}: {v}' if len(str(v)) < 100 else f'  {k}: {str(v)[:100]}...')
            elif isinstance(v, list):
                print(f'  {k}: list[{len(v)}]')
            elif isinstance(v, dict):
                print(f'  {k}: dict keys={list(v.keys())[:5]}')
        break
    except Exception as e:
        print('Error:', e)
