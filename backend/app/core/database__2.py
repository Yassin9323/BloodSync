from sqlalchemy import create_engine
from app.models.base_model import Base
from sqlalchemy.orm import sessionmaker
from app.core.config import Config


# MySQL database URL
SQLALCHEMY_DATABASE_URL = ('mysql+mysqldb://{}:{}@{}/{}'.
                                    format(Config.HBNB_MYSQL_USER,
                                            Config.HBNB_MYSQL_PWD,
                                            Config.HBNB_MYSQL_HOST,
                                            Config.HBNB_MYSQL_DB))

# Create the engine with the new MySQL URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

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
