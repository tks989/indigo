import psycopg2
import configparser
import json
from sqlalchemy import create_engine, delete
import pandas as pd

#load config file
config = configparser.ConfigParser()
config.read("config.ini")
host=config['Docker Local Config']['host']
port=config['Docker Local Config']['port']
database=config['Docker Local Config']['database']
user=config['Docker Local Config']['user']
password=config['Docker Local Config']['password']

#create connection with postgres in docker container
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
    )

# Create dictionary of data
f = open('./assets_machines.json')
data = json.load(f)
f.close()

#convert to pandas
df = pd.DataFrame.from_dict(data['machines'])

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
df.to_sql('machines', engine, if_exists='replace')

