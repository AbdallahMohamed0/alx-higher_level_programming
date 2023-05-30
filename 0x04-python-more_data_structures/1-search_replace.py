#!/usr/bin/python3
def search_replace(my_list, search, replace):
<<<<<<< HEAD
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
  
=======
    if not my_list:
        return my_list
    return [val if val != search else replace for val in my_list]
>>>>>>> 6ae6adb14391552d15c3c79a727af35fdb2678c7
