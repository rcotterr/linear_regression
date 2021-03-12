import pandas as pd
import json


class ft_linear_regression():
    def __init__(self):
        df = pd.read_csv('data.csv')
        self.X_train, self.Y_train = df.km, df.price
        self.t0 = 0
        self.t1 = 0
        self.n_epoch = 1000
        self.lr = 0.1
        self.len = len(self.Y_train)

    def norm_data(self):
        self.min_X = min(self.X_train)
        self.max_X = max(self.X_train)
        self.min_Y = min(self.Y_train)
        self.max_Y = max(self.Y_train)
        self.X_train = (self.X_train - self.min_X) / (self.max_X - self.min_X)
        self.Y_train = (self.Y_train - self.min_Y) / (self.max_Y - self.min_Y)

    def train(self):
        for i in range(self.n_epoch):
            Y_estim = self.t0 + self.t1 * self.X_train
            tmp_t0 = self.lr * sum(Y_estim - self.Y_train) / self.len
            tmp_t1 = self.lr * sum((Y_estim - self.Y_train) * self.X_train) / self.len
            self.t0 = self.t0 - tmp_t0
            self.t1 = self.t1 - tmp_t1

    def denorm_coefs(self):
        self.t0 = self.min_Y + self.t0 * (self.max_Y - self.min_Y) - self.t1 * self.min_X * \
                    (self.max_Y - self.min_Y) / (self.max_X - self.min_X)
        self.t1 = self.t1 * (self.max_Y - self.min_Y) / (self.max_X - self.min_X)

    def save_coefs(self):
        with open('coefs.json', 'w') as file:
            json.dump({'t0': self.t0, 't1': self.t1}, file, indent=4)


if __name__ == "__main__":
    try:
        lin = ft_linear_regression()
        lin.norm_data()
        lin.train()
        lin.denorm_coefs()
        lin.save_coefs()
    except Exception as exp:
        print('Something went wrong: ', exp)