# # how to creat owen function(iteretor) to take function in argument
# def myfunc(l):
#     return l**3
# def my_map(func,l):
#     newlist=[]
#     for i in l:
#         newlist.append(func(i))
#     return newlist
#
# list1 =[2,3,4,5]
# print(my_map(myfunc, list1))
#
# # or
# def my_map2(func, l):
#     return [func(i) for i in l]
#
# print(my_map2( lambda i:i**3, list1))