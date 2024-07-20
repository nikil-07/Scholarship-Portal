from app import db, app
from model import StudentInfo, Company, Login
from datetime import datetime

def initialise_db():
    db.create_all()

# # Creating Views
def list_all_students():
    students = StudentInfo.query.all()
    return students
def list_all_login_info():
    login_data = Login.query.all()
    return login_data

def add_student(student):
    student = StudentInfo(**student)
    db.session.add(student)
    db.session.commit()
    return list_all_students()

def add_employee(employee):
    employee = Company(**employee)
    db.session.add(employee)
    db.session.commit()
    return list_all_employees()

def list_all_employees():
    employees = Company.query.all()
    return employees



# def get_by_ticket_no(ticket_no):
#     return db.session.get(Ticket, ticket_no)

# def filter_by_category(category):
#     tickets = Ticket.query.filter_by(category=category).all()
#     return tickets

# def filter_by_priority(priority):
#     tickets = Ticket.query.filter_by(priority=priority).all()
#     return tickets

# def filter_by_status(status):
#     tickets = Ticket.query.filter_by(status=status).all()
#     return tickets

# def update_status(ticket_no):
#     ticket = get_by_ticket_no(ticket_no)
#     ticket.status = "closed"
#     ticket.close_date = datetime.now()
#     db.session.commit()

# def delete_ticket(ticket_no):
#     ticket = get_by_ticket_no(ticket_no)
#     db.session.delete(ticket)
#     db.session.commit()

# def delete_all():
#     Ticket.query.delete()
#     db.session.commit()


if __name__ == "__main__" :
    with app.app_context() :    
        initialise_db()
        # students = [{"aadhar": "1111222233334444", "name" : "Jack", "gender" : "Male", "caste" : "OBC","age" : "22",  "ssc" : "89",  "hsc" : "90",  "annual_income" : "1000000",  "parent_profession" : "Industry Server", "parent_company": "A","emp_id": "1122"}]
        # for student in students :
        #     print(add_student(student))
# 
        # print(list_all_login_info())

        # employees=[{"emp_id":"123","emp_name":"Jane","emp_post":"Manager","income":"300000"}]
        # for employee in employees :
        #     print(add_employee(employee))



    #     tickets = [{"product": "S21", "category" : "Hardware Issues"},
    #                 {"product": "S22", "category" : "Software Issues"}]
        
    #     for ticket in tickets :
    #         print(add_ticket(ticket))

#         # print(filter_by_category("Hardware Issues"))
#         tck = get_by_ticket_no(1)
#         print(tck.to_json())
        # ticket = get_by_ticket_no(4)
        # ticket.status = "pending"
        # ticket.close_date = datetime.now()
        # db.session.commit()


# ----------- Testing Rest API requests --------------------
# import requests
# import pandas as pd

# url = r"http://127.0.0.1:5000/tickets"

# response = requests.put(url+"/1")
# print("Response Status - ", response.status_code)
# print("---------- Ticket Closed ----------")
# print("-"*50)

# data_to_update = {"category" : "Network Issues", 
#                   "priority" : "high"}
# response = requests.put(url+"/obj/1", 
#                         json=data_to_update)
# print("Response Status - ", response.status_code)
# print("---------- Ticket Closed ----------")
# print("-"*50)

# response = requests.delete(url+"/1")
# print("Response Status - ", response.status_code)
# print(response.text)

# response = requests.delete(url+"/all")
# print("Response Status - ", response.status_code)
# print(response.text)


# response = requests.get(url)
# print("Response Status - ", response.status_code)
# print("--------- All Tickets -------------------")
# ticket_df = pd.DataFrame(response.json())
# print(ticket_df)


# response = requests.get(url + "/1")
# print("Response Status - ", response.status_code)
# print("Ticket Object - ", response.json())

# print("-"*50)
# data = {"product" : "Samsung Note", "category" : "Hardware Issues"}
# response = requests.post(url, json=data)
# print("Response Status - ", response.status_code)
# print("Ticket Added successfully!!!")