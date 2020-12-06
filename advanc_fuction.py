#
# def avregfinder1(args,a):
#     avrege1 = []
#     for i in args,a:
#         avrege1.append(sum(i)/len(i))
#     return avrege1
# print(avregfinder1([1,2,3],[4,5,6]))
#
# def avregfinder(*args):
#     avrege = []
#     for i in args:
#         avrege.append(sum(i)/len(i))
#     return avrege
#
# print(avregfinder([1,2,3],[4,5,6]))
# print(avregfinder([1,2,3], [4,5,6], [7,8,9]))
# # now same output in one line
# average_finder = lambda *args:[sum(i)/len(i) for i in zip(*args) ]
# print(average_finder([1,2,3],[4,5,6]))
# print(avregfinder([1,2,3],[4,5,6], [7,8,9]))
