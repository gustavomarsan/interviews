# este programa encuentra el primer numero duplicado entre una lista y un set de numeros 
import os

def firsduplicate(lista) :
    
    for num in lista :
        
        if num in setnumeros :
            return num

        else :
            setnumeros.add(num)

    return True

    
os.system("clear")

setnumeros = set()
listanumeros = [1,2,3,5,6,7,8,9,0,3]

print("First duplicate = ", firsduplicate(listanumeros))
print(listanumeros)
print(setnumeros)


