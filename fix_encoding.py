import re
import glob

for filepath in ['templates/fertilizer.html', 'templates/market.html']:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Fix the price template string
        content = re.sub(r'[^a-zA-Z0-9<>\s\"\':;/=\-]*\$\{item\.price\.toLocaleString\(\)\}', r'₹${item.price.toLocaleString()}', content)

        # Fix other instances of corrupted rupee
        content = re.sub(r',1', '₹', content)
        content = re.sub(r'', '₹', content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed encoding in {filepath}')
    except Exception as e:
        print(f'Error processing {filepath}: {e}')
