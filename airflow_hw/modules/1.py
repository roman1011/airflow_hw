import os
import glob

path = 'C:/Users/Roma/airflow_hw/'
a = glob.glob(f"{path}data/models/*.pkl")[-1]

print(a)