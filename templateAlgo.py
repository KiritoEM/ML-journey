# Régression linéaire 
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

coefficient = model.coef_
intercept = model.intercept_

# K-Nearest Neighbors (KNN) 
from sklearn.neighbors import KNeighborsRegressor  # ou KNeighborsClassifier pour classification

model = KNeighborsRegressor(n_neighbors=k)  # Utiliser KNeighborsClassifier pour classification

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
