# Se requiere desarrollar un sistema de nómina para los trabajadores de una empresa.
# Los datos personales de los trabajadores incluyen Nombre y Apellidos, Dirección y DNI.
# Existen diferentes tipos de trabajadores:
# Mensualizados: Estos empleados reciben una cantidad fija cada mes, basada en la categoría que tienen.
# Jornalizados: Estos empleados reciben un pago por cada hora trabajada durante el mes.
# El precio es fijo para las primeras 40 horas y diferente para las horas restantes.
# Jefe: Estos empleados tienen un salario fijo, que es un acuerdo personal con la empresa.
# Cada empleado tiene obligatoriamente un jefe, excepto los jefes que no tienen ninguno. 
# El sistema debe ser capaz de calcular las remuneraciones de cada trabajador en un período dado.
class Trabajador:
  def __init__(self,nombre,apellido,direccion,dni):
    self.nombre = nombre 
    self.apellido = apellido
    self.direccion = direccion
    self.dni = dni

  def calcular_remuneracion(self):
    return 0
    

class Mensualizado(Trabajador):
  def __init__(self,nombre,apellido,direccion,dni,categoria,sueldo_fijo):
    super().__init__(nombre,apellido,direccion,dni)
    self.categoria = categoria
    self.sueldo_fijo = sueldo_fijo

  def calcular_remuneracion(self):
    return self.sueldo_fijo

class Jornalizado(Trabajador):
  def __init__(self,nombre,apellido,direccion,dni,sueldo_fijo,sueldo_diferente):
    super().__init__(nombre,apellido,direccion,dni)
    self.sueldo_fijo = sueldo_fijo
    self.sueldo_diferente = sueldo_diferente
  
  def calcular_remuneracion(self,horas_trabajadas):
    total = 0
    if horas_trabajadas > 40:
      total += self.sueldo_fijo * 40
      total += self.sueldo_diferente * (horas_trabajadas-40)
    else:
      total = self.sueldo_fijo * horas_trabajadas
    return total

class Jefe(Trabajador):
  def __init__(self,nombre,apellido,direccion,dni,salario_fijo):
    super().__init__(nombre,apellido,direccion,dni)
    self.salario_fijo = salario_fijo
  
  def calcular_remuneracion(self):
     return self.salario_fijo

trabajador1 = Mensualizado("Jorge","Perez","Rivadavia 2131",12312312,100,200)
print(trabajador1.calcular_remuneracion())
