#Multiplicación
def ejercicio1():
    print "Escriba multiplicación"
    producto=0
    while(producto==0):
        print "Escriba los números a multiplicar"
        a=input ("Escriba primera variable ")
        b=input ("Escriba segunda variable ")
        c=input ("Escriba tercera variable ")
        d=input ("Escriba cuarta variable ")
        producto= a*b*c*d
        if (producto==0):
            print "Reintroduzca datos "
        else:
            print producto
ejercicio1()
