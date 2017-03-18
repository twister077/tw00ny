from gluon import (DAL, Field, IS_NOT_EMPTY)

class Models:
    def __init__(self, *args, **kwargs):
        db1 = None

    def db(self):
        db1 = DAL('sqlite://storage.sqlite')
        db1.define_table('person', Field('name', requires=IS_NOT_EMPTY()))
        return db1


