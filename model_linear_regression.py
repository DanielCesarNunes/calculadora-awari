import pickle as pk
import pandas as pd


class LinearRegression:
    def __init__(self):
        self.model_pipe = pk.load(open('linear_regression_pipe_calculadora.pkl','rb'))

    def predict(self, df):
        return self.model_pipe.predict(df)


