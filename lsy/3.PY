'''
message = '나는 전역 변수'
def secret():
    message = '이건 나만의 비밀'
    print(message)
    message = '함수내에서 변경함'
    print(message)

secret()
'''
message = '나는 전력 변수'

def  no_secret():
    global message
    message = '진짜 전역변수?'
    print(message, id(message))

no_secret()
print(message, id(message))