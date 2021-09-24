lista = ('a', 'b', 'c', 'd', 'e','h')
 
combinaciones=[]
 
for i in range(len(lista)):
    combinaciones.append([])
 
 
for a in range(len(lista)):
    combinaciones[0].append(lista[a])
    for b in range(a+1,len(lista)):
        combinaciones[1].append(lista[a] + lista[b])
        for c in range(b+1,len(lista)):
            combinaciones[2].append(lista[a] + lista[b] + lista[c])
print(combinaciones[2])