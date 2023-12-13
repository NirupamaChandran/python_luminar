order1={"cb","tika","fishfry","friedrice","vb","gheerost"}
order2={"cb","friedrice","nan","upma","vegmeals","idly"}

# uninon_ord=order1.union(order2)
# inter_ord=order1.intersection(order2)
# diff_ord=uninon_ord.difference(inter_ord)
# print(diff_ord)                               set1 U set2 - set1 ^ set2  is called Symmetric difference

diff_ord=order1.symmetric_difference(order2)
print(diff_ord)