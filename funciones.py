from colorama import Fore, init
init(autoreset=True)
def menu(opciones, titulo):
    print(Fore.GREEN + '*'*30)
    print('{}'.format(titulo))
    print(Fore.GREEN + '*'*30)
    for op in range(0, len(opciones)):
        print("{}) {}".format(op, opciones[op]))
    opc = input('Elija Opcion [0...{}]: '.format(len(opciones)-1))
    return opc




# men = menu(('Grupo','Plan de cuenta','Salir'),'Menu Principal')




        