from app import db
from peewee import *
from datetime import datetime

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField(max_length=100, null=True)
    email = CharField(max_length=50, unique=False, null=False)
    created = DateTimeField(default=datetime.now)
    is_active = BooleanField(default=False)
    is_app_user = BooleanField(default=False)
    is_verified = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    is_staff = BooleanField(default=False)

    class Meta:
        table_name = 'tbl_user'
    def __str__(self):
        return '{}'.format(self.name)

class Note(BaseModel):
    author = ForeignKeyField(User, backref = 'notes')
    title = TextField()

    class Meta:
        table_name = 'tbl_note'

class Power(BaseModel):
    title = CharField(max_length=50)

    class Meta:
        table_name = 'tbl_power'

class Role(BaseModel):
    user = ForeignKeyField(User)
    power = ForeignKeyField(Power)
    status = BooleanField(default=True)

    class Meta:
        table_name = 'tbl_role'
