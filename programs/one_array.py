# dabido a que a se pueden resalizar 3 tipos de ediciones a una lista (agregar, modificar o eliminar) 
# dados 2 strings, comparar si uno puede ser reasultado de un movimiento del otro (solo un movimiento)

import os


def onearray(a,b):

    dif =  len(a)-len(b)        #comparar arrays para sabe si añadio ó  elimino
    if abs(dif) >1 :
        return False
    
    if dif == 0 :               #dif es cero, no elimino ni añadio, verificar si hubo un cambio
        error = 0
        for i in range (len(a)):
            if  a[i] != b[i] :
                error += 1
            if error == 2 :
                return False
        return True
    
    if len(a) > len (b) :       # cuando a es mayor que b, se compara aceptando un solo cambio en las comparaciones
        error = 0
        for i in range (len(b)):
            if error == 0:
                n=i
            else :
                n=i+1
            print(n, a[n], b[i], i)
            if a[n] != b[i] :
                error += 1
                if error == 2 :
                    return False
                if a[i+1] != b[i]:
                    return False
        return True
    
    if len(a) < len (b) :       # cuando b es mayor que a, se compara aceptando un solo cambio en las comparaciones
        error = 0
        for i in range (len(a)):
            if error == 0:
                n=i
            else :
                n=i+1
            print(i, a[i], b[n], n)
            if a[i] != b[n] :
                error += 1
                if error == 2 :
                    return False
                if a[i] != b[i+1]:
                    return False
        return True

    
os.system("clear")
a="anastacio"
b="anastaciii"        
print(onearray(a,b))

