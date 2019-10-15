#Detector de numeros primos
def es_primo():
    n= input("Escriba un mumero ")
    primo=True
    for i in range(2,n):
        if (n%i==0):
            primo=False
    if (primo==True):
        print "Es primo"
    else:
        print"No es primo"
es_primo() 
