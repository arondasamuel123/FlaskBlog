from app import create_app,db
from app.models import User, Posts, Comment
from flask_script import Manager, Server
from flask_migrate import Migrate,MigrateCommand



app = create_app('development')
manager = Manager(app)
manager.add_command('serve', Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def shell_context():
    return dict(db=db, User=User, Posts=Posts, Comment=Comment)

if __name__== '__main__':
    manager.run()
