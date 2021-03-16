import os
from flask_script import Manager, Command
from flask_migrate import Migrate, MigrateCommand
import SQL_Stringers.SQL_Seeder as SQLString

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

class seedInit(Command):
    "Creates empty tables for database."
    def run(self):
        engineDB.execute(SQLString.SQL_Init_String(DBName))
        print("Database successfully seeded with empty tables.")

class dropDatabase(Command):
    "Deletes database (DANGEROUS)"
    def run(self):
        engineDB.execute("DROP DATABASE " + DBName)
        print("Database successfully deleted.")

@manager.command
def run():
    app.run()

manager.add_command('create-db', createDB())
manager.add_command('db-seed-init', seedInit())
manager.add_command('danger-drop-database', dropDatabase())
manager.add_command('db', MigrateCommand)

# Class Imports
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))

if __name__ == '__main__':
    manager.run()
