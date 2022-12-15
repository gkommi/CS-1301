
def combine_two(list1, list2):
    return_list = []
    for i in range(len(list1)):
        return_list.append(list1[i])
        return_list.append(list2[i])
        continue
    return return_list

"""
print(combine_two( [ "cat", "dog", "bear"], [2, 3, 4] ))  # will print out ["cat", 2, "dog", 3, "bear", 4]

print(combine_two( [ "cat"], [2] ))  # will print out ["cat", 2]

print(combine_two( [ ], [ ] ))  # will print out [ ]
"""
