from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Setting up PostgreSQL database connection: this will be from the created Pgadmin4 and the PostgreSQL containers.
# Create a database in pgadmin4 and use the credentials to connect to the database.

DATABASE_URL = "postgresql://<username>:<password>@localhost:5432/<database_name>"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
