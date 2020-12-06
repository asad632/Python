# # star args make our def function flexable
# def num1(a,b):    # we can pass only two parameter in this function
#     return a+b
# print(num1(1,2))
# # but *args is accepting  unlimited arameter
#
# def num2(*args):
#     total=0
#     for i in args:
#         total +=i
#     return total
# print(num2(1,2,3,4,5,6,7,8,9))
# print(type(num2))
#
# # multifly in star* ags
# def num3(*args):
#     total=1
#     for i in args:
#         total *=i
#     return total
# print(num3(2,3,4))
# print(num3(1500,43))
#
# def multifly_n(num1, *args):   #*args with num perameter now the first argument be the part of num1 then the rest will be args
#     multifly =1  #  for the revuse of multipal numbers
#     print(num1)
#     for i in args:
#         multifly *= i
#     return multifly
# print(multifly_n(5,4,4))
#
# print(multifly_n(5,5))
#
# def multy_m(*args):
#     total = 1
#     for i in args:
#         total *= i
#     return total
# print(multy_m(3,4))
#  # if we have numbers=[1,2,3,4,5] or (1,2,3,4,5) we shoud use * befor numbers---> multifly_n(*numbers)
# numbers = (3,4,5)
# numbers2 = [4,4,4]
# print(multy_m(*numbers))  # *numbers
# print(multy_m(*numbers2))
