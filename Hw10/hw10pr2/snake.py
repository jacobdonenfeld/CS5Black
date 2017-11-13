def test():
    while True:
        x = input("pinnumb?")
        x = int(x)
        if (x//12 % 2) != 0:
            # print("row")
            row = x // 12 +1
            # print(row)
            print(12*row-(x%12)-1)
        else:
            print(x)

print(test())