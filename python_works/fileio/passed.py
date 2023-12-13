std_path="C:\\Users\\HP\\Desktop\\Pythonlmnr\\fileio\\students.txt"
fstd=open(std_path,"r")

fail_path="C:\\Users\\HP\\Desktop\\Pythonlmnr\\fileio\\failed.txt"
ffail=open(fail_path,"r")

# std_set=set()
# for line in fstd:
#     std=line.rstrip("\n")
#     std_set.add(std)
std_set={line.rstrip("\n") for line in fstd}   # set comprehension
# print(std_set)

# failed_set=set()
# for line in ffail:
#     fail=line.rstrip("\n")
#     failed_set.add(fail)
failed_set={line.rstrip("\n") for line in ffail}
# print(failed_set)

# passed=std_set.difference(failed_set)
passed=std_set-failed_set
print(passed)