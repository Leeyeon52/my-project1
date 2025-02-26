#쳇 gpt를 활용한 파이썬 연습문문
#아래와 같은 간단한 모듈 calculator.py를 작성하고, 다른 파이썬 스크립트에서 이 모듈을 사용해보세요.


def add(a,b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        print('0으로 나눌 수 없습니다')
    else:
        return a / b

# main.py 파일
import calculator

print(calculator.add(3, 4))      # 출력: 7
print(calculator.subtract(3, 4)) # 출력: -
