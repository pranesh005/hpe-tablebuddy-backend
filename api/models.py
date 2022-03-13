from . import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    std= db.Column(db.String)
    section = db.Column(db.String)
    password = db.Column(db.String)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "std": self.std,
            "section": self.section,
            "password":self.password
        }

class TimeTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    std=db.Column(db.String)
    section=db.Column(db.String)
    day=db.Column(db.String)
    p_one=db.Column(db.String)
    p_two=db.Column(db.String)
    p_three=db.Column(db.String)
    p_four=db.Column(db.String)
    p_five=db.Column(db.String)
    p_six=db.Column(db.String)

    def to_dict(self):
        return {
            "id":self.id,
            "std":self.std,
            "section":self.section,
            "day":self.day,
            "p_one":self.p_one,
            "p_two":self.p_two,
            "p_three":self.p_three,
            "p_four":self.p_four,
            "p_five":self.p_five,
            'p_six':self.p_six,
        }