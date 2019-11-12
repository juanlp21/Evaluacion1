def piramide():
    filas= int(input("Introduzca filas: "))
    for i in range(filas):
        espacios=' '*(filas-i-1)
        asteriscos='*'*(2*i+1)
        print  espacios + asteriscos

piramide()
