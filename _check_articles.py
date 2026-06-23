import os, re, json, glob
os.chdir('D:/openclaw/workspace/smrtdesk')
pattern = r'<script type="application/ld\+json">(.*?)</script>'
articles = glob.glob('article-*.html')
print('=== Article Schema Types ===')
for f in articles:
    with open(f,'r',encoding='utf-8') as fp:
        c = fp.read()
    schemas = re.findall(pattern, c, re.DOTALL)
    for s in schemas:
        try:
            data = json.loads(s)
            t = data.get('@type','?')
            dp = data.get('datePublished','?')
            dm = data.get('dateModified','?')
            headline = data.get('headline','')[:60]
            print(f'{f}: @type={t}, published={dp}, modified={dm}, headline={headline}')
        except:
            print(f'{f}: INVALID JSON')
