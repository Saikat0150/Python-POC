from flask import Flask, request, render_template
import pyodbc
import json

app = Flask(__name__)

# Database connection details
db_server = 'RK-0595-SAIKAT'
db_name = 'TRYNEW'
db_user = 'sa'
db_password = '123456'


# API endpoint to render the form page
@app.route('/')
def home():
    return render_template('form.html')


@app.route('/employees', methods=['POST'])
def insert_employees():
    try:
        employees_list = json.loads(request.form.get('employees_list'))

        conn_str = f"DRIVER={{SQL Server}};SERVER={db_server};DATABASE={db_name};UID={db_user};PWD={db_password}"

        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        for employee in employees_list:
            print(employee)
            # Insert into employee details table
            cursor.execute("INSERT INTO Employee_Details (Name, Age) VALUES (?,?)",
                           (employee['Name'], employee['Age']))

            cursor.execute("SELECT ID from Employee_Details WHERE Name = ? AND Age = ?",
                           (employee['Name'], employee['Age']))
            employee_id = cursor.fetchone()[0]

            # Insert into employee address table
            cursor.execute("INSERT INTO Employee_Address (ID, Present_Address, Permanent_Address) VALUES (?,?,?)",
                           (employee_id, employee['Present_Address'], employee['Permanent_Address']))

            # Insert into employee salary table
            cursor.execute("INSERT INTO Employee_Salary (ID, Salary) VALUES (?,?)",
                           (employee_id, employee['Salary']))

        conn.commit()

        cursor.close()
        conn.close()

        return "Data inserted successfully"

    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
