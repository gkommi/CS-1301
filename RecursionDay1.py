def rec1(num):
    if num > 0:
        print(num)
        rec1(num - 2)
        print(num)
rec1(6)
