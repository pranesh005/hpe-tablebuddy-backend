from . import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    section_id = db.Column(db.Integer)
    password = db.Column(db.String)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "section_id": self.section_id,
            "password":self.password
        }