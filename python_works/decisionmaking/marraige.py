her_age=int(input("Enter her age: "))
his_age=int(input("Enter his age: "))
# marraige_status=False

marraige_status=int(input("Select marraige status 1 for married 2 for unmarried: "))

if(her_age>=21 and his_age>=21 and marraige_status==2):
    print("Proceed")
else:
    print("Not possible")

