from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
import json
import data_connection_sqlalchemy

app = Flask(__name__)

obj = data_connection_sqlalchemy.DbConnection()
con_str = obj.connection()

app.config['SQLALCHEMY_DATABASE_URI'] = con_str
app.config['SALALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# define the Employee_Details table
employee_details = db.Table('Employee_Details',
                            db.Column('ID', db.Integer, primary_key=True),
                            db.Column('Name', db.String(50)),
                            db.Column('Age', db.Integer)
                            )

# Define the EmployeeAddress table
employee_address = db.Table('Employee_Address',
                            db.Column('Id', db.Integer, primary_key=True),
                            db.Column('EmpID', db.Integer, db.ForeignKey('Employee_Details.ID')),
                            db.Column('Present_Address', db.String(255)),
                            db.Column('Permanent_Address', db.String(255))
                            )

# Define the EmployeeSalary table
employee_salary = db.Table('Employee_Salary',
                           db.Column('Id', db.Integer, primary_key=True),
                           db.Column('EmpID', db.Integer, db.ForeignKey('Employee_Details.ID')),
                           db.Column('Salary', db.Integer)
                           )


# API endpoint to render the form page
@app.route('/')
def home():
    return render_template('form.html')


@app.route('/employees', methods=['POST'])
def insert_employees():
    try:
        employee_list_str = request.form.get('employees_list')
        employee_list = json.loads(employee_list_str)
        print(employee_list)

        with app.app_context():
            for employee in employee_list:
                print(employee)
                result = db.session.execute(employee_details.insert().values(Name=employee['Name'],
                                                                             Age=employee['Age']))
                employee_id = result.inserted_primary_key[0]
                print(employee_id)

                # db.session.flush()  # Get the generated ID

                db.session.execute(employee_address.insert().values(EmpID=employee_id,
                                                                    Present_Address=employee['Present_Address'],
                                                                    Permanent_Address=employee['Permanent_Address']))

                db.session.execute(employee_salary.insert().values(EmpID=employee_id,
                                                                   Salary=employee['Salary']))

            db.session.commit()

            return "Data inserted successfully"

    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
