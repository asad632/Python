# use_info = { 'name' : 'asad', 'last name' : 'khan', 'age' : 31, 'fav_car' : 'rangrover', }
# # add in dictionary ,----->  use_info['song']=['tapy', 'ghazal']
# use_info['song']=['tapy', 'ghazal']
# print(use_info)
# # pop method use to remove but it will return, we should pass argument in pop('argument') method and no argument in popitem()
# popped_item = use_info.pop('fav_car')
# print(popped_item)
# print(use_info)
# print(type(popped_item))
# # popitem method use to remove the last key value and return (tuple), there is not using (argument) in popitem
# pop_item = use_info.popitem()
# print(pop_item)
# print(type(pop_item))
# print(use_info)
# pop_item = use_info.popitem()
# print(pop_item)
# # update() method use to add dictionaries if there is two same keys they will update new one
# more_info = {'name' : 'asad ullah', 'contry' : 'Pakistan'}
# use_info.update(more_info)     #use_info name=asad and  more_info name= asad ullah ,here is updated
# print(use_info)
# print(more_info)
#  to make