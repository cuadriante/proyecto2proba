# espacio muestral: {escudo, corona}
# cada tirada dentro de la secuencia es independiente
# probabilidad NO es igual para ambas
# E = 0.7, C = 0.3
# N = 10
# 1. Se utiliza la distribución binomial ya que
#    X = número de éxitos en n ensayos
#    ensayo = tirar la moneda
#    éxito = obtener corona
#    n = 10

import numpy as np
import matplotlib.pyplot as plt



# Muestra un gráfico de bastones para una función de masa
# entradas: conjunto de valores de X, conjunto de valores de fmp(X)
# salidas: Muestra el gráfico respecto a la información dada

def grafico_pmf(n, pmf):
    ns = []
    for i in range(n):
        print(i)
        ns += [i]

    ns += [n]
    x = ns
    y = pmf
    fig, ax = plt.subplots()
    ax.stem(x,y)
    plt.title('Gráfica de la función de masa de probabilidad')
    plt.xlabel('Éxitos')
    plt.ylabel('Probabilidad en 10 ensayos')
    plt.show()



def moneda_truco():
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
    samples = np.random.binomial(n, p, size=1000)


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

moneda_truco()
