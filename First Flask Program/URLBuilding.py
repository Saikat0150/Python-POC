from flask import *


app = Flask(__name__)

@app.route('/admin')
def Admin():
    return "Admin"

@app.route('/librarion')
def Librarion():
    return "Librarion"

@app.route('/student')
def Student():
    return "Student"

@app.route('/user/<name>')
def User(name):
    if name == 'Admin':
        return redirect(url_for('Admin'))
    if name == 'Librarion':
        return redirect(url_for('Librarion'))
    if name == 'Student':
        return redirect(url_for("Student"))
    
if __name__ == "__main__":
    app.run(debug=True, port=8080)
