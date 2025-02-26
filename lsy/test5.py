def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i ==0:
            return False
    return True
    

num = 7
result = is_prime(num)
print(result)


num=2200
result = is_prime(num)
print(result)