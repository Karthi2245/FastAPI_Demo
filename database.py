from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = "sqlite:///./inventory.db"
engine = create_engine(db)
local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()

