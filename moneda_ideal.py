# espacio muestral: {escudo, corona}
# cada tirada dentro de la secuencia es independiente
# probabilidad es igual para ambas
# E = 0.5, C = 0.5
# N = 10
# 1. Se utiliza la distribución geométrica ya que
#    X = número de ensayos para un éxito
#    ensayo = veces que se debe tirar la moneda
#    éxito = obtener corona

import numpy as np
import matplotlib.pyplot as plt



# probabilidad de éxito (Obtener corona)
p = 0.5

# Muestra un gráfico de bastones para una función de masa
# entradas: conjunto de valores de X, conjunto de valores de fmp(X)
# salidas: Muestra el gráfico respecto a la información dada

def grafico_pmf(n, pmf):
    ns = []
    for i in range(n):
        ns += [i]

    ns += [n]
    x = ns
    y = pmf
    fig, ax = plt.subplots()
    ax.stem(x,y)
    plt.title('Gráfica de la función de masa de probabilidad')
    plt.xlabel('Ensayo')
    plt.ylabel('Probabilidad de éxito')
    plt.show()



def moneda_ideal():
    # parámetros de la distribución
    # número de ensayos (tiros de moneda):
    n = 10
    # probabilidad de éxito (obtener corona):
    p = 0.7

    # se utiliza la función np.random.binomial de numpy, la cual
    # genera una secuencia de 1000 numeros que pertenecen a la distribución binomial

    # función: np.random.binomial
    # entrada: número de ensayos, probabilidad de éxito, cantidad de números generados
    # salida: array de los números obtenidos
    samples = np.random.geometric(p, size=1000)


    # función: np.bincount
    # entrada: números resultados de la distribución binomial
    # salida: numero de ocurrencias de cada valor en la secuencia
    ocurrencias = np.bincount(samples, minlength=n+1)

    # Normaliza las ocurrencias para obtener la funcion masa probablidad
    pmf = ocurrencias / len(samples)

    
    # PMF:
    print("PMF de la distribución binomial para la moneda truco con n={}, p={}: \n{}".format(n, p, pmf))
    print(pmf)

    grafico_pmf(n, pmf)



moneda_ideal()
