string = 'Python'
reverse_string = ''

for c in string:
    reverse_string = c + reverse_string

print(f'string:{string}')
print(f'reverse:{reverse_string}')



str = 'apple'
new_str = ''

for a in str:
    new_str = a + new_str

print(f'{str}')
print(f'{new_str}')




def reverse_string(str):
    return str[::-1]

str = 'Python'
print(reverse_string(str))
