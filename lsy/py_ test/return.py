def get_price(is_vip=False):
    if is_vip == True:
        return 10000
    else:
        return 15000

price1 = get_price()
print(price1)
price2 = get_price(True)
print(price2)


#print(f'단골 손님은{price}원 입니다.')


def cal(a,b):
    return a+b, a-b, a*b, a/b
'''
print(cal(1,2))
result = cal(1,2)
s, munus, muktiple, dici
'''

def visit(today, *customers):
    print(today)
    for customers in customers:
        print(customers)
visit('오늘','나')
visit('-'*10)
visit('오늘','나','너')
visit('-'*10)
visit('오늘','나','너','우리')
visit('-'*10)

def print_kwargs(**a):
    print(a)

print_kwargs('name','foo',age=3, height=150)