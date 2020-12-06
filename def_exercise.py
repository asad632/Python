# # # # make function to find greater number in two numbers
# # def greater(a,b):
# #     if a > b :
# #         return a
# #     else:
# #         return b
# # #
# # num1 = int(input("enter first number ; "))
# # num2 = int(input("enter second number ; "))
# # bigger = greater(num1,num2)
# # print(f"{bigger} is greater ")
#
#
#
#
# # n1= int(input("enter number a ; "))
# # n2= int(input("enter number b ; "))
# # n3 = int(input("enter number c ; "))
# # bigger = greater(n1,n2,n3)
#
# # we can creat function inside function
# def greater(a,b):
#     if a > b :
#         return a
#     else:
#         return b
# #
# num1 = int(input("enter first number ; "))
# num2 = int(input("enter second number ; "))
# bigger = greater(num1,num2)
#
# def greatest(a,b,c):
#     bigger=greater(a,b)
#     return greater(bigger,c)
#
# print(greater(bigger,1011))
#
#    # or
#
# def greatest_new(a,b,c):
#     return greater(greater(a,b),c)
# print(greater(bigger,9911))