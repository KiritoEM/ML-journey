from sklearn.neighbors import KNeighborsClassifier  # ou KNeighborsRegressor pour la regression
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd
import numpy as numpy
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv('nom_fichier_csv.csv')

X = df[['Age', 'Income']] 
y = df[['Subscription']] # étiquette

encoder = LabelEncoder()
y = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=3) # 3 voisins

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse:.2f}")