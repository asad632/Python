# # find the position of name
# names = ['asad', 'abid', 'atiq']
# position1 = 0
# for i in names:
#     print(f' {position1} ---> {i}')
#     position1 +=1
# # now with enumerate function
# for position1, i in enumerate(names):
#     print(f'  {position1}---> {i}')
#
# def findpos(l, s):
#     for position1, i in enumerate(l):
#         if i==s:
#             return position1
#     return -1
# print(findpos(names,'atiq'))
# print(findpos(names,'asad'))
# print(findpos(names,'ad'))