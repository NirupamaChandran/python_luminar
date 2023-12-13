for row in range(1,6):
    for col in range(1,row+1):
        print(col,end=" ")
    for col2 in range(col-1,0,-1):
        print(col2,end=" ")
    print()
