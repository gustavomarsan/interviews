# debido a que a se pueden resalizar 3 tipos de ediciones a una lista (agregar, modificar o eliminar)
# dados 2 strings, comparar si uno puede ser reasultado de un movimiento del otro (solo un movimiento)


def onearray(a, b):
    if abs(len(a) - len(b)) > 1:  # comparar arrays para sabe si añadio ó  elimino
        return False

    # dif es cero, no elimino ni añadio, verificar si hubo un cambio
    if len(a) - len(b) == 0:
        error = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                error += 1
                print("error number ", error)
                if error == 2:
                    return False
        return True

    if len(b) > len(a):  # dejar el string mas grande en a
        c = a
        a = b
        b = c

    # comaenzar comparacion de string con diferencia de 1 caracter
    error = 0
    for i in range(len(b)):
        n = i if error == 0 else i + 1

        if a[n] != b[i]:
            error += 1
            print("error number ", error)
            if error == 2:
                return False

    # si llego hasta aqui complio con condiciones true
    return True


print(onearray(input(), input()))
