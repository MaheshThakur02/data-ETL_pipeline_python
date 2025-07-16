import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import pandas as pd


# Step 1: Load Data
df = pd.read_csv("car_done.csv")
print("Before dropna:", df.shape)

# Step 2: Clean Data
df.dropna(inplace=True)
print("Before dropna:", df.shape)


# Step 3: Connect to PostgreSQL
engine = create_engine('postgresql://youruusername:yourpassword@localhost:5432/testdb')

# Step 4: Load to PostgreSQL
df.to_sql("cars", engine, if_exists="replace", index=False)
print("Data loaded successfully!")
