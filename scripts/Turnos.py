import random 
Lista= ["Andrea", "Pepino", "Constanza",]

participantes=random.sample(Lista, k=len(Lista))
x=0
for indice, turno in enumerate(participantes):
    x+=1
    print(f'{indice+1}-{turno}')
