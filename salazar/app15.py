import libreria
def pedir_depa1():
    print("Se ingreso Lambayeque")
def pedir_depa2():
    print("Se ingreso Piura")
def pedir_depa3():
    print("Se ingreso Tumbes")
def pedir_depa4():
    print("Se ingreso Lima")

def pedir_capi1():
    print("Se ingreso chiclayo")
def pedir_capi2():
    print("Se ingreso Reque")
def pedir_capi3():
    print("Se ingreso oyotub")
def pedir_capi4():
    print("Se ingreso chosica")

def agregar_departamento():
    opc=0
    max=5
    while(opc!=max):
        print("## SUB-MENU-DEPARTAMENTO ##")
        print("#1. Lambayeque            #")
        print("#2. Piura                 #")
        print("#3. Tumbes                #")
        print("#4. Lima                  #")
        print("#5. Salir                 #")
        print("###########################")
        opc=libreria.pedir_numero("Ingrese opcion de departamento:",1,5)
    if (opc==1):
        pedir_depa1()
    if (opc==2):
        pedir_depa2()
    if (opc==3):
        pedir_depa3()
    if (opc==4):
        pedir_depa4()

def agregar_capital():
    opc=0
    max=5
    while(opc!=max):
        print("## SUB-MENU-CAPITAL ##")
        print("#1. Chiclayo         #")
        print("#2. Reque            #")
        print("#3. Oyotun           #")
        print("#4. chosica          #")
        print("#5. Salir            #")
        print("######################")
        opc=libreria.pedir_numero("Ingrese opcion de capital:",1,5)

        if (opc==1):
            pedir_capi1()
        if (opc==2):
            pedir_capi2()
        if (opc==3):
            pedir_capi3()
        if (opc==4):
            pedir_capi4()

opc=0
max=3
while(opc!=max):
    print("########### MENU #############")
    print("# 1. Departamento            #")
    print("# 2. Capital de departamento #")
    print("# 3. salir                   #")
    print("##############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_departamento()
    if(opc==2):
        agregar_capital()

print("Programa finalizado")
# fin de menu
