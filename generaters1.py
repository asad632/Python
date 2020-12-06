# # exercise
# def even(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             yield i
# even(4)
# for i in even(10):
#     print(i)
#
# # how generaters works
# def ab(n):
#     for i in range(1,n+1):
#         yield i
# print(ab(10))
# gen = ab(10)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# print(ab(10)) #<generator object ab at 0x7f1e8c0a1cf0>
#
# for i in ab(10):
#     print(i)
#
#
#
