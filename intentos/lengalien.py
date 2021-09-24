abecedario = "abcdefghijklmnopqrstuvwxyz"
diccionario = []
l = 3 #cantidad de letras
d = 5 #cantidad de filas por cada conjunto de letras
n = 0 #cantidad de casos 
new_abecedario = abecedario[0:l+1]
fila = 1
while fila <= d:
    fila+=1
    palabra = ''
    for letra in new_abecedario:
        le = letra
        palabra +=le
        if palabra in diccionario:
            print('hola')
            


u = 1
pru = 25
dig = 0
inc = -1
while u <= pru:
    u+=1
    dig = dig + inc
    if dig == (len(new_abecedario) * -1 or dig < len(new_abecedario) * -1):
        inc = inc * 1
    elif dig == len(new_abecedario) or dig > len(new_abecedario):
        inc = inc * -1
    print(dig)
   
    
    



        




    


