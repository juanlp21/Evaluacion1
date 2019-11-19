def piramide2():
    filas= input("Introduzca la altura en pisos: ")
    espacios=' '
    asteriscos='*'
    for i in range(filas):
        for nespacios in range (filas-i-1):
            espacios=espacios+' '
        for nasteriscos in range (2*i+1):
            asteriscos=asteriscos+'*'
        print espacios + asteriscos
        espacios=' '
        asteriscos='*'
piramide2()
