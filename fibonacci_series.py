# # fibonacci series mean first two number add and make third 0, 1 add both make third 0+1=1, its will 0, 1, 1, 2, 3, 5, 8
# def fibonacci_seq(n):
#     a=0
#     b=1
#     if n == 1 :
#         print(a)
#     elif n == 2 :
#         print(a, b)
#     else:
#         print(a, b, end = " ")        # end " "    its mean go in line until last number (n) example=(12345678899)
#         for i in range(n-2):          # n-2 means first two we explained above a=0 b=1 now c=a+b c=0+1,,,   0 , 1, 1
#             c = a + b                  # c= 0+1
#             a = b                      # 0=1
#             b = c                       # 1=1   or    a=0 b=1 c=0+1     d=b+c   d=1+1
#             print(b, end = " ")
# print(fibonacci_seq(10))
# print(fibonacci_seq(20))