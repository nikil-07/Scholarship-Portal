from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 
db = SQLAlchemy()
 
class StudentInfo(db.Model):
    aadhar = db.Column(db.String(12) , nullable = False ,primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    caste = db.Column(db.String(80), nullable = False)
    gender = db.Column(db.String(11), nullable = False)
    status = db.Column(db.String(10), default="pending", nullable = False)
    annual_income = db.Column(db.String(100), nullable = False)
    parent_profession = db.Column(db.String(100), nullable = False)
    ssc = db.Column(db.String(5), nullable = False)
    hsc = db.Column(db.String(5), nullable = False)
    contact_no = db.Column(db.String(10), nullable = False)
    age = db.Column(db.String(2), nullable = False)
    domicile = db.Column(db.String(300), nullable = False)
    company = db.Column(db.String(300), nullable = False)
    emp_post = db.Column(db.String(300), nullable = False)
    employee_id = db.Column(db.String(3), nullable = False)
    application_date = db.Column(db.Date, default = datetime.now(), nullable = False)
    update_date = db.Column(db.Date)
 
    # test = db.Column(db.String(20), nullable = False, default = "world")
 
    def __repr__(self):
        return f"{self.aadhar}, {self.name}, {self.caste}, {self.gender}, {self.status}, {self.annual_income}, {self.parent_profession}, {self.ssc}, {self.hsc}, {self.age}, {self.domicile}, {self.company}, {self.emp_post}, {self.employee_id}, {self.application_date}, {self.update_date}"
   
    def to_json(self):
        ticket_dict = self.__dict__
        ticket_dict.pop('_sa_instance_state')
        return ticket_dict
 
class Company(db.Model):
    emp_id = db.Column(db.String(12) , nullable = False ,primary_key = True)
    emp_name = db.Column(db.String(300), nullable = False)
    emp_post = db.Column(db.String(80), nullable = False)
    income = db.Column(db.String(80), nullable = False)
 
    def __repr__(self):
        return f"{self.emp_id}, {self.emp_name}, {self.emp_post}, {self.income}"
   
    # def to_json(self):
    #     ticket_dict = self.__dict__
    #     ticket_dict.pop('_sa_instance_state')
    #     return ticket_dict
 
class Login(db.Model):
    aadhar = db.Column(db.String(12) , nullable = False ,primary_key = True)
    password = db.Column(db.String(300), nullable = False)

    def __repr__(self):
        return f"{self.aadhar}, {self.password}"