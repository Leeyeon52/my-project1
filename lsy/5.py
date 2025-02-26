f = open('list.txt', 'r', encoding ='utf8')
'''f.write('김xx\n')
f.write('정xx\n')
f.write('허xx\n')
f.close()

contents = f.read()
print(contents)
f.close()
'''
for line in f:    
    print(line,end='')
f.close