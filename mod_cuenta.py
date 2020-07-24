from mod_grupo import ModGrupo
class ModCuenta(ModGrupo):
    def __init__(self, _id=0, cod='', idgrup=0, descrip='', natur='', estad=1):
        super().__init__()
        self.id = _id
        self.codigo = cod
        self.grupo = idgrup
        self.descripcion = descrip
        self.naturaleza = natur
        self.estado =  estad

