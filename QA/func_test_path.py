from os.path import exists

file_exists = exists('city.json')

print(file_exists)

file2_exists = exists('int.json')
print(file2_exists)

with open("interations.json", "w") as outfile:
    data = '[]'
    outfile.write(data)