import pandas as pd
from sklearn import svm
    
class Train:
    
    def __init__():
        x = 0

    def t():
        dframe = pd.read_csv("pong_data.csv")

        x = dframe.drop(columns=['paddle_y'])
        y = dframe['paddle_y']

        # ridge regression method

        model = svm.SVR()
        model.fit(x, y)

        from joblib import dump, load 
        dump(model, 'mymodel.joblib') #save

        return x