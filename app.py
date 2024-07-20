from flask import Flask,render_template, request, redirect, send_from_directory
from flask_migrate import Migrate
from datetime import datetime
from model import StudentInfo,Login,Company,db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scholarship.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/user.html")
def user():
    return render_template("user.html")


# Function to add a new login record
def add_login(aadhar, password):
    login = Login(aadhar=aadhar, password=password)
    db.session.add(login)
    db.session.commit()

@app.route('/submit', methods=['POST', 'GET'])
def add_info():
    aadhar = request.form['aadhar']
    name = request.form['name']
    caste = request.form['caste']
    gender = request.form['gender']
    annual_income = request.form['annual_income']
    parent_profession = request.form['parent_profession']
    ssc = request.form['ssc']
    hsc = request.form['hsc']
    contact_no = request.form['contact_no']
    age = request.form['age']
    domicile = request.form['domicile']
    company = request.form['company']
    emp_post = request.form['emp_post']
    employee_id = request.form['employee_id']

    

    # Assuming you have a model defined, e.g., Application
    new_info = StudentInfo(
        aadhar = aadhar,
        name=name,
        caste=caste,
        gender=gender,
        annual_income=annual_income,
        parent_profession=parent_profession,
        ssc=ssc,
        hsc=hsc,
        contact_no=contact_no,
        age=age,
        domicile=domicile,
        company=company,
        emp_post=emp_post,
        employee_id=employee_id
    )
    
    db.session.add(new_info)
    db.session.commit()
    return f"Success!"  # Redirect to a success page or back to the form

@app.route("/admin.html")
def admin_panel():
    students = StudentInfo.query.all()
    return render_template("admin.html", students=students)

# Route for view form
@app.route("/view/<string:aadhar>", methods=["GET"])
def fetch_form(aadhar):
    student = StudentInfo.query.filter_by(aadhar=aadhar).first()
    if student:
        return render_template("view_form.html", student=student)
    else:
        # Handle case where student with given Aadhar number doesn't exist
        return "Student not found", 404

@app.route("/result.html/<string:status>")
def result(status):
    return render_template("result.html", status=status)

# Route for the login form
@app.route('/user_form.html', methods=['POST'])
def user_form():
    if request.method == 'POST':
        aadhar = request.form['aadhar']
        password = request.form['password']

        # Check if the login exists in the database
        user = Login.query.filter_by(aadhar=aadhar, password=password).first()

        print(user)
        if user is not None:
            status = StudentInfo.query.filter_by(aadhar=aadhar).first()
            status_student = status.status
            return (f"<h1 > {status_student} </h1>")
        else:
            add_login(aadhar, password)
            return render_template('user_form.html', aadhar=aadhar)

    # return render_template('user_form.html')  # Render as a GET request (if needed)

# Route for approving a student
@app.route("/approve/<string:aadhar>")
def approve_student(aadhar):
    student = StudentInfo.query.filter_by(aadhar=aadhar).first_or_404()
    student.status = 'Approved'
    db.session.commit()
    return redirect(f"/view/{aadhar}")

# Route for disapproving a student
@app.route("/disapprove/<string:aadhar>")
def disapprove_student(aadhar):
    student = StudentInfo.query.filter_by(aadhar=aadhar).first_or_404()
    student.status = 'Disapproved'
    db.session.commit()
    return redirect(f"/view/{aadhar}")



if __name__ == "__main__":
    app.run(debug = True)
