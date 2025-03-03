import re

test = """
park 010-9999-9998
kim 010-9909-7789
lee 010-8789-7768
"""
 

modified_test = re.sub("(\d{3}[-]\d{4})[-]\d{4}")
result = re.sub("\g<1>-####",test)

print(result)