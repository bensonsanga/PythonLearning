import re

pattern = re.compile(r"([a-zA-Z]).([h])")

string = "this search for regular this hexpressions"

a = pattern.search(string)
b = pattern.findall(string)
print(b)