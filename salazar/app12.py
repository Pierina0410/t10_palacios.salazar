import libreria
def pedir_nota1():
    libreria.pedir_numero("ingrese nota 1:")
    print("Se agrego nota 1")
def pedir_nota2():
    print("Se agrego nota 2")
def pedir_nota3():
    print("Se agrego nota 3")

def pedir_promedio1():
    print("Se agrego promedio 1")
def pedir_promedio2():
    print("Se agrego promedio 2")
def pedir_promedio3():
    print("Se agrego promedio 3")

def agregar_nota():
    opc=0
    max=4
    while (opc!=max):
        print("# sub-menu- AGREGAR NOTA #")
        print("# 1. NOTA --> 11         #")
        print("# 2. NOTA --> 14         #")
        print("# 3. NOTA --> 16         #")
        print("# 4. SALIR               #")
        print("##########################")
        opc=libreria.pedir_numero("Ingrese opcion de nota:", 1,4)
    if (opc==1):
        pedir_nota1
    if (opc==2):
        pedir_nota2
    if (opc==3):
        pedir_nota3

def agregar_promedio():
    opc=0
    max=4
    while (opc!=max):
        print("# sub-menu-AGREGAR PROMEDIO #")
        print("# 1. Promedio -> 12         #")
        print("# 2. promedio -> 14         #")
        print("# 3. promedio -> 17         #")
        print("# 4. Salir                  #")
        print("#############################")
        opc=libreria.pedir_numero("Ingrese opcion de promedio: ", 1,4)
    if (opc==1):
        pedir_promedio1()
    if (opc==2):
        pedir_promedio2()
    if (opc==3):
        pedir_promedio3()

opc=0
max=3
while(opc!=3):
    print("######### MENU ##########")
    print("# 1. agregar nota:      #")
    print("# 2. promedio           #")
    print("# 3. sali               #")
    print("#########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_nota()
    if(opc==2):
        agregar_promedio()

print("fin del programa")
# fin de menu
