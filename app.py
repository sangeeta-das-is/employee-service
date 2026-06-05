from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

DB_CONFIG = {
    "host": "db",
    "database": "employee_db",
    "user": "employee_user",
    "password": "StrongPassword123"
}

@app.route('/employees')
def get_employees():

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("SELECT name, role FROM employees")

    rows = cur.fetchall()

    employees = []

    for row in rows:
        employees.append({
            "name": row[0],
            "role": row[1]
        })

    cur.close()
    conn.close()

    return jsonify(employees)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
