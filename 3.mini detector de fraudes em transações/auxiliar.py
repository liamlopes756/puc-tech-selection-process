#importar bibliotecas
#!pip install pandas
#!pip install sklearn
import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score

#importar arquivos
path = os.path.expanduser('~/Downloads/creditcard.csv')
df=pd.read_csv(path)

#

display(df.head())
display(df.tail())
display(df.info())
display(df.describe())

#verifica valores nulos
df.isnull().sum()

#verificando fraudes

df_fraudes=df.Amount[df.Class==1]

df_fraudes.describe()

#verificando as nao fraudes

df_nao_fraudes=df.Amount[df.Class==0]

display(df_nao_fraudes.describe())
display(df_nao_fraudes)

print("Class 1 fraude \nClass 0 nao fraude")
df.Class.value_counts()

#cria novos datasets

df_lista_nao_fraude=df[df.Class==0]
df_lista_fraude=df[df.Class==1]

#cria um data frame para balancear as nao fraudes
#sample pega x linhas de forma aleatoria

df_lista_nao_fraude_treino=df_lista_nao_fraude.sample(n=492)
df_lista_nao_fraude_treino

#concatenar os dois dataframes de fraude e nao fraude balanceados

df_balanc=pd.concat([df_lista_nao_fraude_treino,df_lista_fraude],axis=0)  #0=rows
display(df_balanc)

#ajustar index

df_balanc.reset_index(inplace=True)
df_balanc

#retirada de dados para validação

df_val_nao_fraude=df_balanc.head(5)
df_val_fraude=df_balanc.tail(5)

display(pd.concat([df_val_nao_fraude,df_val_fraude],axis=0))

#retirando linhas usadas para a validação

df_balanc=df_balanc.iloc[5:]
df_balanc=df_balanc.iloc[:-5]

display(df_balanc)

#concatenar o dataframe de validação

df_val_total=pd.concat([df_val_fraude,df_val_nao_fraude])

df_val_total.reset_index(inplace=True)
df_val_total_real=df_val_total.Class

df_val_total=df_val_total.drop(['Time','Class','index','level_0'],axis=1)

df_val_total

#verificando a distribuiçao dos dados

df_balanc.Class.value_counts()

#definindo features e labels

X=df_balanc.drop(['Time','Class','index'],axis=1)
Y=df_balanc['Class']

print(X,Y)

#separar entre dados de treino e dados de teste

X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y) #20% pra teste e 80% pra treino

#treinamento

lr = LogisticRegression(max_iter=1000)

lr.fit(X_train,Y_train)
pred =  lr.predict(X_test)

acc = accuracy_score(Y_test, pred)

print(acc*100)

#validação

pred = lr.predict(df_val_total)

df_val_final=pd.DataFrame({'real': df_val_total_real,'previsao':pred})

df_val_final

