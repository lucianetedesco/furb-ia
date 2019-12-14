import math
import numpy as np


def calcula_distancia(featuresOrigem, featuresDestino):
    diferencas = []
    for x1, x2 in zip(featuresOrigem, featuresDestino):
        diferenca = x2 - x1
        diferencaAoQuadrado = diferenca * diferenca
        diferencas.append(diferencaAoQuadrado)
    somatorio = sum(diferencas)
    distancia = math.sqrt(somatorio)
    return distancia


def normaliza_valores(valores):
    maior = np.amax(valores)
    menor = np.amin(valores) 
    diferenca = maior - menor
    normalizados = []
    for x in valores:
        normalizado = (x-menor) / diferenca
        normalizados.append(normalizado)

    return normalizados