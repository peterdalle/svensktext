# Convert names in separate JSON files (kvinnonamn.json and mansnamn.json)
# to separate CSV files.
import json
import csv

# Files to convert from and to.
json_filename = "kvinnonamn.json"
csv_filename = "kvinnonamn.csv"
print("Converting {0} to {1}...".format(json_filename, csv_filename))

# Read JSON to list.
f = open(json_filename, "r", encoding="utf8")
l = json.load(f)
f.close()

# Write list to CSV.
f = open(csv_filename, "w")
for row in l:
	f.write(row)
	f.write("\n")

print("Done.")