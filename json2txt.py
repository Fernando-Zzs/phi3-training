from config import DATA_ROOT
import json

with open(DATA_ROOT + 'Wikipedia CN filtered.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

completions = [item['completion'] for item in data]

with open(DATA_ROOT + 'tokenizer_wiki.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(completions))

print("Done!")