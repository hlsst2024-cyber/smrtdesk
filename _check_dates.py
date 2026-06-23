import os, re
os.chdir('D:/openclaw/workspace/smrtdesk')

# Check article date structure
with open('article-home-office-setup.html','r',encoding='utf-8') as f:
    c = f.read()

# date meta
metas = re.findall(r'<meta[^>]*>', c)
date_metas = [m for m in metas if 'date' in m.lower() or 'published' in m.lower() or 'modified' in m.lower()]
print('Date-related meta tags:')
for m in date_metas:
    print(f'  {m}')

# ISO dates
all_dates = re.findall(r'20\d{2}[-/]\d{2}[-/]\d{2}', c)
print(f'\nISO dates found: {all_dates[:10]}')

# Published/Updated text
pub = re.findall(r'Publishe?d\s*:?\s*[^<]*', c, re.IGNORECASE)
mod = re.findall(r'Update?d\s*:?\s*[^<]*', c, re.IGNORECASE)
print(f'\nPublished text: {pub[:5]}')
print(f'Updated text: {mod[:5]}')

# time elements
times = re.findall(r'<time[^>]*>(.*?)</time>', c, re.DOTALL)
print(f'\nTime elements: {times[:5]}')

# check for schema datePublished
pattern = r'<script type="application/ld\+json">(.*?)</script>'
schemas = re.findall(pattern, c, re.DOTALL)
import json
for s in schemas:
    try:
        data = json.loads(s)
        dp = data.get('datePublished','NOT FOUND')
        dm = data.get('dateModified','NOT FOUND')
        print(f'\nSchema datePublished: {dp}')
        print(f'Schema dateModified: {dm}')
    except:
        pass

# Also check what category-standing-desk bottom looks like
print('\n=== category-standing-desk bottom ===')
with open('category-standing-desk.html','r',encoding='utf-8') as f:
    c2 = f.read()
lines = c2.split('\n')
for i in range(max(0,len(lines)-30), len(lines)):
    print(f'{i}: {lines[i][:120]}')
