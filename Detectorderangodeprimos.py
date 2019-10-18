#Detector en un rango de numeros primos
def rangoprimos():
    n= input("Escriba desde que numero ")
    m= input("Escriba hasta que numero ")
    primo=True
    for i in range(n,m+1):
        for a in range(2,i):
            if (i%a==0):
                primo=False
        if (primo==True):
            print i,"Es primo"
        else:
            print i,"No es primo"
            primo=True
rangoprimos() 
