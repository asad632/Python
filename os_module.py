import os

# oprating system get curant work dirictry(os.getcwd)
# print(os.getcwd())
# make dirictry'folder'(os.mkdir)
# os.mkdir('Asad')
# os.mkdir('Asad')
# print(os.path.exists('Asad'))
# if os.path.exists('Asad'):
#     print('already have folder ')
# else:
#     os.mkdir('Asad')
#
# #### easy way to  crrat a file
# open('file.txt', 'a').close()
# open('file.txt', 'a').close() #no second creat no error
# os.mkdir("/home/asad/Desktop/Aasad")
# os.chdir("/home/asad/Desktop/Aasad")
# # print(os.getcwd())
# os.chdir("/home/asad/Desktop/Python course")
# print(os.getcwd())
# print(os.listdir("/home/asad/Desktop"))
# print(os.listdir())
#
### only folder will show
# for i in os.listdir():
#     path = os.path.join(os.getcwd())
#     print(path)

 # ###very important
# #
# fileiter = os.walk("/home/asad/Desktop")
# for current_path, folder_names, file_names in fileiter:
#     print(f'curent path {current_path}')
#     print(f'folder name {folder_names}')
#     print(f'file names {file_names}')

#### creat folder and inside one more folder in folder
# os.makedirs('new/newinside')

import shutil

# # shutil module delete full folder permenently
# shutil.rmtree('asad')

## ----->>> copy folder --->>  shutil.copytree('namefolder', 'copyto/namefolder_again')
# shutil.copytree('asad', 'Desktop/asad') #can rename  aswell

###for file copy----->>>  shutil.copy('asad.py', 'Desktop/asad.py')
# shutil.copy('asad.txt', 'Desktop/asad.txt')

######   move file or folder  to other folders---->>>>  shutil.move('aad.txt', 'Desktop/asadtxt')
# shutil.move('aad.txt', 'Desktop/asadtxt')