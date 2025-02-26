with open('list.txt', 'r', encoding ='utf8') as f:
    '''f.write('가나다\n')
    f.write('가나다\n')
    f.write('가나다\n')'''
    contents = f.read()
    print(contents)
