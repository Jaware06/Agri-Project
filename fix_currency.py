import glob

for filepath in ['templates/fertilizer.html', 'templates/market.html']:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace ? with ₹ where it comes right before ${
        content = content.replace('?${', '₹${')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed currency symbol in {filepath}')
    except Exception as e:
        print(f'Error processing {filepath}: {e}')
