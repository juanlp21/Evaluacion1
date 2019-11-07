def salario():
    x= int(input("Introduzca horas trabajadas: "))
    if (x<40):
        print (x*30)
    else:
        y= x-40
        z= 40*30
        print (z+(y*45))
salario()
