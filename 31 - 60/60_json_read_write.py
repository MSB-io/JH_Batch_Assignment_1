import json

with open("data.json", "r") as file:
    data = json.load(file)

data["key"] = "new_value"

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)