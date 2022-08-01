
# Write your code above 👆

with open("./file1.txt") as file1:
    file1_number_list = file1.readlines()

with open("./file2.txt") as file2:
    file2_number_list = file2.readlines()

result = [int(number) for number in file1_number_list if number in file2_number_list]

print(result)