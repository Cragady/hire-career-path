from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# Commands Available:
#  python manage.py <command>
#  <command>
#    db init, db migrate, db upgrade, db --help

app = Flask(__name__)

# App Config Import
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Class Imports
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))

if __name__ == '__main__':
    manager.run()
