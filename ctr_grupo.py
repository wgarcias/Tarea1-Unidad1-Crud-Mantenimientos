from dao_grupo import DaoGrupo
from mod_grupo import ModGrupo

class CtrGrupo:
    def __init__(self, gru=None):
        self.grupo = gru
    
    def consulta(self, buscar):
        objDao =  DaoGrupo()
        return objDao.consultar(buscar)

    def ingresar(self, gru):
        objDao =  DaoGrupo()
        return objDao.ingresar(gru)

    def modificar(self, gru):
        objDao =  DaoGrupo()
        return objDao.modificar(gru)

    def eliminar(self, gru):
        objDao =  DaoGrupo()
        return objDao.eliminar(gru)

    def verifi(self, buscar):
        objDao =  DaoGrupo()
        return objDao.verifi(buscar)

""" gru = ModGrupo(3, 'Patrimonios')
ctr = CtrGrupo()
ctr.modificar(gru)
grupos = ctr.consulta("")
print(grupos)
for gru in grupos:
    print(gru[0], gru[1]) """





