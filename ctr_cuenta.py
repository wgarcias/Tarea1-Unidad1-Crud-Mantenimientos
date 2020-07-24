from dao_cuenta import DaoCuenta
from mod_cuenta import ModCuenta

class CtrCuenta:
    def __init__(self, cuen=None):
        self.cuenta = cuen
    
    def consulta(self, buscar):
        objDao =  DaoCuenta()
        return objDao.consultar(buscar)

    def ingresar(self, cuen):
        objDao =  DaoCuenta()
        return objDao.ingresar(cuen)

    def modificar(self, cuen):
        objDao =  DaoCuenta()
        return objDao.modificar(cuen)

    def eliminar(self, cuen):
        objDao =  DaoCuenta()
        return objDao.eliminar(cuen)
    
    def verifi(self, buscar):
        objDao =  DaoCuenta()
        return objDao.verifi(buscar)

    def veriCod(self, buscar):
        objDao =  DaoCuenta()
        return objDao.veriCod(buscar)