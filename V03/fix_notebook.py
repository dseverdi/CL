import json

with open('Python_Regex_II.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if 'outputs' in cell:
        for output in cell['outputs']:
            if 'data' in output and 'image/svg+xml' in output['data']:
                svg_lines = output['data']['image/svg+xml']
                # Remove lines that start with <?xml
                filtered_lines = [line for line in svg_lines if not line.strip().startswith('<?xml')]
                output['data']['image/svg+xml'] = filtered_lines

with open('Python_Regex_II.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)