# # geerate list with range function
# numbers = list(range(1,11))
# print(numbers)
#
# # more about pop method
#
# pop_items = numbers.pop()
# print(numbers)
# print(pop_items)
#
# # index method
# numbers.index(3)
# print(numbers.index(3))                  # 3 on 2nd position
#
# a = [1, 2, 3, 1, 2, 4, 1, 3, 1, 2]
# print(a.index(2))
# # # it will show first 2 position wich is 1, i want to know about next 2 position
# print(a.index(2, 2))    # 2 on 4 postion
# print(a.index(2, 5))     # 2 on 9 position
#
# # pass list to function
# def negative_list(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative
# print(negative_list(numbers))