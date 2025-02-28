import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = '''
Elice 123456-1234567 010-1234-5678
Cheshire 345678-678901 01098765432
'''

p1 = "(010)\D?\d{4}\D?(\d{4})"          # 정규식 패턴 입력!

print("m1 결과 : ", re.sub(p1, "\g<1>-****-\g<2>", text))
