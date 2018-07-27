import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ['homerion@gmail.com']
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD =   os.environ.get('MAIL_PASSWORD')

# mail username and password should be strings if doing this locally


# in command line export these env variables (when in environment):
# export FLASK_APP=main.py
# export FLASK_DEBUG=1
# export MAIL_SERVER=smtp.googlemail.com
# export MAIL_PORT=587
# export MAIL_USE_TLS=1
# export MAIL_USERNAME=[PUT YOUR USERNAME]
# export MAIL_PASSWORD=[PUT YOUR PASSWORD]

# Because I use 2-step validation the mail password should be generated using:
# https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor
# if I am doing a local debugging


# In a separate terminal activate local mail server using:
# python -m smtpd -n -c DebuggingServer localhost:8025
