# __dict__ expalanation
class Employee:
    leaves=8
prince= Employee()
pri= Employee()
print(f"Employee Leaves: {Employee.leaves}")
print(f"pri leaves: {pri.leaves}")
pri.leaves=9 #Instantaneous variable
print("After Updating:-")
print(f"                    Employee Leaves: {Employee.leaves}")
print(f"                    pri leaves: {pri.leaves}")
print(pri.__dict__) #dict is a attribute