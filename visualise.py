import pandas as pd
import json

if __name__ == "__main__":
    try:
        df = pd.read_csv('data.csv')
        fig = df.plot("km", "price", kind='scatter')
        with open('coefs.json', 'r') as file:
            dict_t = json.load(file)
            t0 = dict_t.get('t0', 0)
            t1 = dict_t.get('t1', 0)
            price = t0 + t1 * df['km']
        fig.plot(df.km, price)
        fig = fig.get_figure()
        fig.savefig('vis')
    except Exception as exp:
        print('Something went wrong: ', exp)
