def IVA():
    x=True
    i= float(input("Introduzca un precio:"))
    while x==True:
        tipo= input("Introduzca el tipo: ")
        tipos= "reducido" and "general" and "superreducido"
        if tipo==tipos:
            x=False
            if tipo=="reducido":
                print (i*1.07," euros")
            if tipo=="general":
                print (i*1.16," euros")
            if tipo=="superreducido":
                print (i*1.04," euros")
        else:
            x=True
    
IVA()
