import json

with open('data.json', 'r') as f:
    data = json.load(f)

outlist = []

for key, value in data.items():
    dict_item = {}
    def read_all(current, parent_key=None):
        for k, v in current.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            if isinstance(v, dict):
                read_all(v, new_key)
            else:
                if isinstance(v, list):
                    for i in range(len(v)):
                        new_key = f"{parent_key}.{k}.{i}"
                        if isinstance(v, dict):
                            read_all(v, new_key)
                        else:
                            new_key = f"{parent_key}.{k}.{i}"
                            if isinstance(v[i], dict):
                                read_all(v[i], new_key)
                            else:
                                dict_item[new_key] = v[i]                
                else:
                    dict_item[new_key] = v
    
    read_all(value)
    outlist.append({key: dict_item})

formatted_output = json.dumps(outlist, indent=4)

with open('items.txt', 'w') as output_file:
    output_file.write(formatted_output)

print(outlist)
