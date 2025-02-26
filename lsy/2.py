def print_kwargs(**a):
    print(a)
    return(a)

res = print_kwargs(name='foo',age=3, height=150)
print(type(res))



def secret():
    message = '이건 나만의 비밀'
    print(message)
    message = '함수내에서 변경함'
    print(message)

secret()


def please():
    message = '이건 가능?'
    print(message)
please()


