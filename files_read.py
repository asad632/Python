# use terminal for this topic

# with open('file.txt') as f:
#     data = f.read()
#     print(data)
#
#
# print(f.closed)

# mode of file.txt  "-------->>.. 'r', 'w', 'a', 'r+', .......<-------"

# with open('file.txt', 'r')  to read the file
# with open('file.txt', 'w')   --> to write the file but this mode will delete the data if there is,.

# with open('file.txt', 'a') -----> to append(add) the data.if we dont have file wich we enter a mode will creat that file
# with open('file.txt', 'r+') ----> to

# with open('file.txt', 'w') as ge:
#     ge.write('hello all, hope you will be fine')

# with open('file.txt', 'a') as hj:
#     hj.write('\nplease do it \n thank you,\n')
#     hj.write('see you\n')
#
# with open('file2.txt', 'a') as hj:
#     hj.write('\nplease do it \n thank you,\n')
#     hj.write('see you\n')
#
# # we can creat file in terminal with hello txt
# ┌─[asad@parrot]─[~/Desktop/Python course]
# └──╼ $echo =e "hello there" >> file3.txt
#
# with open('file3.txt', 'r+') as hj:
#     hj.write('\nplease do it \n thank you,\n')
#     hj.write('see you\n')

#
# with open('file3.txt', 'r+') as hj:
#     hj.seek(len(hj.read()))
#     hj.write('have a great day\n')
#
#
