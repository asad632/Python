# from functools import wraps
#
# def decorater_func(any_function):
#     @wraps(any_function)
#     def wraper_func(*args, **kwargs):
#         """this is decorater function"""
#         print("this is decorater")
#         return any_function()
#     return wraper_func
#
# def add(a):
#     print(f" this is {a}")
#     """this is add func"""
#
#
# print(add(5))
# print(add.__doc__)