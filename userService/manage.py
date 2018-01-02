#https://testdriven.io/

from flask_script import Manager
from init_flask_app import createApp
from config import config_prefix
app = createApp('development', config_prefix)

manager = Manager(app)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()