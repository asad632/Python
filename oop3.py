# # encapsulation
# # Abstract
# # some special naming convention
# # name mangling
# 
# class Phone:
#     def __init__(self,mobile, model, price):
#         self.mobile =mobile
#         self.model = model
#         self.price = price
#         self.complet_specification = (f'{self.mobile } {self.model } price is {self.price }')
# 
#     def phone_num(self, phone_number):
#         print(f'calling to {phone_number}')
# 
# phon1 = Phone('nokia', '1100', '1000')
# 
# print(phon1.mobile)
# print(phon1.model)
# print(phon1.price)
# 
# print(phon1.complet_specification)