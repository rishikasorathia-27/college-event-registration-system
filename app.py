from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",  
    database="college_events"
)

cursor = db.cursor()

# 👉 HOME PAGE (SHOW FORM + COUNT + DATA)
@app.route('/')
def home():
    cursor.execute("SELECT COUNT(*) FROM registrations")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM registrations")
    data = cursor.fetchall()

    return render_template('index.html', total=total, data=data)

# 👉 REGISTER
@app.route('/register', methods=['POST'])
def register():
    data = (
        request.form['full_name'],
        request.form['student_id'],
        request.form['email'],
        request.form['phone'],
        request.form['department'],
        request.form['year'],
        request.form['event']
    )

    query = """
    INSERT INTO registrations 
    (full_name, student_id, email, phone, department, year, event_name)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, data)
    db.commit()

    return "<script>window.location.href='/'</script>"

if __name__ == '__main__':
    app.run(debug=True)
