num = 13
if num % 2 == 0:
    print('짝수')
else:
    print('홀수')


num = '881120-1068234'
print(num[:6])
print(num[7:])
print(num[7])



a = 'a:b:c:d'
print(a.replace(':','#'))
new_a = a
print


a = [1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)

a = ['Life', 'is', 'too', 'short']
print(' '.join(a))


a = (1,2,3)
b = (4,)
print(type(b))
print(a + b)



a = dict()
a['name'] = 'python'
print(a)


a[('a',)] = 'python'
print(a)

#a[[1]] = 'python'
print(a)

a[250] = 'python'
print(a)


'''

a = {'A':90, 'B':80, 'C':70}
print(a['B'])


a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
set_a = set(a)
print(set_a)

last_a = list(set_a)
print(last_a)


a = b = [1, 2, 3]
print(id(a),id(b))
a[1] = 4
print(b)

today = '월요일'
if today == '월요일':
    print('학교가야지')
elif today == '토요일':
    print('영화 보자')
else:
    print('숙제')
print('숙제시작')


if today == '일요일':
    print('게임 한 판')
elif today == '토요일':
    print('폰 5분만')
else:
    print('물 한 잔')
    print('공부 시작')


yellow_card = 3
foul = False
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else:
        print('휴.. 조심해야지')
else:
    print('주의')


for x in range(20):
    print(f'팔 벌려 뛰기{x}')

for x in range(1,30,5):
    print(f'팔 벌려 뛰기{x}번 ')




my_list = [1,2,3]
for x in my_list:
    print(x)

person = {'이름': '나귀욤', '나이': 7,'키': 150, '몸무게': 50}
for k,v in person.items():
    print(v)
'''


max = 25
weight = 0
item = 3

while weight + item <=max:
    weight += item
    print(f'짐을 {weight} 추가합니다')
print(f'총 무게는 {weight}입니다.')

max = 25
weight = 15
item = 2

while weight + item >=max:
    weight += item
    print(f'짐을 {weight}추가합니다')
print(f'총 무게는 {weight}입니다.')


drama = ['시즌1','시즌2','시즌3','시즌4','시즌5']
for x in drama:
    if x == '시즌3':
        print('재미 없음')
        continue
    print(f'{x}')


for x in range(10):
    if x % 2 == 1:
        continue
    print(x)




products = ['JOA-2020','JOA-2021','SIRO-2021', 'SIRO-2022']
recall = []
for x in products:
    if x.startswith('SIRO'):
        recall.append(x)
print(recall)


products = ['JOA-2020','JOA-2021','SIRO-2021', 'SIRO-2022']
recall2 = [x for x in products if x.startswith('SIRO')]
print(recall2)