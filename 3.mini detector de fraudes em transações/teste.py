import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score

#importar arquivos
path = os.path.expanduser('~/Downloads/archive/creditcard.csv')
df=pd.read_csv(path)

df.info()