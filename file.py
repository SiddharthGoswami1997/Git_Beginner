# class Mymeta(type):
#     def __new__(cls, name, bases, dct):
#         print("Hiiiiii")
#         return super().__new__(cls, name, bases, dct)
# class Student(metaclass=Mymeta):
#     __slots__ = ["name", "age", "id"]
#     def __init__(self, name, age, id):
#         self.name = name
#         self.age = age
#         self.id = id
#
# def add(a: int, b: int) -> int:
#     return a+b
#
# print(add(4,5))
#
#
# ob = Student

# class Dog:
#     def speak(self):
#         return "Woof!"
#
# class Cat:
#     def speak(self):
#         return "Meow!"
#
# class Duck:
#     def speak(self):
#         return "Quack!"
#
# def animal_sound(animal):
#     print(animal.speak())  # Duck typing: we care if it has 'speak()'
#
# dog = Dog()
# cat = Cat()
# duck = Duck()
#
# animal_sound(dog)   # Woof!
# animal_sound(cat)   # Meow!
# animal_sound(duck)  # Quack!
#
# def new_speak(self):
#     return "this is new speak"
#
# Dog.speak = new_speak
# print(dog.speak())

# a = 256
# b = 256
# print(a is b)  # True – same object!
#
# a = 257
# b = 257
# print(a is b)  # Might be False – new objects

# file = open("fil1.txt", "r")
# print(file.readlines())

# file = open("fil1.txt", "a")
# file.write("helllllloooooooooooo")
# print(file.tell())
# file.close()
#
# import json
#
# data = {'name': 'Bob', 'age': 30}
#
# # Serialize
# with open('data.json', 'w') as f:
#     json.dump(data, f)
#
# # Deserialize
# with open('data.json', 'r') as f:
#     loaded_data = json.load(f)
#
# print(loaded_data)


# s = "Siddhhdgdjttttthhartrrrrrrrrrrrrrrrrrrrrrrrh"
# dict = {}
# for i in s:
#     if i in dict.keys():
#         dict[i] = dict[i] + 1
#     else:
#         dict[i] = 1
#
# temp = 0
# for i, j in dict.items():
#     if j > temp:
#         key = i
#         temp = j
#
# print(key)


# class MyClass:
#     def __init__(self):
#         self._value = "Protected"
#
# obj = MyClass()
# print(obj._value)  # ⚠️ Accessible but discouraged
#
#
# class MyClass:
#     def __init__(self):
#         self.__secret = "Private"
#
# obj = MyClass()
# # print(obj.__secret)       ❌ AttributeError
# print(obj._MyClass__secret)  # ✅ Accessible via name mangling


# class A:
#     @staticmethod
#     def greet():
#         print("Hello from A")
#
# class B:
#     def call_static(self):
#         A.greet()
#         print("hiihi")  # Accessing static method of class A
#
# A.greet()
#
# B().call_static()