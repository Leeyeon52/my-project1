from faker import Faker

fake = Faker('ko-KR')
print(fake.name())
for i in range(10):
    print(fake.job())
