from ctr_cuenta import CtrCuenta
from mod_cuenta import ModCuenta
from funciones import menu
from ctr_grupo import CtrGrupo
from colorama import Fore, init
init(autoreset=True)
import os
ctr = CtrCuenta()
ctrg = CtrGrupo()
def insertar(rango):
    for i in range(int(rango)):
        while True:
            try:
                codigo = input('Ingrese el codigo: ')
            except ValueError:
                continue
            if (codigo.isalpha()):
                print(Fore.RED + "Debes escribir un codigo valido")
                continue
            if not(codigo != ''):
                print(Fore.RED + "Debes escribir un codigo valido")
                continue
            if (ctr.veriCod(codigo)):
                print(Fore.RED +'Error: ya existe el codigo Ingresado, por favor escriba un codigo nuevo')
            else:
                break
        while True:
            try:
                print(Fore.BLUE + " <<< Verifique el grupo >>>")
                from int_grupo import busq
                busq()
                grupo = int(input('Ingrese el grupo: '))
            except ValueError:
                print(Fore.RED + "Debes escribir el grupo correcto")
                continue
            if grupo < 0:
                print(Fore.RED + "Debes escribir numero positivo")
                continue
            if not(ctrg.verifi(grupo)):
                print(Fore.RED +'Error: No existe el codigo del Grupo ingresado, por favor escriba un codigo valido')
            else:
                break
        while True:
            try:
                descripcion = input('Ingrese la descripcion: ')
            except ValueError:
                continue
            if not(descripcion.isalpha()):
                print(Fore.RED + "Debes escribir una descripcion valida")
                continue
            else:
                break
        while True:
            try:
                naturaleza = input('Ingrese la naturaleza(A-D): ')
            except ValueError: 
                continue
            if not(naturaleza.isalpha()):
                print(Fore.RED + "Debes escribir una naturaleza valida (A-D) Ejem: D=Deudora, A=Acredora")
                continue
            if not(naturaleza == 'A' or naturaleza == 'D' or naturaleza == 'a' or naturaleza == 'd'):
                print(Fore.RED + "Debes escribir una naturaleza valida (A-D) Ejem: D=Deudora, A=Acredora")
                continue
            else:
                break
        
        while True:
            try:
                estado = int(input('Ingrese el estado (1-0) Ejem: 0=False,  1= True: '))
            except ValueError:
                print(Fore.RED + "Debes escribir el estado correcto (1-0) Ejem: 0=False,  1= True")
                continue
            if not(estado >= 0 and estado < 2):
                print(Fore.RED + "Debes escribir el estado correcto (1-0) Ejem: 0=False,  1= True")
                continue
            else:
                break
        cli = ModCuenta(cod=codigo,idgrup=grupo,descrip=descripcion.capitalize(),natur=naturaleza.upper(),estad=estado)
        answer=input(f"Estas seguro que desea guardar el Plan de Cuenta con codigo:{codigo}, grupo:{grupo}, descripcion:{descripcion}, naturaleza:{naturaleza}, estado:{estado}? [y/n]: ")
        if not answer or answer[0].lower() != 'y':
            input('Presione una tecla para continuar')
            ejecutar_cuenta()
        else:
            if ctr.ingresar(cli):
                print(Fore.YELLOW + 'Registro grabado correctamente')
                
            else:
                print(Fore.RED + 'Error al grabar el registro')

def modificar():
    while True:
        try:
            cuenta = int(input('Ingrese el id de la cuenta: '))
        except ValueError:
            print(Fore.RED + "Debes escribir un codigo valido")
            continue
        if cuenta < 0:
            print(Fore.RED + "Debes escribir numero positivo")
            continue
        if not(ctr.verifi(cuenta)):
            print(Fore.RED +'Error: No existe el id Ingresado, por favor escriba un id valido')
        else:       
            break
    while True:
        try:
            codigo = input('Ingrese el codigo : ')
        except ValueError:
            continue
        if (codigo.isalpha()):
            print(Fore.RED + "Debes escribir un codigo valido")
            continue
        if not(codigo != ''):
            print(Fore.RED + "Debes escribir un codigo valido")
            continue
        if (ctr.veriCod(codigo)):
            print(Fore.RED +'Error: ya existe el codigo Ingresado, por favor escriba un codigo nuevo')
        else:
            break
    while True:
        try:
            print(Fore.BLUE + " <<< Verifique el grupo >>> ")
            from int_grupo import busq
            busq()
            grupo = int(input('Ingrese el grupo: '))
        except ValueError:
            print(Fore.RED + "Debes escribir el grupo correcto")
            continue
        if grupo < 0:
            print(Fore.RED + "Debes escribir numero positivo")
            continue
        if not(ctrg.verifi(grupo)):
            print(Fore.RED +'Error: No existe el codigo del Grupo ingresado, por favor escriba un codigo valido')
        else:
            break
    while True:
        try:
            descripcion = input('Ingrese la descripcion : ')
        except ValueError:
            continue
        if not(descripcion.isalpha()):
            print(Fore.RED + "Debes escribir una descripcion valida")
            continue
        else:
            break
        
    while True:
        try:
            naturaleza = input('Ingrese la naturaleza(A-D) : ')
        except ValueError:
            continue
        if not(naturaleza.isalpha()):
            print(Fore.RED + "Debes escribir una naturaleza valida (A-D) Ejem: D=Deudora, A=Acredora")
            continue
        if not(naturaleza == 'A' or naturaleza == 'D' or naturaleza == 'a' or naturaleza == 'd'):
            print(Fore.RED + "Debes escribir una naturaleza valida (A-D) Ejem: D=Deudora, A=Acredora")
            continue
        else:
            break
        
    while True:
        try:
            estado = int(input('Ingrese el estado (1-0) Ejem: 0=False,  1= True: '))
        except ValueError:
            print(Fore.RED + "Debes escribir el estado correcto (1-0) Ejem: 0=False,  1= True")
            continue
        if not(estado >= 0 and estado < 2):
            print(Fore.RED + "Debes escribir el estado correcto (1-0) Ejem: 0=False,  1= True")
            continue
        else:
            break
    
    cli = ModCuenta(_id=cuenta,cod=codigo,idgrup=grupo,descrip=descripcion.capitalize(),natur=naturaleza.upper(),estad=estado)
    answer=input(f"¿Estas seguro que desea guardar la modificacion el Plan de Cuenta con id:{cuenta}, codigo:{codigo}, grupo:{grupo}, descripcion:{descripcion}, naturaleza:{naturaleza}, estado:{estado}?  [y/n]: ")
    if not answer or answer[0].lower() != 'y':
        input('Presione una tecla para continuar')
        ejecutar_cuenta()
    else:
        if ctr.modificar(cli):
            print(Fore.YELLOW + 'Registro modificado correctamente')
        else:
            print(Fore.RED + 'Error al modificar el registro')

def eliminar():
    while True:
        try:
            cuenta = int(input('Ingrese codigo: '))
        except ValueError:
            print(Fore.RED + "Debes escribir un codigo valido")
            continue
        if cuenta < 0:
            print(Fore.RED + "Debes escribir numero positivo")
            continue
        if not(ctr.verifi(cuenta)):
            print(Fore.RED +'Error: No existe el id Ingresado, por favor escriba un id valido')
        else:
            break
    cli =  ModCuenta(_id=cuenta)
    answer=input(f"¿Estas seguro que desea eliminar el Plan de Cuenta: {cuenta}? [y/n]: ")
    if not answer or answer[0].lower() != 'y':
        input('Presione una tecla para continuar')
        ejecutar_cuenta()
    else:
        if ctr.eliminar(cli):
            print(Fore.YELLOW + 'Registro eliminado correctamente')
        else:
            print(Fore.RED + 'Error al eliminar el registro')
        

def consultar():
    buscar = input('Ingrese la descripcion a buscar: ')
    cli = ctr.consulta(buscar)
    print(Fore.BLUE + "                 <<< Listado Plan de Cuenta >>>>          ")
    print(Fore.WHITE + '--------------------------------------------------------------------------')
    print(Fore.BLUE + '  Id    Codigo     grupo        Descripcion       Naturaleza       Estado ')
    print(Fore.WHITE + '--------------------------------------------------------------------------')
    for registro in cli:
        print('{0:3}      {1:7} {2:4}\t\t {3:11}        {4:15}{5:45}'.format(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5]))
    print(Fore.WHITE + '--------------------------------------------------------------------------')

def busq():
    buscar = ''
    cli = ctr.consulta(buscar)
    print(Fore.BLUE + "                 <<< Listado Plan de Cuenta >>>>          ")
    print(Fore.WHITE + '--------------------------------------------------------------------------')
    print(Fore.BLUE + '  Id    Codigo     grupo        Descripcion       Naturaleza       Estado ')
    print(Fore.WHITE + '--------------------------------------------------------------------------')
    for registro in cli:
        print('{0:3}      {1:7} {2:4}\t\t {3:11}        {4:15}{5:45}'.format(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5]))
    print(Fore.WHITE + '--------------------------------------------------------------------------')

def ejecutar_cuenta():
    opc = ''
    os.system('cls||clear')
    while True:
        os.system('cls||clear')
        opc =  str(menu(
            ['Ingresar', 'Mostrar' ,'Modificar', 'Eliminar', 'Retornar Menu Principal'],
            Fore.GREEN + 'MENU PLAN DE CUENTA'))
        if opc == '0':
            os.system('cls||clear')
            print(Fore.GREEN + '\n<<<Insertar datos>>> ')
            
            while True:
                try:
                    valor = int(input(' Ingrese cantidad de datos a Ingresar '))
                except ValueError:
                    print(Fore.RED + "Debes ingresar cantidad de datos a Ingresar")
                    continue
                if valor < 0:
                    print(Fore.RED + "Debes ingresar cantidad de datos a Ingresar")
                    continue
                else:
                    break
            insertar(valor)
            input('Presione una tecla para continuar')
        elif opc == '1':
            os.system('cls||clear')
            print(Fore.GREEN + '\n<<<Mostrar datos>>> ')
            consultar()
            input('Presione una tecla para continuar')
        elif opc == '2':
            os.system('cls||clear')
            print(Fore.GREEN + '\n<<<Modificar datos>>> ')
            busq()
            modificar()
            input('Presione una tecla para continuar')
        elif opc == '3':
            os.system('cls||clear')
            print(Fore.GREEN + '\n<<<Eliminar datos>>> ')
            busq()
            eliminar()
            input('Presione una tecla para continuar')
        elif opc == '4':
            answer=input(f"¿Estas seguro que desea retornar al Menu Principal? [y/n]: ")
            if not answer or answer[0].lower() != 'y':
                input('Presione una tecla para continuar')
            else:
                os.system('cls||clear')
                print(Fore.GREEN + '\n<<<Ha regresado al menu principal>>> ')
                from int_menuprincipal import ejecutar_menu
                ejecutar_menu()
                input('Presione una tecla para continuar')
                os.system('cls')
                break
            
            
