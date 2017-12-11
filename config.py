import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MONGODB_SETTINGS = {'db': 'todoflappdb',
                        'host': 'mongodb://localhost/todoflappdb'}
    DEBUG = True

    DEBUG_TB_PANELS = ['flask_mongoengine.panels.MongoDebugPanel']
