from funciones import menu
from colorama import Fore, init
init(autoreset=True)
import os 
def ejecutar_menu():
    Integrantes()
    opc = ' '
    while True:
        os.system('cls||clear')
        Integrantes()
        opc =  str(menu(
            ['Grupo','Plan de cuenta','Salir'],
            Fore.GREEN + '      MENU PRINCIPAL   '))
        if opc == '0':
            os.system('cls||clear')
            from int_grupo import ejecutar_grupo
            ejecutar_grupo()
            print(Fore.GREEN + '\n<<<Ha Ingresado al menu Grupo>>> ')
            input('Presione una tecla para continuar')
        elif opc == '1':
            os.system('cls||clear')
            from int_cuenta import ejecutar_cuenta
            ejecutar_cuenta()
            print(Fore.GREEN + '\n<<<Ha Ingresado al menu Plan de cuenta>>> ')
            input('Presione una tecla para continuar')
        elif opc == '2':
            answer=input(f"¿Estas seguro que desea salir del sistema? [y/n]: ")
            if not answer or answer[0].lower() != 'y':
                input('Presione una tecla para continuar')
            else:
                print(Fore.GREEN + '\n<<<Gracias por usar el Sistema>>> ')
                exit( )
                break

def Integrantes():
    print(Fore.GREEN + '*'*30)
    print(Fore.GREEN + '   INTEGRANTES DEL DEBER:      ')
    print(Fore.GREEN + '*'*30)
    print(Fore.BLUE + '  José Arreaga Salvatierra ')
    print(Fore.BLUE + '  William Garcia Sojos ')
    print(Fore.BLUE + '  Israel Zambrano Dominguez ')
    

       
ejecutar_menu()
