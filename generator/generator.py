import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()

def generated_person():
    yield Person(
        full_name=faker_ru.first_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        age=random.randint(18, 80),
        salary= random.randint(20000, 200000),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )

def generated_file():
    path = rf'C:\PythonProject\PythonSelenium\filetest{random.randint(1,100)}.txt'
    file = open(path, 'w+')
    file.write(f'Test text {random.randint(1,1000)}')
    file.close()
    return file.name, path