from app import app
from flask import Server,Manager
app = app('development') 
manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test():
    '''
    Run test
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verboity=2).run(tests)
if __name__ == '__main__':
    manager.run()
