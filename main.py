import json

# open infinitecraft.json
with open('infinitecraft.json') as f:
    pc = json.load(f)
with open('mobile.json') as f:
    mobile = json.load(f)

pc_elements = []
for element in pc['elements']:
    pc_elements.append(element['text'])

for element in mobile['elements']:
    if element['text'] not in pc_elements:
        pc['elements'].append({
            "text": element['text'],
            "emoji": element['emoji'],
            "discovered": False
        })

with open('infinitecraft2.json', 'w', encoding='utf-8') as f:
    json.dump(pc, f, indent=2)