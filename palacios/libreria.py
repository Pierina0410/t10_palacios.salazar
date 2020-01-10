def validar_entero(n):
    if (isinstance(n, int)):
        return True
    else:
        return False

def validar_rango(n, ri, rf):
    if ( validar_entero(n) == True):
        if (n >= ri and n <= rf):
            return True
        else:
            return False
    else:
        return False

def pedir_numero(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
#fin_pedir_numero

def validar_nombre(nombre):
    if ( isinstance(nombre, str)):
        if (len(nombre) >= 3):
            return True
        else:
            return False
    else:
        return False

def pedir_nombre(msg):
    nombre=""
    while ( validar_nombre(nombre) == False ):
        nombre=input(msg)
    #fin_while
    return nombre
#fin_pedir_nombre

def guardar_datos(nombre_archivo, contenido, modo):
    archivo=open(nombre_archivo, modo)
    archivo.write(contenido)
    archivo.close()


def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido = archivo.read()
    archivo.close()
    return contenido
def validar_playas(msg):
    if(isinstance(msg,str)):
        if(msg=="pimentel"/"SanJose"/"Rocas"/"zorritos"/"mancora"):
            return True
        else:
            False
    def pedir_playa(msg):
        playa=""
        while (validar_playas==False):
            return playa

    def pedir_playa(msg):
        playa=""
        while (validar_playas==False):
            playa=input(msg)
            return playa
def validar_rio(msg):
    if(isinstance(msg,str)):
        if(msg=="SanJose"/"Rocas"/"zorritos"/"mancora"):
            return True
        else:
            False
    def pedir_rio(msg):
        rio=""
        while (validar_rio==False):
            rio=input(msg)
            return rio
#12
def validar_satelite(msg):
    if(isinstance(msg,str)):
        if(msg=="luna"/"calisto"/"sinope"/"caronte"):
            return True
        else:
                False
    def pedir_satelite(msg):
        satelite=""
        while (validar_satelite==False):
            return satelite

    def pedir_planeta(msg):
        planeta=""
        while (validar_planeta==False):
            playa=input(msg)
            return planeta
def validar_planeta(msg):
    if(isinstance(msg,str)):
        if(msg=="tierra"/"jupiter"/"marte"/"venus"):
            return True
        else:
            False
    def pedir_rio(msg):
        rio=""
        while (validar_planeta==False):
            rio=input(msg)
            return rio
#13
def pedir_nombre(msg):
    nombre=""
    while (validar_nombre(nombre,str)==False):
        nombre=input(msg)
        return True
    else:
        False
def pedir_antiguedad(msg,ri,rf):
    nombre=""
    while (validar_antiguedad(n,ri,rf)==False):
        n=input(msg)
        if(n.isdigit()==True):
            n=int(n)
        return True
    else:
        False



