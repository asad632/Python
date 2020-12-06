# # NotImplementedError
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def sound(self):
#         raise NotImplementedError('you have to define this method in subclasses')
#
# class Dog(Animal):
#     def __init__(self, name, bread ):
#         super().__init__(name)
#         self.bread = bread
#
#     def sound(self):
#         return 'Bhao Bhao '
#
# class Cat(Animal):
#     def __init__(self, name, bread):
#         super().__init__(name)
#         self.bread = bread
#
#     def sound(self):
#         return 'Mhao Mhao Mhaoooo'
#
# cat1 = Cat('Mono', 'meo meo ')
# print(cat1.sound())
