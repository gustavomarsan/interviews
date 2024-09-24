# debido a que a se pueden resalizar 3 tipos de ediciones a una lista (agregar, modificar o eliminar)
# dados 2 strings, comparar si uno puede ser reasultado de un movimiento del otro (solo un movimiento)


def oneaway(a, b):
    diff = len(a) - len(b)

    # comparar arrays para saber si hay mas de 1 digito de diferencia y salir en caso que si
    if abs(diff) > 1:
        return False

    if len(b) > len(a):  # dejar el string mas grande en a
        c = a
        a = b
        b = c

    # comenzar comparacion de strings de igual tamaño o con diferencia
    error = 0
    for i in range(len(a)):
        # si los strings tiene diferecia de tamaño mueve apuntadores cuando encuentra el primer cambio
        
        if error == 0 or diff == 0 : 
            n = i 
        else : 
            i - 1
        
        if a[i] != b[n]:
            error += 1
            print("error number ", error)
            if error == 2:
                return False

    # si llego hasta aqui complio con condiciones true
    return True


print(oneaway(input(), input()))
