text = 'hello world, this is a python example.'

words = text.split()
print(words)

capitalized_words = [word.capitalize() for word in words ]
print(capitalized_words)
result = ' '.join(capitalized_words)

print(result)




















