import sys
from conexion import Conector
from colorama import Fore, init
init(autoreset=True)
class DaoCuenta(Conector):
    def __init__(self):
        super().__init__()
    
    
    def consultar(self, buscar):
        result = False
        try:
            sql = "SELECT id, codigo, grupo, descripcion, naturaleza, case estado  when 0 then 'False'  when 1 then 'True' end as estado FROM cuentas where descripcion like'%" + \
                    str(buscar) + "%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e: 
            print("Error en la consulta de las cuentas", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def ingresar(self, cuen):
        correcto = True
        try:
            sql = "insert into cuentas (codigo,grupo,descripcion,naturaleza,estado) values (%s,%s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(sql, (cuen.codigo,cuen.grupo,cuen.descripcion,cuen.naturaleza,cuen.estado))
            self.conn.commit()
        except Exception:
            print(Fore.RED +'¡Advertencia!: ', "Error al insertar Plan de Cuenta, porque el grupo no existe")
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def modificar(self, cuen):
        correcto =  True
        try:
            sql = "Update cuentas set codigo = %s,grupo = %s,descripcion = %s,naturaleza = %s,estado = %s where id = %s"
            self.conectar()
            self.conector.execute(sql, (cuen.codigo,cuen.grupo,cuen.descripcion,cuen.naturaleza,cuen.estado,cuen.id))
            self.conn.commit()
        except Exception as e:
            correcto = False
            print("Error al modificar cuentas", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def eliminar(self, cuen):
        correcto = True
        try:
            sql = "delete from cuentas where id = %s"
            self.conectar()
            self.conector.execute(sql, (cuen.id))
            self.conn.commit()
        except Exception as e:
            print("Error al eliminar cuentas", e)
            correcto =  False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto
    
    
    def verifi(self, buscar):
        result = False
        try:
            sql = "select id from cuentas where id = %s" 
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
    
    def veriCod(self, buscar):
        result = False
        try:
            sql = "select codigo from cuentas where codigo = %s" 
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