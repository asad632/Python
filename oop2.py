# class Person:
#     count_instance = 0   # its called class attributes or class variable
#     def __init__(self, name, class_name, age):
#         Person.count_instance += 1
#         self.name = name
#         self.class_name = class_name
#         self.age = age
#
#     @classmethod
#     def count_instances(cls):
#         return f"you have created {cls.count_instance} instances of  {cls.__name__} class"
#
#     @classmethod
#     def from_sting(cls,string):
#         first,last,age = string.split(',')
#         return cls(first,last,age)
#
#     @staticmethod
#     def hello():
#         print('hello you called static method')
#
# p4 = Person.from_sting('asad,ullah,31')
#
# Person.hello()
#
#
# p1 = Person('alina', '2nd', 7)
# p2 = Person('omar', '1st', 5)
# p3 = Person('hasnain', 'kg', 3)
#
# print(Person.count_instance)
#
# print(Person.count_instances())