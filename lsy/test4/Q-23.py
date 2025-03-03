import random
random_newnums = [random.randint(1,45) for _ in range(6)]
print( random_newnums)




result = []
while len(result) < 6:
    num = random.randint(1,45)
    if num not in result:
        result.append(num)

print(result)