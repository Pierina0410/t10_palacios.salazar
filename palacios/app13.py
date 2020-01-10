import libreria
def universidad():
    nombre=libreria.pedir_nombre("nombre:")
    antiguedad=libreria.pedir_antiguedad("antiguedad:",1,1000)
    contenido=nombre + " " + str(antiguedad)+ " " + antiguedad
    libreria.guardar_datos("info.txt",contenido,"a")
    print("Datos guardados")
def instituto():
    nombre=libreria.pedir_nombre("nombre:")
    antiguedad=libreria.antiguedad("antigüedad:",1,1000)
    contenido=nombre + " " + str(antiguedad)+ " " + antiguedad
    libreria.guardar_datos("info.txt",contenido,"a")
    print("Datos guardados")
def verDatos():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo sin datos")
def universidad():
    opc=0
    max=3
    while(opc!=max):
        print("#########Menú universidad##############")
        print("#1.nombre de la universidad           #")
        print("#2.-antigüedad                        #")
        print("#3.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,3)
    if (opc==1):
        pedir_nombre()

    if (opc==2):
         pedir_antiguedad()
def instituto():
    opc=0
    max=3
    while(opc!=max):
        print("#########Menú instituto##############")
        print("#1.nombre del instituto          #")
        print("#2.-antigüedad                        #")
        print("#3.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,3)
    if (opc==1):
       instituto()
    if (opc==2):
         verDatos()

opc=0
max=3
while(opc!=max):
        print("#########Menú ##################")
        print("#1.-universidad                  #")
        print("#2.-instituto0                   #")
        print("#3.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,3)
        if(opc==1):
            universidad()
        if(opc==2):
            verDatos()

