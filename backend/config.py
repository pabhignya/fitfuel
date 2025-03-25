import os

# Flask Config
SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/fitfuel'
SQLALCHEMY_TRACK_MODIFICATIONS = False

