num1 = 3
num2 = '0'
try:
    int('3.14')
    result = num1 / num2
    print(f'연산 결과는 {result}입니다.')

except ZeroDivisionError:
    print('0으로 나룰 수 없어요')

except TypeError:
    print('값의 타입이 이상해요')


except Exception as err:
    print('에러남')
    print('에러명 :', err)

else:
    print('정상동작중')

finally:
    print('수행종료')