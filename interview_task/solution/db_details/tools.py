from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://dev:abcdef123@mysql_db:3306/app_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def with_db_session(func):
    def wrapper(*args, **kwargs):
        with get_db() as db:
            return func(*args, session=db, **kwargs)

    return wrapper
