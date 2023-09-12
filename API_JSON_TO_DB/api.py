from flask import Flask, request, render_template
import pyodbc
import json
import data_connection

app = Flask(__name__)


obj = data_connection.DbConnection()
conn_str = obj.connection()


# API endpoint to render the form page
@app.route('/')
def home():
    return render_template('form.html')


@app.route('/employees', methods=['POST'])
def insert_employees():
    try:
        employees_list = json.loads(request.form.get('employees_list'))

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


@app.route('/display')
def display_data():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Employee_Details")
        employee_details = cursor.fetchall()

        cursor.execute("SELECT * FROM Employee_Address")
        employee_address = cursor.fetchall()

        cursor.execute("SELECT * FROM Employee_Salary")
        employee_salary = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template('display.html', employee_details=employee_details, employee_address=employee_address,
                               employee_salary=employee_salary)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
