from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



SQL_MODEL_URL="sqlite:///./product.db"
connect_args = {"check_same_thread": False}
engine = create_engine(SQL_MODEL_URL,connect_args=connect_args)

Base= declarative_base()
local_session=sessionmaker(bind=engine,autocommit=False,autoflush=False)



