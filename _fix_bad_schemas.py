import os

os.chdir('D:/openclaw/workspace/smrtdesk')

# Fix 3 products with broken JSON schemas: unescaped double quotes in inch measurements
fixes = [
    {
        'file': 'product-elegear-cumbrex-4-thick-self-inflating-sleeping-pad.html',
        'replacements': [
            ('Elegear CumbreX 4" Thick Self-Inflating Sleeping Pad', 'Elegear CumbreX 4 inch Thick Self-Inflating Sleeping Pad'),
        ]
    },
    {
        'file': 'product-songmics-43-clothes-garment-rack-with-shelves-heavy-duty.html',
        'replacements': [
            ('SONGMICS 43" Clothes Garment Rack with Shelves Heavy Duty', 'SONGMICS 43 inch Clothes Garment Rack with Shelves Heavy Duty'),
        ]
    },
    {
        'file': 'product-veradek-metallic-series-tall-tapered-planter-24.html',
        'replacements': [
            ('Veradek Metallic Series Tall Tapered Planter 24"', 'Veradek Metallic Series Tall Tapered Planter 24 inch'),
        ]
    },
]

for fix in fixes:
    fpath = fix['file']
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    for old, new in fix['replacements']:
        content = content.replace(old, new)
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed: {fpath}')
        # Verify JSON now parses
        import re, json
        schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
        for s in schemas:
            try:
                json.loads(s)
                print(f'  Schema now VALID')
            except json.JSONDecodeError as e:
                print(f'  Schema STILL INVALID: {e}')
    else:
        print(f'No changes needed: {fpath}')
