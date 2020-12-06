# # any function and all function/
# numbers = [2,4,6,8,10]
# odd_numbers= [1,3,5,7,9]
# even =[]
# for i in numbers:
#     even.append(i%2==0)
# print(even)
#
# even1 = [ i%2==0 for i in numbers]
# print(even1)
# odd = [i%2==0 for i in odd_numbers]
# print(odd)
# # now use all and any functions
# print(all(even1))
# print(all(odd))
# print(any(even1))
# print(any(odd))
# # if in all fun one in false will show false but any is opposite
#
# def sum_(*args):
#     total = 0
#     if all([(type(i)==int or type(i)==float) for i in args]):
#         total += i
#         return total
#     else:
#         return 'wrong input only int or float acceptable '
# print(sum_(1,2,3,4))
# print(sum_(1,2, 'a'))