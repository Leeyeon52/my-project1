import os
os.chdir('C:/doit')
f = os.popen('dir')
result = os.popen('dir')
print(result.read())