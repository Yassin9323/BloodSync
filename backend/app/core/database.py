from sqlalchemy import create_engine
from app.models.base_model import Base
from sqlalchemy.orm import sessionmaker
from app.core.config import Config
import time
from sqlalchemy.exc import OperationalError
import atexit

# MySQL database URL
SQLALCHEMY_DATABASE_URL = ('mysql+mysqldb://{}:{}@{}/{}'.
                                    format(Config.SYNC_MYSQL_USER,
                                            Config.SYNC_MYSQL_PWD,
                                            Config.SYNC_MYSQL_HOST,
                                            Config.SYNC_MYSQL_DB))

# Create the engine with the new MySQL URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Drop DB if it was test DB
def retry_ddl_operation(operation, max_retries=5, delay=2):
    for attempt in range(max_retries):
        try:
            operation()
            break
        except OperationalError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    else:
        print("Exceeded maximum retries for DDL operation")

if Config.SYNC_ENV == "test":
    print("Dropping test Database....")
    def drop_all_tables():
        Base.metadata.drop_all(bind=engine)

    retry_ddl_operation(drop_all_tables)
    print("\nPreparing ")

# Configure the session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Define the base class for the ORM models
Base.metadata.create_all(bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
