
import pandas as pd
# Pretty print the dictionary to make it readable
from pprint import pprint


df=pd.read_csv("training_and_development_data.csv")
#df.columns
# Convert DataFrame into a dictionary with 'EmpID' as the key (index)
emp_dict = df.set_index("Employee ID").to_dict(orient="index")
#pprint(emp_dict) 
# Function to search employee by EmpID
def get_employee_info(emp_id):
    if emp_id in emp_dict:
        return emp_dict[emp_id]
    else:
        return "Employee not found"

emp_id = int(input("Enter Employee ID: "))  # Asking user for Employee_ID (input)
employee_info = get_employee_info(emp_id)

# Displaying  employee information or a "not found" message
print(employee_info)
# *********id of employee Started from 1001 to 4000 ****************


