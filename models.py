from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstnamme = db.Column(db.String(100), nullable=False)
    lastnamme = db.Column(db.String(100), nullable=False)
    address1 = db.Column(db.String(100), nullable=False)
    address2 = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zip = db.Column(db.String(100), nullable=False)
    hourlyrate = db.Column(db.Float)
    age = db.Column(db.Int)

    def __repr__(self):
        return f'<User {self.name}>'