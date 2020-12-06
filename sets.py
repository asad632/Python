# # set data type is unorder store collection of uniqe items
# #  sets = {1,2,3,4,5,,'name','age'} we can store int float str and we cant store list, dictionaries
# s = {1,2,3,4,5}
# # if we have list so we can convert it to set
# l = [1,2,3,2,3,4,5,5,5,6,] #we can remove duplicat from list by set
# s1 = list(set(l))
# print(s1)   #  [1, 2, 3, 4, 5, 6, 7]
# # we can add to set by add method
# s.add(6)
# s.add(7)
# s.add(5)  # 5 already in s set so it will not add
# s.add('asad')
# print(s)
# # now how to remove from sets by using remove and discard method
# s.remove('asad')
# s.remove(7)
# # if the element's not in set output'll be key error to aovid the arroe we using discard
# s.discard(9) #9 not in s
# s.discard(5)
# print(s)
