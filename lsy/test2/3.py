class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return(f'greet(self):' '{name}님이 {age}살입니다')
    

person1 = person("홍길동", 30)
print(person1.greet())

person2 = person("전우치", 20)
print(person2.greet())
