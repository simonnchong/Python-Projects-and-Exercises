# general code
# `new_list` = [`new_item` for `item` in `list` if `condition/test`]

# python sequences (has a specific order):
# list
# string
# range
# tuple


#* -------------------------------------- list ------------------------------------
# write a single line code to save a list into another list

number_list = [1, 2, 3]

# using for loop to iterate
new_list = []
for number in number_list:
    add_1 = number + 1
    new_list.append(add_1)
    
    
# using list comprehension to iterate
new_list2 = [number + 1 for number in number_list]

print(new_list)
print(new_list2)


#? list comprehension with condition/validation
name_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_name = [name for name in name_list if len(name) <= 4]
upper_case_name = [name.upper() for name in name_list if len(name) > 5]





#* -------------------------------------- string ------------------------------------
# this can be used in string as well

name = "Simon"
letter_list = [letter for letter in name]

print(letter_list)



#* -------------------------------------- range ------------------------------------
# this can be used in range as well

number_range = [number * 2 for number in range(1,5)]