# # if else forloop in comprehension list
# newlist=[]
# def nums(l):
#     for i in l:
#         if i%2==0:
#             newlist.append(i**2)
#         else:
#           newlist.append(-i)
#     return newlist
# number =[1,2,3,4,5,6,7,8,9,10]
# print(nums(number))
# # now in list comprehension
# def nums1(l):
#     return [i**2 if (i%2==0) else -1 for i in l ]
# print(nums1(number))
