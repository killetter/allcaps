import random 
from math import floor, ceil 
Lista = ["Andrea", "Pepino", "Constanza", "Tam", "Miguel",]
letras = ["b", "E", "e", "H", "I","i", "l", "n", "O", "ó", "P", "q", "T", "v",]
participantes = random.sample(Lista, k=len(Lista))
randomLetras = random.sample(letras, k=len(letras))
if len(Lista) <= len(letras):
    divisionLetras = ceil(len(letras)/len(Lista))
else:
    divisionLetras = floor(len(letras)/len(Lista))
indiceInicial = 0

for indice, turno in enumerate(participantes):
    teTocan = []
    try:
        for index  in range(divisionLetras):
            teTocan.append(randomLetras[index+indiceInicial]) 
        indiceInicial += divisionLetras
    except IndexError:
        for index  in range(0):
            teTocan.append(randomLetras[index+indiceInicial])
    print(f'{indice+1} - {turno} {teTocan}')

