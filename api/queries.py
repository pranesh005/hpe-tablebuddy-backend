from .models import Student
from ariadne import convert_kwargs_to_snake_case

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

@convert_kwargs_to_snake_case
def getStudent_resolver(obj, info, id):
    try:
        student = Student.query.get(id)
        payload = {
            "success": True,
            "student": student.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Post item matching {id} not found"]
        }
    return payload
