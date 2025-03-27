from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Students


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://robert@localhost/school_db'
db.init_app(app)


@app.route("/students/", methods=['GET'])
def get_students():
    return jsonify(get_all_students())


@app.route('/old_students/', methods=['GET'])
def get_old_students():
    students = get_all_students()
    old_students = [stud for stud in students if stud['age'] >= 20]
    return jsonify(old_students)


@app.route('/young_students/', methods=['GET'])
def get_young_students():
    students = get_all_students()
    young_students = [stud for stud in students if stud['age'] < 20]
    return jsonify(young_students)


@app.route('/advance_students/', methods=['GET'])
def get_advance_students():
    students = get_all_students()
    advance_students = [stud for stud in students if stud['age'] < 20 and stud['grade'] == 'A']
    return jsonify(advance_students)


@app.route('/student_ages/', methods=['GET'])
def get_student_ages():
    students = get_all_students()
    student_ages = [{'student_name': f"{stud['first_name']} {stud['last_name']}", 'age':stud['age']} for stud in students]
    return jsonify(student_ages)

def get_all_students():
    students = Students.query.all()
    json_students = [{'id': stud.id, 'first_name': stud.first_name, 'last_name': stud.last_name, 'age': stud.age, 'grade': stud.grade} for stud in students]
    return json_students


if (__name__) == '__main__':
    app.run(debug=True, port=8000)