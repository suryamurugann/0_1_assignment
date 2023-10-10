# Assignment 6.1.1

import json

class Employee:
    def __init__(self, name, DOB, height, city, state):
        self.name = name
        self.DOB = DOB
        self.height = height
        self.city = city
        self.state = state

employee_list = []

with open(r'C:\Users\AKAS\Documents\107_Assignments,qust\assignment_6\employee_as_6.json') as json_file:
    data = json.load(json_file)
    for employee_data in data:
        name = employee_data["name"]
        DOB = employee_data["DOB"]
        height = employee_data["height"]
        city = employee_data["city"]
        state = employee_data["state"]
        
        employee = Employee(name, DOB, height, city, state)
        employee_list.append(employee)

for employee in employee_list:
    print(f"\nName: {employee.name}, DOB: {employee.DOB}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")



# Assignment 6.1.2

import json


indian_states_and_capitals = {
    "Tamil Nadu": "Chennai",
    "Andhra Pradesh":"Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram"
    
}

with open(r'C:\Users\AKAS\Documents\107_Assignments,qust\assignment_6\indian_states.json', 'w') as json_file:
    json.dump(indian_states_and_capitals, json_file)
    print("\nIndian states and capitals have been written to indian_states.json.\n")