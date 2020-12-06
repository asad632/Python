# class Laptop:
#     descounta = 20
#     def __init__(self,Brand_name, Model_name, Price):
#         self.Brand_name = Brand_name
#         self.Model_name = Model_name
#         self.Price = Price
#     def descount_15(self):     #this is class instance method.
#         print( f'orignal price is --> {self.Price} and 15 % discount is --> {self.Price*15/100}')
#         return self.Price - self.Price*15/100
#
#     def put_discount(self,dis):   # this is instance method
#         off_price = (dis/100)*self.Price
#         return self.Price - off_price
#
# # fix descount or class descount
#
#     def class_descoun(self):
#         off_price = (Laptop.descounta/100)*self.Price
#         return self.Price - off_price
#
# # self discount we can manage it down
#
#     def self_discount(self):
#         off_price = (self.descounta/100)*self.Price
#         return self.Price - off_price
#
#
# # if discount finished then we can ---> Laptop.descounta=0
# Laptop.descounta = 0
#
#
# l1 = Laptop('Toshiba', 'Setilite', 15000)
# l2 = Laptop('HP', 'P5', 90000)
#
# l1.descounta=20
# print(l1.__dict__)
# print(l1.self_discount())
#
# print(l1.Brand_name)
# print(l1.Model_name)
# print(l1.Price)
#
# print(l1.descount_15())
# print(l2.put_discount(20))
# print(l1.class_descoun())