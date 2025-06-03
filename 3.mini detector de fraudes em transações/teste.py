import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

# 1. Carregar o dataset real
file_path = 'https://www.kaggle.com/api/v1/datasets/download/mlg-ulb/creditcardfraud'  # Altere se necessário
df = pd.read_csv(file_path, encoding='ISO-8859-1')

print("Visualizando as primeiras linhas:")
print(df.head())

# 2. Análise e pré-processamento
print("\nInformações do dataset:")
print(df.info())

print("\nDistribuição das classes (0 = legítima, 1 = fraude):")
print(df['Class'].value_counts(normalize=True))

# Separar features e target
X = df.drop(['Class', 'Time'], axis=1)  # 'Time' não é relevante para o modelo
y = df['Class']

# Normalizar valores monetários e features com StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir em treino e teste com estratificação
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, stratify=y, random_state=42)

# 3. Treinamento com Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# 4. Avaliação do modelo
y_pred = model.predict(X_test)

print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred, digits=4))

# Matriz de confusão
print("Matriz de Confusão:")
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Legítima", "Fraude"])
disp.plot(cmap='Blues')
plt.title("Matriz de Confusão")
plt.show()

# 5. Importância das features
importances = model.feature_importances_
features = df.drop(['Class', 'Time'], axis=1).columns
sorted_idx = importances.argsort()[::-1]

plt.figure(figsize=(12, 6))
sns.barplot(x=importances[sorted_idx], y=features[sorted_idx])
plt.title("Importância das Features - Random Forest")
plt.xlabel("Importância")
plt.ylabel("Feature")
plt.tight_layout()
plt.show()