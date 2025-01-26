import json
import os
cwd = os.getcwd()
print(cwd)

def employee_information():
   user_dict = {
       "Name":"Afaz",
       'Phone Number':'4389310083',
       'Email address':'afaz3192@gmail.com'
   }
   return user_dict
def user_information_json(employee_dict):
    with open('data.json', 'w')as json_file:
        json.dump(employee_dict, json_file)
        return json_file

def retrieve_information(user_json_file):
   with open('data.json', 'r') as json_file:
       data = json.load(json_file)
       return data

def search_user_information(json_data):
    user_input = input("Search by name,phone number, email address:")
    found = False
    for value in json_data.values():
        if value == user_input:
            found = True
            print(f"Found and here is the information: {value}")





#user_name = input("Name:")
#user_phone_number = input("Phone Number:")
#user_email = input("Email address:")
#the function is converting informations into dictionary
employee_information()
#the function is converting into json
user_information_json(employee_information())
#this function is retrieving the user information as dictionary
retrieve_information(user_information_json((employee_information())))
search_user_information(json_data=retrieve_information(user_information_json((employee_information()))))