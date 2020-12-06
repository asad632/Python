# # multlivel inheritance
#
# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def full_name(self):
#         return f' {self.brand} {self.model}  {self.price}'
#
#     def make_call(self, number):
#         return f'calling to {number} ...'
#
#
#
# class SmartPhone(Phone):
#     def __init__(self, brand, model, price, ram, memory):
#         # now we can do it in two way one is ---> Phone.__init__(self, ...) and second is --> super().__init__(self,..)
#         # Phone.__init__(self, brand, model, price)   #uncommon way
#
#         super().__init__(brand, model, price)
#         self.ram = ram
#         self.memory = memory
#
#     def full_name(self):
#         return f' {self.brand} {self.model} {self.price} {self.ram} {self.memory} '
#
# class FlagshipPhone(SmartPhone):
#     def __init__(self, brand, model, price, ram, memory, camera):
#         super().__init__(brand, model, price, ram, memory)
#         self.camera = camera
#
#     def full_name(self):
#         return f' {self.brand} {self.model} {self.price} {self.ram} {self.memory} {self.camera} '
#
#     # __repr__ or __str__
#     def __repr__(self):
#         return f'this is \'{self.brand}\'  price is \'{self.price}\' pkr'
#
#     def __str__(self):
#         return f'FlagshipPhone(this is \'{self.brand}\' model is \'{self.model}\' rame is \'{self.ram}\' )'
#
#     def __add__(self, other):
#         return self.price + other.price
#
#     def __sub__(self, other):
#         return self.price - other.price
#
# p1= Phone('Nokia', '3310', 2000 )
#
# sp= SmartPhone('samsung', 'S8', 40000, '4gb', '32gb')
#
# fp= FlagshipPhone('iphone', 'i10', 80000, '6GB', '128GB', '40 mp')
#
#
# my_phone = FlagshipPhone('iphone', 'i10', 80000, '6GB', '128GB', '40 mp')
# my_phone2=SmartPhone('samsung', 'S8', 40000, '4gb', '32gb')
# print(my_phone.__repr__())
# print(str(my_phone))
# print(repr(my_phone))
#
# print(my_phone - my_phone2)
# print(my_phone + my_phone2)
#
#
#
#
#
# # print(p1.full_name())
# #
# # print(sp.full_name())
# #
# # print(fp.full_name())
# #
# # print(help(fp))
# # print(p1.make_call(+923489830308))
#
#
# #           ____ dunder , special magic methods____
# #                     __dict__  / __name__ / __doc__ /