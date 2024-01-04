from sqlalchemy import create_engine
# from sqlalchemy..declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
import configparser


config = configparser.ConfigParser()
config.read("../data_loader/config.ini")
host=config['Docker Local Config']['host']
port=config['Docker Local Config']['port']
database=config['Docker Local Config']['database']
user=config['Docker Local Config']['user']
password=config['Docker Local Config']['password']

db_url=f'postgresql://{user}:{password}@{host}:{port}/{database}'

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(db_url)
#     db_url, connect_args={"check_same_thread": False}
# )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

print("complete")
