n = input('숫자를 입력 : ')
n = int(n)

pib = [0,1]
result = 0
if n==1:
    print(pib[0])
elif n >1:
    for i in range(1,n-1):
        pib.append(pib[i-1]+pip[i])
print(pib)