# debido a que a se pueden resalizar 3 tipos de ediciones a una lista (agregar, modificar o eliminar) 
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
                print("error numero ",error)
                if error == 2 :
                    return False
        return True
    


    if len(b) > len (a) :       # dejar el string mas grande en a
        print(a,b)
        c=a
        a=b
        b=c
        print(a,b)
    

    # comaenzar comparacion de string con diferencia de 1 caracter
    error = 0
    for i in range (len(b)):
        if error == 0:
            n=i
        else :
            n=i+1
        
        if a[n] != b[i] :
            error += 1
            print("error number ",error)
            if error == 2 :
                return False
    
    #si llego hastaqui complio con condiciones true
    return True



os.system("clear")
a="anastacio"
b="anastac"        
print(onearray(a,b))

