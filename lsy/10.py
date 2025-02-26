import sys

args =sys.argv[1:]
sum = 0
for i in args:
    sum += int(i)
print(sum)