# # nested list comprehension (list inside list)
#
# nestedlist=[]
# for i in range(3):
#     nestedlist.append([1,2,3])
# print(nestedlist)
#
# # now by list comprehension
# new_list=[[i for i in range(1,4)] for j in range(3)]
# print(new_list)