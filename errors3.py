# # # exception
# #
# # while True:
# #     try:
# #         age = int(input('enter your age : '))
# #     except ValueError:
# #         print('maybe you entered in string ')
# #     except:
# #         print('invalide error !! ')
# #     else:
# #         print(f'your age is {age} years')
# #         break
# #     finally:
# #         print(' finally ')
# #
# # if age < 18 :
# #     print('you can\'t play this game ')
# # else:
# #     print('you can play this game ')
#
#
# def divide(a,b):
#
#     try:
#         return a / b
#
#     except ZeroDivisionError as err:
#             print(err)
#     except TypeError as err:
#             print(err)
#
#     else:
#         print('unexpeted error ')
#
#
# print(divide(20,3))
