# calcular el factorial de un numero
# funcion

def factorial(n):
    if n==0 or n==1:
        resultado=1
        
    elif n>1 :
       return n*factorial(n-1)
    
    return resultado

fac= factorial(int(input()))
print (fac)

