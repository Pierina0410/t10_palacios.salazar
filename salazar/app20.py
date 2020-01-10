import libreria
def pedir_nota1():
    print("Se agrego nota 1")
def pedir_nota2():
    print("Se agrego nota 2")
def pedir_nota3():
    print("Se agrego nota 3")
def pedir_nota4():
    print("Se agrego nota 4")
def pedir_prom1():
    print("Se agrego promedio 1")
def pedir_prom2():
    print("Se agrego promedio 2")
def pedir_prom3():
    print("Se agrego promedio 3")
def pedir_prom4():
    print("Se agrego promedio 4")
#fin_def

def agregar_nota():
    opc=0
    max=5
    while(opc!=max):
        print("#####  Nota  #####")
        print("#1. NOTA 11      #")
        print("#2. NOTA 17      #")
        print("#3. NOTA 13      #")
        print("#4. NOTA 19      #")
        print("#5. Salir        #")
        print("##################")
        opc=libreria.pedir_numero("Ingrese nota: ",1,5)

        #Mapeo
        if(opc==1):
            pedir_nota1()
        if(opc==2):
            pedir_nota2()
        if(opc==3):
            pedir_nota3()
        if(opc==4):
            pedir_nota4()

def agregar_promedio():
    opc=0
    max=5
    while(opc!=max):
        print("#### Sub-Menu  ####")
        print("#1. prom: 12      #")
        print("#3. prom: 14      #")
        print("#3. prom: 16      #")
        print("#4. prom: 18      #")
        print("#5. Salir         #")
        print("##################")
        opc=libreria.pedir_numero("Ingrese promedio: ",1,5)
#fin_while

        #Mapeo
        if(opc==1):
            pedir_prom1()
        if(opc==2):
            pedir_prom2()
        if(opc==3):
            pedir_prom3()
        if(opc==4):
            pedir_prom4()

opc=0
max=3
while(opc!=3):
    print("######### MENU ##########")
    print("# 1.agregar nota:       #")
    print("# 2.promedio            #")
    print("# salir                 #")
    print("#########################")
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
#FIN_WHILE

    #MAPPEO
    if(opc==1):
        agregar_nota()
    if(opc==2):
        agregar_promedio()

print("fin del programa")
# fin de menu
