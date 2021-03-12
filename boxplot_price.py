import pandas as pd
import json

if __name__ == "__main__":
    try:
        df = pd.read_csv('data.csv')
        fig = df.boxplot(column=['price'])
        fig = fig.get_figure()
        fig.savefig('boxplot_price')
    except Exception as exp:
        print('Something went wrong: ', exp)
