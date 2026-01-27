"""
Python JSON File Handling – Complete Guide
1. What JSON Really Is (No theory fluff)

JSON = structured text data (key–value, lists, nested objects)

Used for:

ML configs

Test configurations

API responses

Application state

Model metadata
"""

# Reading JSON using file handling
import json
with open("config.json") as json_file:
    config = json.load(json_file)

    print(config['training'])

json_text = '{"model": "LinearRegression", "accuracy": 0.91}'

data = json.loads(json_text)

print(data['model'])


result = {
    "model": "LinearRegression",
    "accuracy": 0.94,
    "loss": 0.02
}

with open("config.json", "r") as json_file:
    data = json.load(json_file)


import json

with open("config.json", "r") as file:
    data = json.load(file)

data["training"]["epochs"] = 100

data.setdefault("last_updated", "2026-01-26")

data.pop("enabled", None)
with open("config.json", "w") as file:
    json.dump(data, file, indent=4)


# with open("config.json", "w") as json_file:
#     data.dump(json_file)

# with open('config.json', 'a') as outfile:
#     json.dump(result, outfile, indent=4)

with open("config.json") as json_file:
    reader = json.load(json_file)
    print(reader)


# json_text = json.dumps(result, indent=4)
# print(json_text)