from asyncio import streams
from .models import Student, TimeTable
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

def addStudent_resolver(obj,info,name,email,password,section,std):
    try:
        student=Student()
        student.email=email
        student.name=name
        student.section=section
        student.std=std
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


def createTimeTable_resolver(obj,info,std,section,day,p_one,p_two,p_three,p_four,p_five,p_six):
    try:
        # print(list)
        
        timetable=TimeTable()
        timetable.std=std
        timetable.section=section
        timetable.day=day
        timetable.p_one=p_one
        timetable.p_two=p_two
        timetable.p_three=p_three
        timetable.p_four=p_four
        timetable.p_five=p_five
        timetable.p_six=p_six

        db.session.add(timetable)
        db.session.commit()
        payload={
            "success":True,
            "message":"Timetable created successfully"
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
      
        student = Student.query.filter_by(email=email,password=password).first()
        if(student):
            payload = {
                "success": True,
                "student": student
            }
        else:
            payload = {
            "success": False,
            "errors": [f"Student with given credentials not found"]
            }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Student not found"]
        }
    return payload


def getTimeTable_resolver(obj,info,std,section):
    try:
        timetable=[table.to_dict() for table in TimeTable.query.filter_by(std=std,section=section)]
        print(timetable)        
        # print(len(timetable))
        if len(timetable)==0:
            payload = {
            "success": False,
            "errors": [f"section not found"]
            }
            return payload
            
        else:
            print("len !=0")
            # print(timetable)
            payload = {
                "success": True,
                "timetable": timetable
            }
            print(payload)
            return payload
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": "something happened get over with that"
        }
    return payload

def deleteTimeTable_resover(obj,info):
    truncate_query = text("drop table time_table")
    print(db.engine.execute(truncate_query))
    db.create_all()
    payload={
        "success":True,
        "message":"Deleted successfully"
    }
    return payload
