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

class TimeTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    std=db.Column(db.String)
    section=db.Column(db.String)
    day=db.Column(db.String)
    period_1=db.Column(db.String)
    period_2=db.Column(db.String)
    period_3=db.Column(db.String)
    period_4=db.Column(db.String)
    period_5=db.Column(db.String)
    period_6=db.Column(db.String)

    def to_dict(self):
        return {
            "std":self.std,
            "section":self.section,
            "day":self.day,
            "period_1":self.period_1,
            "period_2":self.period_2,
            "period_3":self.period_3,
            "period_4":self.period_4,
            "period_5":self.period_5,
            "period_6":self.period_6,
        }