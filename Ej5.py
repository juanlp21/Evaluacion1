def fecha():
    repetir=True
    rmes=True
    while(repetir==True):
        d= input("Introduzca el dia: ")
        repetir= ((d<1) or (d>31))
        if(repetir==True):
            print("ERROR: Dia incorrecto. ")
    while(rmes==True):
        m= input("Introduzca el mes: ")
        rmes= ((m<1) or (m>12))
        if(rmes==True):
            print("ERROR: Mes incorrecto. ")
    if m==1:
        m= "Enero"
    if m==2:
        m= "Febrero"
    if m==3:
        m= "Marzo"
    if m==4:
        m= "Abril"
    if m==5:
        m= "Mayo"
    if m==6:
        m= "Junio"
    if m==7:
        m= "Julio"
    if m==8:
        m= "Agosto"
    if m==9:
        m= "Septiembre"
    if m==10:
        m= "Octubre"
    if m==11:
        m= "Noviembre"
    if m==12:
        m= "Diciembre"
    print d, m, a
fecha()
