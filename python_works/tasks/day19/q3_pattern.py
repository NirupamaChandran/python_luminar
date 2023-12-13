for row in range(1,6):
    for space in range(row,5):
        print(" ",end="")
    for col in range(1,row+1):
        if col in [1,row]:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for row in range(5,1,-1):
    for space in range(6,row,-1):
        print(" ",end="")
    for col in range(1,row):
        if col in [1,row-1]:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()