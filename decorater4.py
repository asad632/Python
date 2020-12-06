# # exercise
# from functools import wraps
# import time
#
# def decorate_(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"you are calling {func}")
#         t1 = time.time()
#         deco = func(*args, **kwargs)
#         t2= time.time()
#         tootal_time = t2-t1
#         print(tootal_time)
#         return deco
#     return wrapper
#
# @decorate_
# def add(a):
#     return [i**4 for i in range(1,a+1)]
#
# add(100)
