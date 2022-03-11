from asyncio import streams
from .models import Student
from api import db
from flask_sqlalchemy import SQLAlchemy
from ariadne import convert_kwargs_to_snake_case
from sqlalchemy import text

def listStudents_resolver(obj, info):
    try:
        students = [student.to_dict() for student in Student.query.all()]
        print(students)
        payload = {
            "success": True,
            "students": students
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def addStudent_resolver(obj,info,id,name,email,section_id,password):
    try:
        student=Student()
        student.id=id
        student.email=email
        student.name=name
        student.section_id=section_id
        student.password=password
        db.session.add(student)
        db.session.commit()
        payload={
            "success":True,
            "message":"Student added successfully"

        }
    except Exception as error:
        payload={
            "success":False,
            "errors":error
        }
    return payload


@convert_kwargs_to_snake_case
def getStudent_resolver(obj, info, email,password):
    try:
        print("email: ")
        student = Student.query.filter_by(email=email,password=password).first()
        # sql_query = flask_sqlachemy.text("SELECT * FROM airports WHERE country = 'United States'")
        # sql = text(f"select * from student where email='{email}' and password='{password}'")
        # result = db.engine.execute(sql)
        # names = [row for row in result]
        # student={
        #     "id": names[0][0],
        #     "name": names[0][1],
        #     "email": names[0][2],
        #     "section_id": names[0][3],
        #     "password":names[0][4]
        # }

        # db.engine.execute()
        if(student):
            payload = {
                "success": True,
                "student": student
            }
        else:
            payload = {
            "success": False,
            "errors": [f"Post item matching {email},{password} not found"]
            }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Post item matching {name},{password} not found"]
        }
    return payload
