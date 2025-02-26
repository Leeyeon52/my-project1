'''
print(True)
int  (  ) 정수로  -> 변환불가  ex) int('5.9')x  ->   print(int('5.9'))x 오류 뜸   ->   print(int(float('3.14)))o 
float (  ) 실수로
str (  ) 문자로
bool (  ) 

print(7 % 3)
print(3 % 7)


print(7//4)
print(5//3)


a = 80
b = 75
c = 55
d = print(float(a+b+c)/3)


print('c'in ' dog')


my_list = [4,5,6,7]
print(my_list)




lang = "anconda"
print(lang[1:]) # 1번 부터 끝까지
print(lang[:6]) # 처음부터 인덱싱 5번까지
print(lang[2:7]) # 인덱싱 2번부터 6번까지
print(lang[-2:-6]) # 
print(lang[:]) # 전체
print(lang)


person = {'name':'pey','phone':'010-9999-1234','birth': '1118'}

print(person['name'])
print(person['phone'])
print(person['birth'])
print(person.get('nickname'))  # key error


person['birth'] = 1119
print(person['birth'])
person = {'name':'leo','phone':'010-1234-9999'}
print(person['phone'])
print(person['name'])
person.clear()



snack = '새우깡'
five = '5개'
juseyo = snack + five
juseyo = juseyo + '주세요'
print(juseyo)
juseyo += '주세요'
print(juseyo)

num = 5
num = num + 2
print(num)

num = num *3
num = num/5
print(num)


snack = "새우 깡"
4개
있네요.
print(snack)




print('-'*15)
print('안녕하세요')
print('-'*15)

letter = "How are you?"
print(letter.lower())               
print(letter.upper())          
print(letter.capitalize())   
print(letter.title())   
print(letter.swapcase()) 
print(letter.split())   
print(letter.count('How'))



b = '...나도 초등학교...   '
print(b.replace('초등','중'))
print(b.find('학교'))
print(b.center(10,'-'))

python = "파이썬"
java = '자바'
C = 'C언어'
print(python + java)
print(python , java, C)
print('개발 언어에는 {2},{1},{0}가 있어요.'.format(python, java,C)) 
print(f'개발 언어에는 {python}, {java}, {C}가 있어요.')


print('동생이''파이썬 배우기 쉬워?''하고 물었다.')
print("나는 속으로 '엄청 어려운데...'라고 생각했다.")
print('하지만 \'나만 당할 순 없지\' 라는 생각에\ "엄청 쉽지\"라고 했다.')


snack  = 꿀꽈배기는
너무
맛있어요
print(snack)

my_list = ['오예스', '몽쉘', '초코파이', '초코파이', '카카오 초콜릿']
print(my_list[0])
print(my_list[-1])
print(my_list[-3])
print(my_list[2:])
print(my_list[1:3])
print('카카오'in my_list)
print(len(my_list))
my_list[1] = '카카오 몽쉘'
my_list[3] = '딸기 초코파이'
print(my_list)
my_list.append('오뜨')
print(my_list)
my_list.remove('오예스')
print(my_list)
your_list = ['빅파이', '가나초콜릿']
print(my_list + your_list)

my_list.extend(your_list)
print(my_list)
my_list.pop()
print(my_list)
copy_list = my_list.copy()
print(my_list)

my_tuple = ('오예스', '몽쉘', '초코파이')
#print(len(my_tuple))
pie1, pie2, pie3 = my_tuple
print(pie1, pie2, pie3 )

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
(*others,nine, ten) = numbers
print(nine)
print(ten)
print(others)

A = {'스파게티', '족빌', '카레'}
B = {'족발','치킨','피자'}
print(A.intersection(B))
print(A.union(B))
print(A.difference(B))   # is...() 가 있으면 trure  or false로 나옴





person = {'이름': '나귀욤', '나이': 7,'키': 150, '몸무게': 50}
print(person['나이'])
print(person['이름'])
print(person['학교'])  
print(person.get('학교'))
person['학교'] = '헬가 고등학교'
print(person)
person.update({'키':155,'학교': '대학교'})
print(person)
person.pop('몸무게')
print(person)
person.clear()
print(person)
print(person(keys))    # key 만
print(person(values))  # values만 
print(person(items))   # 전부

print(person.popitem())
print(person.setdefault('이름'))



my_tuple = ('오예스', '몽쉘')
my_list = list(my_tuple)
print(my_list, type(my_list))
my_list.append('빅파이')
my_tuple = tuple(my_list)
print(my_tuple)


my_list = ['오예스', '몽쉘', '초코파이', '초코파이', '초코파이']
my_dict = dict.fromkeys(my_list)
print(my_dict)
my_list = list(my_dict)
print(my_list)
'''