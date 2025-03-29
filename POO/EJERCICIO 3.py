import datetime

class Facultad:
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre
        self.inscripciones = []
        self.carreras = []

    def mostrar_carreras_y_alumnos(self):
      print(f"Facultad: {self.nombre}")
      for carrera in self.carreras:
        carrera.mostrar_alumnos()

    def agregar_inscripcion(self, inscripcion):
        self.inscripciones.append(inscripcion)
      
    def agregar_carrera(self,carrera): #METODO PARA AGREGAR CARRERAS A LA CLASE FACULTAD
      self.carreras.append(carrera)
        

class Alumno:
    def __init__(self, nombre, dni, fecha_nacimiento, carrera):
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento =  fecha_nacimiento
        self.carreras = [carrera]

    def calcular_edad(self):
        dif_anios = datetime.datetime.now().year - self.fecha_nacimiento.year
        return dif_anios

    def obtener_nombre(self):
        return self.nombre

class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inscripciones = []

    def mostrar_alumnos(self):
        print("Carrera: ",self.nombre)
        for inscripcion in self.inscripciones:
          inscripcion.mostrar()

    def obtener_nombre(self):
        return self.nombre

class Inscripcion:
    def __init__(self, fecha_inscripcion, alumno, carrera) -> None:
        self.fecha_inscripcion = fecha_inscripcion
        self.alumno = alumno
        self.carrera = carrera
        self.carrera.inscripciones.append(self) #AGREGA UNA INSCRIPCION A CARRERA

    def mostrar(self):
        print("- ",self.alumno.obtener_nombre(), self.fecha_inscripcion)

# Crear facultad
fich = Facultad("FICH")

# Crear carreras
informatica = Carrera("Ingeniería en Informática")
recursos_hidricos = Carrera ("Ingeniería en Recursos Hídricos")
# AGREGA CARRERAS A FACULTAD
fich.agregar_carrera(informatica)
fich.agregar_carrera(recursos_hidricos)

# Crear alumnos
alumno1 = Alumno("Alumno1", "11.111.111", datetime.date(1990, 11, 11), informatica)
alumno2 = Alumno("Alumno2","22.222.222",datetime.date(1990,12,12),informatica)

# Crear inscripciones, agregar a facultad, etc..
fich.agregar_inscripcion(Inscripcion(datetime.date(2008,12,10), alumno1, informatica))
fich.agregar_inscripcion(Inscripcion(datetime.date(2008,11,12),alumno2,informatica))

# Mostrar información
fich.mostrar_carreras_y_alumnos()