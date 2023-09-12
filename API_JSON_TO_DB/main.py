import json
import pyodbc

# Database connection details
db_server = 'RK-0595-SAIKAT'
db_name = 'TRY'
db_user = 'sa'
db_password = '123456'

with open('data.json', 'r') as f:
    data = json.load(f)


try:
    con = pyodbc.connect('DRIVER={SQL Server};SERVER=' + db_server + ';DATABASE=' + db_name +
                         ';UID=' + db_user + ';PWD=' + db_password)

    cur = con.cursor()

    for item in data:
        print(item)
        details_val = (item['Name'], item['Age'])

        # Insert into employee details table
        details_sql = "INSERT INTO Employee_Details (Name, Age)VALUES(?,?)"
        cur.execute(details_sql, details_val)

        cur.execute("SELECT ID from Employee_Details WHERE Name = ? AND Age = ?", details_val)
        emp_id = cur.fetchone()[0]
        print(emp_id)

        address_val = (emp_id, item['Present_Address'], item['Permanent_Address'])
        salary_val = (emp_id, item['Salary'])

        # Insert into employee address table
        cur.execute("INSERT INTO Employee_Address (ID, Present_Address, Permanent_Address)VALUES(?,?,?)", address_val)

        # Insert into employee salary table
        cur.execute("INSERT INTO Employee_Salary (ID, Salary)VALUES(?,?)", salary_val)

        cur.commit()

    cur.close()
    con.close()

except Exception as e:
    print("Cannot Connect")

