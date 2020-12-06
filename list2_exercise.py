# # define a function it will take input a list and will return reverse of it
# # reverse method
# num = [1, 2, 3, 4, 5]
# def reverse_list(l):
#     l.reverse()      # first reverse l and then return l
#     return l
# print(reverse_list(num))
#
# # slicing method
#
# numb= [1, 2, 3, 4, 7]
# def rev_list(l):
#     return l[::-1]
# print(rev_list(numb))
#
# # pop and append methods to reverse list
# number= [1, 2, 3, 4, 5, 6 ,7]
# def revers_list(l):
#     empty_list=[]
#     for i in range(len(l)):
#         popped_item = l.pop()
#         empty_list.append(popped_item)
#     return empty_list
#
# print(revers_list(number))