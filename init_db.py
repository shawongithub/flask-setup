from app.models import db, User, Note, Power, Role

def initializer_database():
    tables = [
        User,
        Note,
        Power,
        Role
    ]

    try:
        db.drop_tables(models=tables)
        db.create_tables(models=tables)
    except Exception as e:
        raise e



if __name__ == '__main__':
    initializer_database()