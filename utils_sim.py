
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# def correr_simulacion(estado, p1, p2, num_pasos):
#     """Simular el número dado de pasos de tiempo.
    
#     state: objeto State
#     p1: probabilidad de llegada de un cliente a Robledo->C4TA
#     p2: probabilidad de llegada de un cliente a C4TA->Robledo
#     num_pass: número de pasos de tiempo
#     """
#     results = TimeSeries()
#     results[0] = estado.robledo
    
#     for i in range(num_pasos):
#         paso(estado, p1, p2)
#         results[i+1] = estado.robledo
        
#     results.plot(label='Robledo')
#     decorar(title='Sistema de Bicicletas Compartidas Robledo-C4TA',
#              xlabel='Paso de tiempo (min)', 
#              ylabel='Número de bicicletas')
    
def paso(estado, p1, p2):
    """Simular un paso de tiempo.
    
    state: objeto State del sistema de bicicletas compartidas
    p1: probabilidad de un viaje Robledo->C4TA
    p2: probabilidad de un viaje C4TA->Robledo
    """
    if lanzamiento(p1):
        bicicleta_a_c4ta(estado)
    
    if lanzamiento(p2):
        bicicleta_a_robledo(estado)


def bicicleta_a_robledo(estado):
    """Mover una bicicleta de C4TA a Robledo.
    
    state: objeto State del sistema de bicicletas compartidas
    """
    if estado.c4ta == 0:
        estado.c4ta_vacia += 1
        return
    estado.c4ta -= 1
    estado.robledo += 1


def bicicleta_a_c4ta(estado):
    """Mover una bicicleta de Robledo a C4TA.
    
    state: objeto State del sistema de bicicletas compartidas

    """
    if estado.robledo == 0:
        estado.robledo_vacia += 1
        return
    estado.robledo -= 1
    estado.c4ta += 1

def lanzamiento(p=0.5):
    """Lanza una moneda con la probabilidad dada.

    Args:
        p (float): Probabilidad entre 0 y 1.

    Returns:
        bool: True o False.
    """
    return np.random.random() < p

def TimeSeries(*args, **kwargs):
    """Crear un objeto pd.Series para representar una serie temporal.

    Args:
        *args: Argumentos pasados a pd.Series.
        **kwargs: Argumentos con nombre pasados a pd.Series.

    Returns:
        pd.Series: Serie con nombre de índice 'Time' y nombre 'Quantity'.
    """
    if args or kwargs:
        underride(kwargs, dtype=float)
        series = pd.Series(*args, **kwargs)
    else:
        series = pd.Series([], dtype=float)

    series.index.name = "Time"
    if "name" not in kwargs:
        series.name = "Quantity"
    return series

def underride(d, **options):
    """Agregar pares clave-valor a d solo si la clave no está en d.

    Si d es None, crear un nuevo diccionario.

    Args:
        d (dict): Diccionario a actualizar.
        **options: Argumentos con nombre para agregar a d.

    Returns:
        dict: Diccionario actualizado.
    """
    if d is None:
        d = {}

    for key, val in options.items():
        d.setdefault(key, val)

    return d

def decorar(**options):
    """Decora los ejes actuales.

    Llama a decorar con argumentos con nombre, por ejemplo:
    decorar(title='Título',
                xlabel='x',
                ylabel='y')

    Los argumentos con nombre pueden ser cualquiera de las propiedades de los ejes:
    https://matplotlib.org/api/axes_api.html

    Args:
        **options: Argumentos con nombre para las propiedades de los ejes.
    """
    ax = plt.gca()
    ax.set(**options)

    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(handles, labels)

    plt.tight_layout()

def Estado(**variables):
    """Contiene los valores de las variables de estado.

    Args:
        **variables: Argumentos con nombre para almacenar como variables de estado.

    Returns:
        pd.Series: Serie con las variables de estado.
    """
    return pd.Series(variables, name="state")