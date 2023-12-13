for row in range(1,8):
    for col in range(1,8):
        print(max(row-3,col-3,8-row-3,8-col-3),end=" ")
    print()