# # use of fromkeys
# # d = {'name': 'unknown', 'age': 'unknown'} how we creat the same values by use fromkeys
# d = dict.fromkeys({'name', 'age'}, 'unknown')
# print(d)         #  d = {'name': 'unknown', 'age': 'unknown'}
# # we can write in ((... ),'..)
# e = dict.fromkeys(('name', 'age', 'hight'), 'unknown')
# print(e)   # or we can write in str    ("..." , "...")
# f =('abc', 'unknown')    # a = unknow , b= unk,...   , c = unk...,
# print(f)
# # we can use range method to enter numbers as well
# g = dict.fromkeys(range(1,11), 'unknown')   #we can enter anything in value i enter "unknown"
# print(g)   # {1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown', 6: 'unknown', 7: 'unknown', 8: 'unknown', 9: 'unknown', 10: 'unknown'}
# # we can enter in list style
# h = dict.fromkeys(['name', 'age'], ['unknown', 'unknown'])
# print(h)   #{'name': ['unknown', 'unknown'], 'age': ['unknown', 'unknown']}
#
#  #                 --------- get methiod ------------
#  # when we enter items and the item not  in dictionary it wiil show error   so we using get method it will give output None
# ij = {'name': 'asad', 'age': 31, 'hight': 5 }
#
# if 'names' in ij:
#     print('yes there is name')
# else:
#     print(' no there is not ')
#     # we can use get if there is showing error
# if ij.get('name'):
#     print('yes')
# else:
#     print('no')
#
# print(ij.get('name')) #  yes
# print(ij.get('mobile'))   # None
# print(ij.get('carss', 'not found'))   #if carss isnot in ij dictionary we pass argument not found
#
# # ----------------------copy method in dictionary--------------
# #  copy mehtod use to copy one to two are more dictionary we can use it defferantly
# jk = {'name': 'asad', 'age': 31, 'hight': 5 }
# jk_1 = jk.copy()
# print(jk_1)
# jk_2= jk_1.copy()
# print(jk_2)
# jk_2['cars']=['toyta', 'suzuki']
# print(jk_2)
