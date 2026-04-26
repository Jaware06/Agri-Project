import glob
import re
import os

html_files = glob.glob('templates/*.html')

# We want to exclude navbar.html, login.html, signup.html
targets = ['index.html', 'crop.html', 'disease.html', 'farming.html', 'fertilizer.html', 'market.html', 'scheme.html']

for target in targets:
    filepath = os.path.join('templates', target)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We are looking for: <header class="topbar"> ... </header>
    # Using regex to find the block
    pattern = re.compile(r'<header class="topbar">.*?</header>', re.DOTALL)
    
    page_name = target.split('.')[0]
    replacement = f"{{% set active_page = '{page_name}' %}}\n{{% include 'navbar.html' %}}"

    new_content = pattern.sub(replacement, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {target}')
    else:
        print(f'No topbar found or already updated in {target}')
