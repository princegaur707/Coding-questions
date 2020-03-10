class Employee:
    leaves=8
prince= Employee()
pri= Employee()
print(f"Employee Leaves: {Employee.leaves}")
print(f"pri leaves: {pri.leaves}")
pri.leaves=9
print("After Updating:-")
print(f"                    Employee Leaves: {Employee.leaves}")
print(f"                    pri leaves: {pri.leaves}")
print(pri.__dict__)