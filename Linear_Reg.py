import pandas as pd                                       #importa pandas como pd
from sklearn.cross_validation import train_test_split     #importa la clase train_test_split para dividir el dataset y tomar la muestra con la que se va a trabajar.
from sklearn.linear_model import LinearRegression         #importa LinearRegression de sklearn para realizar el cálculo de los mínimos cuadrados comunes.
import matplotlib.pyplot as plt                 #importa matplotlib.pyplot como plt para poder hacer uso de la interzaz que muestra las gráficas.

dataset = pd.read_csv('Salary_Data.csv')        #realiza la lectura del dataset cuyo nombre se encuentra entre paréntesis.
X = dataset.iloc[:,:-1].values                  #selecciona los valores del dataset para X
y = dataset.iloc[:,1].values                    #selecciona los valores del dataser para y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0) #inicializa los valores de todas las variables utilizando el metodo train_test_split indicando sus valores (entre paréntesis)
regressor = LinearRegression()                  #asigna la función LinearRegression a la variable regressor
regressor.fit(X_train, y_train)                 #aplica el método de ajuste en regressor teneiendo como parámetro las variables x y y' de entrenamiento

y_pred = regressor.predict(X_test)              #aplica la funcion de regresión lineal con el método predict a X_test (el valor de y)
plt.scatter(X_train, y_train, color = 'red')    #realiza una grafica de dispersión con los valores de entrenamiento de x y de y'
plt.plot(X_train, regressor.predict(X_train), color = 'blue')  #realiza una gráfica con los valores de entrenamiento de x con una línea recta para mostrar el ajuste  
plt.show()                                      #muestra en la interfaz las gráficas.
