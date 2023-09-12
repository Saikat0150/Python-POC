from flask import Flask, flash, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import data_connection_sqlalchemy

app = Flask(__name__)

obj = data_connection_sqlalchemy.DbConnection()
con_str = obj.connection()

app.config['SQLALCHEMY_DATABASE_URI'] = con_str
app.config['SALALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Employee_Details(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50))
    Age = db.Column(db.Integer)


# Define the EmployeeAddress table model
class Employee_Address(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    EmpID = db.Column(db.Integer, db.ForeignKey('employee_details.ID'))
    Present_Address = db.Column(db.String(255))
    Permanent_Address = db.Column(db.String(255))


# Define the EmployeeSalary table model
class Employee_Salary(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    EmpID = db.Column(db.Integer, db.ForeignKey('employee_details.ID'))
    Salary = db.Column(db.Integer)


# API endpoint to render the form page
@app.route('/')
def home():
    return render_template('form.html')


# API endpoint to receive the JSON list
@app.route('/employees', methods=['POST'])
def insert_employees():
    try:
        # Get the JSON list from the form submission
        employees_list = json.loads(request.form.get('employees_list'))

        # Iterate over the employees and insert into the tables
        for employee in employees_list:
            # Create EmployeeDetails object
            employee_details = Employee_Details(Name=employee['Name'], Age=employee['Age'])
            db.session.add(employee_details)
            db.session.flush()  # Get the generated ID

            # Create EmployeeAddress object
            employee_address = Employee_Address(employee_id=employee_details.ID,
                                                Present_Address=employee['Present_Address'],
                                                Permanent_Address=employee['Permanent_Address'])
            db.session.add(employee_address)

            # Create EmployeeSalary object
            employee_salary = Employee_Salary(employee_id=employee_details.ID, salary=employee['Salary'])
            db.session.add(employee_salary)

        # Commit the changes to the database
        db.session.commit()

        return "Data inserted successfully"

    except Exception as e:
        return str(e)


# API endpoint to display data from all tables
@app.route('/display')
def display_data():
    try:
        # Retrieve data from all tables
        select = db.select(Employee_Details)
        employee_details = db.session.execute(select).scalar()
        employee_address = db.session.execute(select).scalar()
        employee_salary = db.session.execute(select).scalar()

        return render_template('display.html', employee_details=employee_details, employee_address=employee_address,
                               employee_salary=employee_salary)

    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
