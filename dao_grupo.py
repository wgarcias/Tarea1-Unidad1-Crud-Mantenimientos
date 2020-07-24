import sys
from conexion import Conector
from colorama import Fore, init
init(autoreset=True)
import  pymysql.cursors

class DaoGrupo(Conector):
    def __init__(self):
        super().__init__()

    def consultar(self, buscar):
        result = False
        try:
            sql = "select id idgrup, descripcion descrip from grupo where descripcion like'%" + \
                    str(buscar) + "%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e: 
            print("Error en la consulta del grupo", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def ingresar(self, gru):
        correcto = True
        try:
            sql = "insert into grupo (descripcion) values (%s)"
            self.conectar()
            self.conector.execute(sql, (gru.descripcion))
            self.conn.commit()
        except Exception as e:
            print("Error al insertar grupo", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def modificar(self, gru):
        correcto =  True
        try:
            sql = "Update grupo set descripcion = %s where id = %s"
            self.conectar()
            self.conector.execute(sql, (gru.descripcion, gru.id))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar grupo", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def eliminar(self, gru):
        correcto = True
        try:
            sql = "delete from grupo where id = %s"
            self.conectar()
            self.conector.execute(sql, (gru.id))
            self.conn.commit()
        except Exception:
            print(Fore.RED +'¡Advertencia!: ', "Error al eliminar grupo, porque se esta utilizando en el Plan de cuenta")
            correcto =  False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def verifi(self, buscar):
        result = False
        try:
            sql = "select id from grupo where id = %s" 
            self.conectar()
            self.conector.execute(sql, int(buscar))
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e: 
            print("Error en la consulta de las cuentas", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result


    

   
        



""" con = DaoGrupo()
grupos = con.consultar("")
print(grupos)
for gru in grupos:
    print(gru[1]) """



# sql = "Select id idgrup, descripcion descrip From grupo where like'%" + \
#                 str(buscar) + "%' order by id"



