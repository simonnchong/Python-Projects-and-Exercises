from operator import index


def lastIndex(s):
    if not "1" in s:
        return -1
    current_index = 0
    index_of_last_1 = 0
    for digit in s:
        if digit == "1":
            index_of_last_1 = current_index
        current_index += 1 #1
    return index_of_last_1

print(lastIndex("00000000001000"))