# def decorater_func(any_function):
#     def wraper_func(*args, **kwargs):
#         print('this is Decorater function ')
#         return any_function(*args, **kwargs)
#     return wraper_func
#
# @decorater_func
# def func(a):
#     print(f'this is function with {a}')
# func(3)
#
# @decorater_func
# def func1(a,b):
#     return a+b
#
# print(func1(4,6))