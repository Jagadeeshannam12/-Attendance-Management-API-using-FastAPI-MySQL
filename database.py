from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url="mysql+pymysql://root:%40Jaggu123@localhost:3306/fastapi_db"
engine=create_engine(db_url)

Session= sessionmaker(autocommit=False,autoflush=False,bind=engine)