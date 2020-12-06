# from functools import wraps
#
# def only_int_allow(function):
#     wraps(function)
#     def wrapper(*args, **kwargs):
#         if all([type(arg) == int for arg in args]):
#             return function(*args, **kwargs)
#         print('invalid input')
#         # adattype = []
#         # for i in args:
#         #     adattype.append(type(i)==int)
#         #     if all(adattype):
#         #         return function(*args, **kwargs)
#         #     return 'invalid '
#     return wrapper
#
# @only_int_allow
# def add(*args):
#     total =0
#     for i in args:
#         total += i
#     return total
#
# print(add(6,2,3,4))
# print(add(6,2,3,4, 'ff'))