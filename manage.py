import os
from flask_script import Manager, Command
from flask_migrate import Migrate, MigrateCommand

from app import app, db

# Commands Available:
#  python manage.py <command>
#  <command>
#    db init, db migrate, db upgrade, db createDB, db --help

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
class createDB(Command):
    "Creates a named database from the configuration."
    def run(self):
        engine = db.create_engine(app.config['DATABASE_SERVER'], {})
        engine.execute("CREATE DATABASE IF NOT EXISTS " + app.config['DB_NAME'])
        print("Database successfully created.")

manager = Manager(app)
manager.add_command('create-db', createDB())
manager.add_command('db', MigrateCommand)

# Class Imports
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))

if __name__ == '__main__':
    manager.run()
