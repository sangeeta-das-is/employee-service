from flask import Flask, jsonify

app = Flask(__name__)

employees = [
    {"name": "Max", "role": "Admin"},
    {"name": "Anna", "role": "HR"}
]

@app.route('/employees')
def get_employees():
    return jsonify(employees)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
