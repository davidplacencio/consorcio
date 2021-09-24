"""" ESTE FRAGMENTO DE CODIGO ESTA COMENTADO PARA FACILITAR LAS PRUEBAS 
conf = input('ingrese configuración: ')
conf = conf.split()

l = int(conf[0])
d = int(conf[1])
n = int(conf[2])
"""

def validarParentesis(cadena): #este metodo se encarga de validar que si se abre un parentesis, también se cierre
    count = 0
    for i in cadena:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0

def separadorParentesis(cadena): #este metodo se encarga de transformar todos los parentsis en espacios, para poder separar los caractares dentro del parentesis
    parente = "()"
    news = ''
    for x in cadena:
        if x == '(' or x == ')':
           x = " "
        news = news + x
    return news

def crearConjuntos(d,l): #este metodo se encarga de validar y crear el conjunto de letras ingresadas por pantalla
    conjuntos=[]
    letras=[]
    i=1
    while i <= int(d):
        j=1
        conjunto=''
        flag = True
        while j <= int(l):
            while flag:
                conjunto = input('ingrese conjunto de letras: ')
                if len(conjunto) > l:
                    print('estas ingresando un numero de letras mayor al acordado')
                elif len(conjunto) < l:
                    print('estas ingresando un numero de letras menor al acordado')
                else:
                    if conjunto in conjuntos:
                        print('este conjunto ya fue ingresado con anterioridad')
                    else:
                        flag = False
                        print('El conjunto ',conjunto,' fue ingresado correctamente')    
            j +=1
        conjuntos.append(conjunto)   
        i+=1
    return(conjuntos)

def crearPruebas(n): #este metodo se encarga de validar y crear las pruebas ingresadas por pantalla
    pruebas = []
    i = 1
    while i <= n:
        flag = True
        while flag:
            prueba = input('ingrese casos de prueba, si desea aumentar la probabilidad de encontra una coincidencia ingrese mas de un caracter entre parentesis ejemplo: (ab)(dc)(bc): \n')
            for h in prueba:
                if h == '(' or h == ')':
                    if validarParentesis(prueba) == False:
                        print('No estas cerrando los parentesis correctamente')
                        prueba = ""
                    else:
                        prueba = separadorParentesis(prueba)
            if len(prueba) > 0:
                flag = False
                pruebas.append(prueba)
            else:
                print('Dato Invalido') 
        i+=1
    return pruebas

def crearCombinaciones(lst): #este metodo es un intento fallido de intentar realizar combinaciones 
    lista = lst
 
    combinaciones=[]
 
    for i in range(len(lista)):
        combinaciones.append([])
 
    for a in range(len(lista)):
        combinaciones[0].append(lista[a])
        for b in range(a+1,len(lista)):
            combinaciones[1].append(lista[a] + lista[b])
            for c in range(b+1,len(lista)):
                combinaciones[2].append(lista[a] + lista[b] + lista[c])
    return combinaciones[2]

def ejecutarCasos(): #este metodo se encarga de ejecutar el algoritmo
    conjuntos = ['adc','dbc','abc','dca'] # datos de prueba solo estan a para evitar digitar los datos de entrada una y otra vez mientras se hacen pruebas
    pruebas = [' ad dc ab ', 'adc', 'dbc',' xzy abc ', ' abc dbc bbc ']
    resultados = dict()
    numprueba = 0
    indice = 0

    for i in pruebas:  
        print('PRUEBA NUMERO: ',numprueba)
        numprueba += 1
        lst = []
        resultados[numprueba] = 0
        testeo = i.split()
        print(testeo)

        if len(testeo) > 1 :  #esta sección falta completarla, tuve varias ideas pero me quede sin tiempo. no alcance a hacer un algoritmo de combinaciones y permutaciones
            for i in testeo: #el bucle for separa cada caracter del conjunto de pruebas para poder tratar cada letra por separado (idea incompleta)
                for k in i.split():
                    lst.clear()
                    for o in range(len(k)):
                        lst.append(k[o])
                    print('COMPARA',lst)
        else:
            for k in conjuntos: #aquí se ahce una comparacíon básica de las cadenas de texto que no contienen parentesis
                if i == k:
                    print(numprueba, 'soy igual al: ', k)
                    resultados[numprueba] = resultados.get(numprueba, 0) + 1 #aquí se agregan los resultados de las pruebas a un diccionario que va almacenando las coincidencias
    print(resultados)
         
ejecutarCasos()