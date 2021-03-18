import os
import SQL_Stringers.SQL_Seeder as SQLString
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


manager = Manager(app)
engineDB = db.create_engine(app.config['DATABASE_SERVER'], {})
DBName = app.config['DB_NAME']

class createDB(Command):
    "Creates a named database from the configuration."
    def run(self):
        engineDB.execute("CREATE DATABASE IF NOT EXISTS " + DBName)
        print("Database successfully created.")

# class seedInit(Command): # Outdated and unnecessary
#     "Creates empty tables for database." # Outdated and unnecessary
#     def run(self): # Outdated and unnecessary
#         engineDB.execute(SQLString.SQL_Init_String(DBName)) # Outdated and unnecessary
#         print("Database successfully seeded with empty tables.") # Outdated and unnecessary

class dropDatabase(Command):
    "Deletes database (DANGEROUS)"
    def run(self):
        engineDB.execute("DROP DATABASE " + DBName)
        print("Database successfully deleted.")

manager.add_command('create-db', createDB())
# manager.add_command('db-seed-init', seedInit()) # Outdated and unnecessary
manager.add_command('danger-drop-database', dropDatabase())
manager.add_command('db', MigrateCommand)

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
