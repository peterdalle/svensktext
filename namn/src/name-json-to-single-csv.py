# Convert names in separate JSON files (kvinnonamn.json and mansnamn.json) to
# a single CSV file (namn.csv) with `name` and `gender` headers.
import json
import csv

print("Converting...")

# Read JSON to list.
f = open("kvinnonamn.json", "r", encoding="utf8")
females = json.load(f)
f.close()

# Read JSON to list.
f = open("mansnamn.json", "r", encoding="utf8")
males = json.load(f)
f.close()

# Write list to CSV with "name,gender" headers.
f = open("namn.csv", "w")
f.write("name,gender")

# Write females.
for name in females:
	f.write("\n")
	f.write("{0},{1}".format(name, "female"))
	
# Write males.
for name in males:
	f.write("\n")
	f.write("{0},{1}".format(name, "male"))
	
f.close()
print("Done.")