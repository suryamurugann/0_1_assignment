import json

class authentication():
    def __init__(self,file=r'C:\Users\AKAS\Documents\107_Assignments,qust\Final_Project _assignment_7\__20__final_project.py\details.json') :
        self.file=file
        authentication.load_user_credentials(self)
    def load_user_credentials(self):
        try:
            with open(self.file, 'r') as file:
                self.credentials = json.load(file)
        except FileNotFoundError as a:
            print(a)
    def userlogin(self,username,password):
        for credits in self.credentials:
            if username ==credits['name'] and password ==credits['password']:
                return True,credits['name']
        else:
            return False
    def adminlogin(self,password):
        if password == "Shop@123":
            return True
        return False            
    def userRegister(self,name,phoneNumber,email,address,password):
        obj={'name': name, 'phoneNumber': phoneNumber, 'email': email, 'address': address, 'password': password}
        self.credentials.append(obj)
        try:
            with open(self.file, 'w') as file:
                json.dump(self.credentials, file)
        except FileNotFoundError as a:
            print(a)