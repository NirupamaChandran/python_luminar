# write only write string
path="C:\\Users\\HP\\Desktop\\Pythonlmnr\\fileio\\colors.txt"
f=open(path,"w")
colors=["red","green","blue"]
for c in colors:
    f.write(c+"\n")