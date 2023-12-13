students=[
    {"id":1,"name":"jhon","skills":["c","c++"],"exp":2,"qualification":"mca"},
    {"id":1,"name":"jain","skills":["python","js"],"exp":0,"qualification":"btec"},
    {"id":1,"name":"vijin","skills":["c","java","python"],"exp":4,"qualification":"mca"},
    {"id":1,"name":"tinu","skills":["r","java"],"exp":3,"qualification":"mtech"},
    {"id":1,"name":"roy","skills":["python","css","js"],"exp":0,"qualification":"bca"},
    {"id":1,"name":"vijil","skills":["js","r","css"],"exp":1,"qualification":"mtech"},
    {"id":1,"name":"ravi","skills":["java","python"],"exp":3,"qualification":"btec"},
    {"id":1,"name":"tom","skills":["java","css","r","sql"],"exp":4,"qualification":"bca"},
    {"id":1,"name":"ryan","skills":["c","css","python"],"exp":0,"qualification":"mca"},
]

# print("total number of students",len(students))


# for st in students:
#     print(st.get("name"))
all_stud_names=[st.get("name") for st in students]
# print(all_stud_names)


exp=[st.get("name") for st in students if st.get("exp")>1]
print(exp)


for st in students:
    if "java" in st.get("skills") and "python" in st.get("skills"):
        print(st.get("name"))

mca_stud=[st.get("name") for st in students if st.get("qualification")=="mca"]
print(mca_stud)


most_exp=max(students,key=lambda d:d.get("exp"))
print(most_exp)
higest_exp=most_exp.get("exp")
print(higest_exp)
most_exp_stud=[st.get("name") for st in students if st.get("exp")==higest_exp]
print(most_exp_stud)


#students names having skills>2
skills_2=[st.get("name") for st in students if len(st.get("skills"))>2]
print(skills_2)

#having maximum skills
max_skill=max(students,key=lambda d:len(d.get("skills")))
print(max_skill)

# name starting with j
for st in students:
    if st.get("name").startswith("j"):
        print(st.get("name"))


# most selected skill
skill_count={}
for st in students:
    skills=st.get("skills")
    for sk in skills:
        if sk in skill_count:
            skill_count[sk]+=1
        else:
            skill_count[sk]=1
print(skill_count)

most_selected_skill