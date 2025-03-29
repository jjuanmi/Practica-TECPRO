import hashlib

class Persona:
    def __init__(self, nombre, apellido, fecha_nacimiento, password):
        self.nombre =  nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.password = hashlib.sha256(password.encode()).hexdigest()

    def calcular_edad(self):
      hoy = datetime.date.today()
      edad = hoy.year - self.fecha_nacimiento.year - ((hoy.month,hoy.day)<(self.fecha_nacimiento.month,self.fecha_nacimiento.day))
      return edad

    def mostrar(self):
      print(self.apellido,self.nombre)
      print(self.calcular_edad()," años")
      print("fecha cumple: ",self.fecha_nacimiento)

    def validar_password(self, password):
      if self.password == hashlib.sha256(password.encode()).hexdigest():
        return True
      else:
         return False


juan = Persona("Juan", "Perez", "1990-11-11", "password")
print(juan.validar_password("password"))  # Salida: True
print(juan.validar_password("incorrecto"))  # Salida: False