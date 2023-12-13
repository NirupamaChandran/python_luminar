set1={"red","green","blue"}
set1.add("yellow")   # add() to add an element in to set
print(set1)
set2={"yellow","black","red","pink"}
print(set2)

inter_set=set1.intersection(set2)
print(inter_set)

uninon_set=set1.union(set2)
print(uninon_set)

diff_set=set1.difference(set2)
print(diff_set)

# set1.pop()  remove first element from their order
# print(set1)

# set1.remove("red")  remove return error if object is not present but discard didn't terminate the program.
# print(set1)

set1.discard("red")
print(set1)

st1={10,20,30}
st2={100,200,300}
st1.update(st2)
print(st1)