import pandas as pd
from sqlalchemy import create_engine

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "placement",
}
csv_file = 'placepredict_with_remarks.csv'
table_name = 'student_data'
engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

try:
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

except Exception as e:
    print(f"An error occurred: {e}")

