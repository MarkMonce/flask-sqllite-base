from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from employees.forms import EmployeeForm
from models import db, Employee

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

# with app.app_context():
#     db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/add_user', methods=['GET', 'POST'])
# def add_employees():
#     form = EmployeeForm()
#     if form.validate_on_submit():
#         user = User(name=form.name.data, email=form.email.data)
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('view_employees'))
#     return render_template('add_employees.html', form=form)

# @app.route('/view_users')
# def view_users():
#     users = User.query.all()
#     return render_template('view_users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
