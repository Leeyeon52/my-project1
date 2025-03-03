import re

p = re.compile('[a-z]+')
m = p.search("5 python")
print(m.end())
print(m.end())
print(m.end())
print(m.start() + m.end())