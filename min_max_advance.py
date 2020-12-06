# # max and min advnce uses
# names = ['asad', 'ullah', 'kpk']
# # now find the min and max lenght of name
# def myfunc(name_):
#     return len(name_)
# print(max(names, key = myfunc))
# print(min(names, key=myfunc))
#
# # now lambda uses to define function in one line
#
# print(max(names, key=lambda i :len(i)))
# print(min(names, key= lambda i:len(i)))
#
# student1 = [
#     {'name': 'asad', 'score': 90, 'age': 31},
#     {'name': 'waqas', 'score': 91, 'age': 18},
#     {'name': 'omar', 'score': 80, 'age': 6}
# ]
#
# print(min(student1, key = lambda item : item.get('score')))
# print(max(student1, key = lambda items : items.get('score'))['name']) #only name will outout
# print(min(student1, key = lambda item : item.get('age')))
# print(max(student1, key = lambda items : items.get('age'))['name'])
#

#
# students = {
#     'asad' : {'score': 90, 'age':31},
#     'waqas' :{'score':91, 'age':18},
#     'omar' : { 'score':80, 'age':6}
# }
# # print(min('score' in user))
# print(min(students, key = lambda item: students[item]['score']))
# print(max(students, key=lambda item:students[item]['score']))
#
# print(min(students, key = lambda item: students[item]['age']))
# print(max(students, key=lambda item:students[item]['age']))