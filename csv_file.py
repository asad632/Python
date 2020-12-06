# # csv = cuma serated value
# # name,email,phone
# # asad,asad@gmail.com,03456827
# # now i im importing (reader and dictwriter) function from csv module
#
# # from csv import reader
# # with open('file.csv', 'r') as f:
# #     csvreader = reader(f)
# #     # print(type(csvreader))
# #     for line in csvreader:
# #         print(line)
#
# # now usin dictreader from csv import
#
# # from csv import DictReader
# # with open('file.csv', 'r') as f:
# #     csvreader = DictReader(f)
# #     # print(type(csvreader))
# #     for line in csvreader:
# #         print(line)
#
# #
# # from csv import writer
# # with open('file.csv', 'w') as f:
# #     csv_writer = writer(f)
# #     csv_writer.writerow(['name','contry'])
# #     csv_writer.writerow(['Asad','Pakistan'])
# #     csv_writer.writerow(['omar','kotigram'])
# #     # print(csv_writer)
# #     csv_writer.writerows([['name','contry'],['omar', 'pak'],['hasan','pak']])
#
#
# # dictwriter method can creat by self  and write
#
# from csv import DictWriter
# with open('file1.csv', 'w') as f:
#     csv_write = DictWriter(f, fieldnames=['name','age'])
#     csv_write.writeheader()
#     # csv_write.writerow({
#     #     'name':'Asad',
#     #     'age':31
#     # })
#     #
#     # csv_write.writerow({
#     #     'name':'omar',
#     #     'age':5
#     #
#     # })
#     #
#     # csv_write.writerow({
#     #     'name':'hasanain',
#     #     'age':3
#     # })
#     # csv_write.writerow({
#     #     'name':'noor'
#     #     ,'age':1
#     # })
#
#     # csv_write.writerows([
#     #     {'name':'hasanain','age':3},
#     #     {'name':'omar','age':5},
#     #     {'name':'noor','age':1},
#     #     {'name':'hasanain','age':4}
#     # ])
#
# # from read to write new file
#
# from csv import DictReader,DictWriter
#
# with open('file.csv', 'r') as rf:
#     with open('file2.csv', 'w')as wf:
#         csv_read = DictReader(rf)
#         csv_writer = DictWriter(wf, fieldnames=['name','contry'])
#         csv_writer.writeheader()
#
#         for row in csv_read:
#             name,contry= row['name'], row['contry']
#             csv_writer.writerow({
#                 'name':name,
#                 'contry':contry
#             })
