#https://testdriven.io/
import os
from flask_script import Manager
from init_flask_app import createApp
from config import config_prefix

app_settings = os.getenv('APP_SETTINGS') or 'development'


app = createApp(app_settings, config_prefix)

manager = Manager(app)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    # print(app_settings)
    manager.run()