import_data = input('입력하세요:')
#data = '456793'
numbers = list(map(int, import_data))
print(numbers)
result = []
for i, num in enumerate(numbers):
    result.append(str(num))
    if i<len(numbers)-1:
        is_odd = num%2==1
        is_next_odd = numbers[i+1]%2==1
        if is_odd and is_next_odd:
            result.append('-')
        elif not is_odd and not is_next_odd:
            result.append('*')
print(''.join(result))