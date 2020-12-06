#
# a=['abc', 'efg', 'xyz']
#
# def reverse_list(l):
#     new_list=[]
#     for i in l:
#         new_list.append(i[::-1])
#     return new_list
# print(reverse_list(a))
#
# # ---------------define function  comprehension list method
#
# def reverse_list1(l):
#     return [i[::-1] for i in l]
# print(reverse_list1(a))
#
# # -------------- sample--------------
#
# b=[i[::-1] for i in a]
# print(b)