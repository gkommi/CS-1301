def count_str(list1):
    count = 0
    if len(list1) == 0:
        return 0
    else:
        if type(list1[0]) == str:
            count += 1
            return count + count_str(list1[1:])
        else:
            return count + count_str(list1[1:])

#print(count_str(["a",1,2,"b",2.3]))  # should print 2
#print(count_str([1,2,3])) # should print 0
