import json
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database connection details
db_server = 'localhost'
db_name = 'sqlalchemy'
db_user = 'root'
db_password = '123456'

# Configure the database connection URI
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_password}@{db_server}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy database instance
db = SQLAlchemy(app)


# Define the EmployeeDetails table model
class employeedetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    #address = db.relationship('employeeaddress', back_populates='employee', uselist=False, lazy=True)
    #salary = db.relationship('employeesalary', back_populates='employee1', uselist=False, lazy=True)


# Define the EmployeeAddress table model
class employeeaddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer)#, db.ForeignKey('employee_details.id'))
    address = db.Column(db.String(200))
    #employee = db.relationship('employeedetails', back_populates='address', uselist=False, lazy=True)


# Define the EmployeeSalary table model
class employeesalary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer)#, db.ForeignKey('employee_details.id'))
    salary = db.Column(db.Integer)
    #employee1 = db.relationship('employeedetails', back_populates='salary', uselist=False, lazy=True)


# API endpoint to render the form page
@app.route('/')
def home():
    return render_template('form.html')


# API endpoint to receive the JSON list
@app.route('/employees', methods=['POST'])
def insert_employees():
    try:
        # Get the JSON list from the form submission
        employees_list_str = request.form.get('employees_list')

        # Parse the JSON list
        employees_list = json.loads(employees_list_str)

        # Iterate over the employees and insert into the tables
        for employee in employees_list:
            # Create EmployeeDetails object
            employee_details = employeedetails(name=employee['name'], age=employee['age'])
            db.session.add(employee_details)
            db.session.flush()  # Get the generated ID

            # Create EmployeeAddress object
            employee_address = employeeaddress(employee_id=employee_details.id, address=employee['address'])
            db.session.add(employee_address)

            # Create EmployeeSalary object
            employee_salary = employeesalary(employee_id=employee_details.id, salary=employee['salary'])
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

        employee_details = employeedetails.query.all()
        employee_address = employeeaddress.query.all()
        employee_salary = employeesalary.query.all()

        return render_template('display1.html', employee_details=employee_details, employee_address=employee_address,
                               employee_salary=employee_salary)

    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
