# <YOUR_IMPORTS>
from datetime import datetime
import json

import dill
import os
import glob

import pandas as pd

path = os.environ.get('PROJECT_PATH', '..')


def predict():
    filename = glob.glob(f"{path}/data/models/*.pkl")
    with open(f'{filename[-1]}', 'rb') as file:
        model = dill.load(file)
    df = pd.DataFrame(columns=['id', 'price', 'pred'])
    for elem in os.listdir(f'{path}/data/test/'):
        with open(f'{path}/data/test/{elem}', 'r') as f:
            data = json.load(f)
            df_2 = pd.DataFrame([data])
            y = model.predict(df_2)
            df.loc[len(df.index)] = [df_2.id[0], df_2.price[0], y[0]]
    df.to_csv(f'{path}/data/predictions/predictions_{datetime.now().strftime("%Y%m%d%H%M")}.csv')


if __name__ == '__main__':
    predict()
