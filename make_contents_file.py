import json
import os

contents = []
rpRoot = './'

for root, dirs, files in os.walk(rpRoot):
    for file in files:
        contents.append({
            'path': os.path.join(root, file).replace(rpRoot, '').replace('\\', '/')
        })

with open(os.path.join(rpRoot, "contents.json"), mode='w', encoding='utf-8') as file:
    file.write(json.dumps({'content': contents}, indent=2))