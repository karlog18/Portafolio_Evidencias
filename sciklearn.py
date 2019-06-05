from sklearn.linear_model import LinearRegression       #importa LinearRegression de sklearn para realizar el cálculo de los mínimos cuadrados comunes.
from sklearn.preprocessing import PolynomialFeatures    #importa PolynomialFeatures para realizar el ajuste de los datos de forma directa con sklearn
import matplotlib.pyplot as plt                         #importa matplotlib.pyplot como plt para poder hacer uso de la interzaz que muestra las gráficas.
import pandas as pd                                     #importa pandas como pd

dataset = pd.read_csv('exam_B_dataset.csv')             #realiza la lectura del dataset cuyo nombre se encuentra entre paréntesis.
X = dataset.iloc[:,:-1].values                          #selecciona los valores del dataset para X
y = dataset.iloc[:,1].values                            #selecciona los valores del dataset para y

lin_reg = LinearRegression()                            #asigna la función LinearRegression a la variable lin_reg
poly_reg = PolynomialFeatures(degree=4)                 #utilizando la función de sklearn, polynomialFeatures, se realiza el ajuste con grado 4 y se asigna a poly_reg

X_poly = poly_reg.fit_transform(X)                      #aplica el ajuste de grado 4 (en este caso) con el método fit_transform
poly_reg.fit(X_poly,y)                                  
lin_reg.fit(X_poly,y)                                   #representa una línea que ajusta mejor o entrena a todos los puntos y permite estimar otros resultados.


plt.scatter(X,y, color ='red')                          #hace una gráfica de dispersión con los valores de X y y'
plt.scatter(X,lin_reg.predict(poly_reg.fit_transform(X)), color = 'black')    #hace una gráfica de dispersión con los valores de x' y los valores que se predicen de x utilizando el método de regresión lineal de sklearn
plt.show()
