#   Class
#   객체 지향 프로그래밍

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'My name is {self.name}, and my age is {self.age}.')

    def get_aged(self, age = 1):
        self.age += age

    def get_id_card(self):
        return f'Person([{self.name}]:[{self.age}])'

person = Person('Charlotte', 20)
print(person.name)
print(person.age)
person.introduce()

person.get_aged()
person.introduce()

person.get_aged(10)
person.introduce()

id_card = person.get_id_card()
print(id_card)