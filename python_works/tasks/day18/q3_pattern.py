asci=65
for row in range(1,6):
    for sp in range(1,6-row):
        print(end=" ")
    for col in range(1,row+1):
        print(chr(asci),end=" ")
        asci+=1
    print()
    asci=65