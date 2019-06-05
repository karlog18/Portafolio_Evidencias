x = [1.0,1.6,3.4,4.0,5.2] # Lista con los elementos de x
y = [1.2,2.0,2.4,3.5,3.5] # Lista con los elementos de y

def suma(x):            	# Función "suma" con x como parámetro
    sum = 0			# "sum" inicia en 0 y va incrementando con el valor de cada elemento
    for i in range(len(x)):	# ciclo for para la detener la sumatoria cuando se llegue al ultimo elemento (Length)
        sum = x[i] + sum	# incrementa el valor de "sum"
    return sum

print ("SUMATORIA DE X:", suma(x))	# Aplica la función "suma" para los diferentes valores de x (lista)
print ("SUMATORIA DE Y:", suma(y))	# Aplica la función "suma" para los diferentes valores de y (lista)

import pandas as pd			# Importa pandas como pd

def lin_reg(m,n):			# Función "lin_reg" con m y n como parámetros (x,y)

    x = pd.array(m)			# Muestra los valores de x (convertidos en array para poder realizar las operaciones directamente entre los arreglos).
    print("VALORES DE X:", x)

    y = pd.array(n)			# Muestra todos los valores (elementos) del arreglo de y
    print("VALORES DE Y:", y)

    n = len(m)				# Muestra y guarda la longitud del arreglo (necesario para su aplicación en la fórmula)
    print("LONGITUD DEL ARREGLO:",n)

    xy=x*y				# Multiplica los arreglos "x" y "y".
    print("VALORES DE X*Y:", xy)

    x2 = x*x				# Multiplica el arreglo x por sí mismo
    print("VALORES DE X^2:", x2)

    sumx2 = (suma(x)*suma(x))		# Realiza la sumatoria de los valores de x y posteriormente, la eleva al cuadrado
    print("LA SUMATORIA DE LOS VALORES DE X, ELEVADA AL CUADRADO ES:", sumx2)

    #  Opción 1 a : Numerador y denominador por separado (a)
        # numerador_a =(n*(suma(xy)))-(suma(x)*suma(y))
        # denominador_a =(n*(suma(x2)))-sumx2
        # a = numerador_a / denominador_a  #numerador_a y denominador_a aplicados en la fórmula a_nd

    #  Opción 2 a : Fórmula completa
    a = ((n*(suma(xy)))-(suma(x)*suma(y))) / ((n*(suma(x2)))-sumx2)

###########################################################################################################

    #  Opción 1 b : Numerador y denominador por separado (b)
       # numerador_b = (suma(y)*suma(x2))-(suma(xy)*suma(x))
       # denominador_b = (n*(suma(x2)))-sumx2
       # b = numerador_b / denominador_b

    #  Opción 2 b : Fórmula completa
    b = ((suma(y)*suma(x2))-(suma(xy)*suma(x))) / ((n*(suma(x2)))-sumx2)

    return a,b
 
print ("VALORES DE A Y B, RESPECTIVAMENTE:", lin_reg (x,y))
