from ctr_grupo import CtrGrupo
from mod_grupo import ModGrupo
from funciones import menu
import os
import sys
from colorama import Fore, init
init(autoreset=True)
ctr = CtrGrupo()

def insertar(rango):
    for i in range(int(rango)):
        while True:
            try:
                descripcion = input('Ingrese descripcion: ')
            except ValueError:
                continue
            if not(descripcion.isalpha()):
                print(Fore.RED + "Debes escribir una descripcion valida")
                continue
            else:
                break
        cli = ModGrupo(descrip=descripcion.capitalize())
        answer=input(f"¿Estas seguro que desea guardar el grupo con la descripcion: {descripcion}? [y/n]: ")
        if not answer or answer[0].lower() != 'y':
            input('Presione una tecla para continuar')
            ejecutar_grupo()
        else:
            if ctr.ingresar(cli):
                print(Fore.YELLOW + 'Registro grabado correctamente')
            else:
                print(Fore.RED + 'Error al grabar el registro')

def modificar():
    while True:
        try:
            codigo = int(input('Ingrese codigo: '))
        except ValueError:
            print(Fore.RED + "Debes escribir un codigo valido")
            continue
        if codigo < 0:
            print(Fore.RED + "Debes escribir numero positivo")
            continue
        if not(ctr.verifi(codigo)):
            print(Fore.RED +'Error: No existe el codigo Ingresado, por favor escriba un codigo valido')
        else:
            break
    while True:
        try:
            descripcion = input('Ingrese descripcion: ')
        except ValueError:
            continue
        if not(descripcion.isalpha()):
            print(Fore.RED + "Debes escribir una descripcion valida")
            continue
        else:

            break
    
    cli = ModGrupo(idgrup=codigo,descrip=descripcion.capitalize())
    answer=input(f"¿Estás seguro que desea guardar la modificacion del grupo con el Código: {codigo} y la descripción: {descripcion}? [y/n]: ")
    if not answer or answer[0].lower() != 'y':
        input('Presione una tecla para continuar')
        ejecutar_grupo()
    else:
        if ctr.modificar(cli):
            print(Fore.YELLOW + 'Registro modificado correctamente')
        else:
            print(Fore.RED + 'Error al modificar el registro')

   
def eliminar():
        while True:
            try:
                codigo = int(input('Ingrese codigo: '))
            except ValueError:
                print(Fore.RED + "Debes escribir un codigo valido")
                continue
            if codigo < 0:
                print(Fore.RED + "Debes escribir numero positivo")
                continue
            if not(ctr.verifi(codigo)):
                print(Fore.RED +'Error: No existe el codigo Ingresado, por favor escriba un codigo valido')
            else:
                break
        cli =  ModGrupo(idgrup=codigo)
        answer=input(f"¿Estás seguro que desea eliminar el grupo con el código: {codigo}? [y/n]: ")
        if not answer or answer[0].lower() != 'y':
            input('Presione una tecla para continuar')
            ejecutar_grupo()
        else:
            if ctr.eliminar(cli):
                print(Fore.YELLOW + 'Registro eliminado correctamente')
            else:
                print(Fore.RED + 'Error al eliminar el registro')

def consultar():
    buscar = input('Ingrese nombre a buscar: ')
    cli = ctr.consulta(buscar)
    print(Fore.WHITE + '-----------------------')
    print(Fore.BLUE + '   Codigo  Descripcion')
    print(Fore.WHITE + '-----------------------')
    for registro in cli:
        print("{:7}     {:7}".format(registro[0],registro[1]))
    print(Fore.WHITE + '-----------------------')
    
def busq():
    buscar = ''
    cli = ctr.consulta(buscar)
    print(Fore.WHITE + '-----------------------')
    print(Fore.BLUE + '   Codigo  Descripcion')
    print(Fore.WHITE + '-----------------------')
    for registro in cli:
        print("{:7}     {:7}".format(registro[0],registro[1]))
    print(Fore.WHITE + '-----------------------')

def ejecutar_grupo():
    opc = ''
    while True:
        os.system('cls||clear')
        opc =  str(menu(
            ['Ingresar', 'Mostrar' ,'Modificar', 'Eliminar', 'Retornar Menu Principal'],
            Fore.GREEN + 'MENU GRUPO DE CUENTA'))
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
            print(Fore.BLUE + '<<< Lista de Grupos >>> ')
            busq()
            modificar()
            input('Presione una tecla para continuar')
        elif opc == '3':
            os.system('cls||clear')
            print(Fore.GREEN + '\n<<<Eliminar datos>>> ')
            print(Fore.BLUE + '<<< Lista de Grupos >>> ')
            busq()
            eliminar()
            input('Presione una tecla para continuar')
        elif opc == '4':
            answer=input(f"Estas seguro que desea retornar al Menu Principal [y/n]: ")
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


# 'ejecutar_grupo()'


    