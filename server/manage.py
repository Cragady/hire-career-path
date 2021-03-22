import os
import unittest

from flask_script import Manager, Command
from flask_migrate import Migrate, MigrateCommand
from app import blueprint
from app.main import create_app, db

# Commands Available:
#  python manage.py <command>
#  <command>
#    db init, db migrate, db upgrade, db createDB, db --help

# app.config.from_object(os.environ['APP_SETTINGS'])

app = create_app()
app.register_blueprint(blueprint)
app.app_context().push()
migrate = Migrate(app, db)

lambda_app = app

engineDB = db.create_engine(app.config['DATABASE_SERVER'], {})
DBName = app.config['DB_NAME']
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def create_db():
    engineDB.execute("CREATE DATABASE IF NOT EXISTS " + DBName)
    print("Database successfully created.")

@manager.command
def drop_database():    
    engineDB.execute("DROP DATABASE " + DBName)
    print("Database successfully deleted.")
        

@manager.command
def run():
    app.run(host='0.0.0.0', port=5000)

@manager.command
def test():
    """ Runs tests """
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

# Class Imports
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))


if __name__ == '__main__':
    manager.run()
