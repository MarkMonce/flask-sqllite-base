from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__='employees'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    address1 = db.Column(db.String(100), nullable=False)
    address2 = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zip = db.Column(db.String(100), nullable=False)
    hourlyrate = db.Column(db.Float)
    age = db.Column(db.Integer)

    def __init__(self, firstname, lastname, address1, address2, city, state, zip, hourlyrate, age):
        self.firstname = firstname
        self.lastname = lastname
        self.address1 = address1
        self.address2 = self.address2
        self.city = city
        self.state = state
        self.zip = zip
        self.hourlyrate = hourlyrate
        self.age = age

    def __repr__(self):
        return f'<Employee {self.name}>'