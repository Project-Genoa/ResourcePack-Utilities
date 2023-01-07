import json
import os

textureTypes = ['tga', 'tiff', 'png', 'jpg']
contents = []
rpRoot = './'

for root, dirs, files in os.walk(os.path.join(rpRoot, 'textures')):
    for file in files:
        if (file.split('.')[-1] in textureTypes):
            contents.append(os.path.join( root, '.'.join(file.split('.')[:-1]).replace(rpRoot, '') ).replace('\\', '/'))

with open(os.path.join(rpRoot, 'textures', "textures_list.json"), mode='w', encoding='utf-8') as file:
    file.write(json.dumps(contents, indent=2))