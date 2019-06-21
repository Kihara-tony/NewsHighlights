from app import app
from flask import Server,Manager
app = app('development') 
manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test():