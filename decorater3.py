# from functools import wraps
#
# def decorater_func(function):
#     @wraps(function)
#     def wrapper_func(*args, **kwargs):
#         print(f' you are calling {function.__name__} functions')
#         print(f'{function.__doc__ }')
#         return function(*args, **kwargs)
#     return wrapper_func
# @decorater_func
# def func(a,b):
#     """this function take 2 arguments"""
#     return a + b
# print(func(4,5))