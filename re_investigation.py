import re

text = """
this is a test string
here are numbers 123
3456
786
some more text
"""

matches = re.findall("[0-9]+", text)

print (matches)

for match in matches:
    print (match)




