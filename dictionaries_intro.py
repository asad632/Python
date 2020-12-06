# # list are not enough to store data we use dictionaries
# # we can store anything in ditionaries
# # we can creat dictionaries in two way
# # user1 = { 'name' : 'asad', 'age' : 31.6  }
# # # print(user1)
# # user2 = dict(name = 'asad', age = 31.7)
# # print(user2)
# # # no index in dictionaries, we can find only print(user2['age'])
# # print(user1['age'])
# # we can store anthing in dictionaries,,   list, string, dictionaries ,,
# users = {
#     "user3" : { 'name' : 'Asad', 'age' : 31, 'belong' : 'Pakistan'  },
#     "user5" :    { 'name' : 'khan', 'age' : 37, 'belong' : 'Pakistan'  },
# }
#
# print(users)
# # how to enter data to empty dictionaries
# # user6 = {}
# # user6['name']='asad'
# # print(user6)
#
#                # -----------------------------------------------------
#
# user_info = { 'name' : 'Asad', 'age' : 31, 'contry' : 'Pakistan'  }
#
# # check if key exist in dictionary or not
# if 'name' in user_info:
#     print('yes')
# else:
#     print('no')
#
# # check if value exist in dictionary or not
#
# if 'Asad' in user_info.values():
#     print('yes')
# else:
#     print('no')
# # loops in dictionary  for loop ,,,,
# for i in user_info:
#     print(i)  # output only keys
#
# for i in user_info.values():       # for values
#     print(i)    #  OR
#     # print(user_info[i])
#
# # values method (dict value)   only value but in one line
# user_value = user_info.values()
# print(user_value)
# print(type(user_value))
#
# # keys method (dict keys)   only keys but in one line
# user_key = user_info.keys()
# print(user_key)
# print(type(user_key))
#
# # items [method dict items]  output will keys and values    ,,dict_items([('name', 'Asad'), ('age', 31), ('contry', 'Pakistan')])
# user_items = user_info.items()
# print(user_items)
# print(type(user_items))
#
# # for loop with items method most important
# for key, value in user_info.items():
#     print(f'key is {key} and value is {value}')
#     # or  i j
# for i, j in user_info.items():
#     print(f' key is {i} and value is {j}')
