import string
import sys

first_letter_chars = string.ascii_lowercase + "åäö" + "1234567890" # ascii_lowercase = a-z

print("Reading...")
svwiki_titles = []
with open("svwiki-latest-all-titles-in-ns0", encoding="utf-8") as f:
	for line in f.readlines():
		svwiki_titles.append(line)

num_titles = len(svwiki_titles)
print("Found", num_titles, "titles")

def get_list_starts_with(char, titles):
	print("Getting titles starting with", char)
	return [title for title in titles if title.lower().startswith(char)]

def get_remaining_titles(titles):
	print("Getting remaining chars...")
	return [title for title in titles if not title.lower()[0] in first_letter_chars]

alltitles = {}
for char in first_letter_chars:
	if char not in alltitles:
		alltitles[char] = []
	alltitles[char] = get_list_starts_with(char, svwiki_titles)

# Get remaining characters.
alltitles["_"] = []
alltitles["_"] = get_remaining_titles(svwiki_titles)

del svwiki_titles

print()
for k, v in alltitles.items():
	print("Writing to {}.txt".format(k))
	with open(k + ".txt", "a", encoding="utf-8") as f:
		for line in v:
			f.write(line)
print("Done.")