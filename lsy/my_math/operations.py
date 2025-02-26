# my_math/operations.py 파일
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# main.py 파일
from my_math.operations import add, subtract

print(add(3, 4))      # 출력: 7
print(subtract(3, 4)) # 출력: -1

