import os

for filename in ['login.html', 'signup.html']:
    filepath = os.path.join('templates', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '{% include \'navbar.html\' %}' not in content:
        page_name = filename.split('.')[0]
        replacement = f"<body>\n\n{{% set active_page = '{page_name}' %}}\n{{% include 'navbar.html' %}}"
        content = content.replace('<body>', replacement)
        
        # Also, the body has flex centered which will ruin the navbar layout.
        content = content.replace('body{', 'body{\n  flex-direction: column;\n  align-items: stretch;\n  justify-content: flex-start;')
        content = content.replace('height:100vh;', 'min-height:100vh; height:auto;')
        
        # Wrap the card in a main container
        content = content.replace('<div class="card">', '<main style="flex: 1; display: flex; justify-content: center; align-items: center; padding: 40px;">\n<div class="card">')
        content = content.replace('</body>', '</main>\n</body>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {filename}')
