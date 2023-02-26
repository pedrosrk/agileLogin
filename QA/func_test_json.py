import json

# Open file
with open('city.json', 'r') as f:
  data = json.load(f)
  # print(data, type(data))
  # Update the data
  example = {
    "name"  :"Sam",
    "age"   :30,
    "gender":"fem"
  }
  data.append(example)
  json_object = json.dumps(data, indent=2)

with open("city.json", "w") as outfile:
    outfile.write(json_object)

