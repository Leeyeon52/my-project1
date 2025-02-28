import re

pattern = re.compile('[a-z]+',re.I)
result = pattern.match('python PYTHON')
#result = pattern.search('3 Python')
#result = pattern.findall('life is too short')
print(result)
print(result.group())
print(result.start())
print(result.end())
print(result.span())