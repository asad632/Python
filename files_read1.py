# # # how to read one file and the same data write in other file,
# # with open('file3.txt', 'r') as rf:
# #     with open('file2.txt', 'w') as wf:
# #         wf.write(rf.read())
# #
# with open('file4.txt', 'r') as rf:
#     with open('file3.txt', 'a') as wr:
#         for line in rf.readlines():
#             name,salary = line.split(',')
#             wr.write(f'{name}\'s salary is {salary}')
#
