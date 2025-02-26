a  = 'Life is too short, you need python'
if 'Wife' in a:
    print('Wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:
    print('shirt')
elif 'need' in a:
    print('need')
else:
    print('none')


result = 0
i = 1

while  i <= 1000:
    if i % 3 ==0: 
        result += i
    i += 1
print(result)




a = 0
while  True:
    a += 1
    if a > 5:
        break
    print('*'*a)



for c in  range(1,101):
    print(c)





A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score
average = total/len(A)
print(average)


num = [1,2,3,4,5]
result = [n*2 for n in num if n %2 == 1]
print(result)

print('hello world')
print("Mary's cosmeeetics")
print('신씨가 소리질렀다."도둑이야"')
print('C:\window')
print('안녕하세요.\n만나서\t\t반갑습니다.')
print('오늘은','일요일')
print('naver','kakao','sk','samsung',sep= ';')
print('naver','kakako','sk','samsung', sep='/')
print('first',end = '');print('second')
print(5/3)
print(50000*10)
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

