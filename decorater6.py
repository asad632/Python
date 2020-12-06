# from functools import wraps
#
# def only_data_type(all_data):
#     def decorater(function):
#         @wraps(function)
#         def wrapper(*args, **kwargs):
#            if all([type(i)== all_data for i in args]):
#                return function(*args, **kwargs)
#            print('invlide input')
#         return wrapper
#     return decorater
#
# @only_data_type(str)    #(str) is most important here
# def addstring(*args):
#     string= ''
#     for i in args:
#         string += i
#     return string
#
# print(addstring('asad ', 'ullah ', 'khan'))