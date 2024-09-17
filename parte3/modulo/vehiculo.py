import os
import platform
import time
import csv 
import json 


class Vehiculo:
    def __init__(self, marca: str, modelo:str , n_ruedas:int ):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas

    def __str__(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, n_ruedas: {self.n_ruedas}")
    
    def guardar_datos_csv(self, archivo_csv):
        """guarda los datos de los vehiculos en un archvio csv."""
        with open(archivo_csv, "a", newline="") as archivo:
            archivo_csv_writer = csv.writer(archivo)
            datos = { "class": self.__class__.__name__,
                "atributos": self.__dict__}
            archivo_csv_writer.writerow([json.dumps(datos)])
        
    @staticmethod
    def leer_datos_csv(archivo_csv):
        """Lee archivo csv  y lo muestra """
    
        if not os.path.isfile(archivo_csv):
            print(f"El archivo {archivo_csv} no existe.")
            return
        try:
            with open(archivo_csv, "r") as archivo:
                archivo_csv_reader = csv.reader(archivo)
                for fila in archivo_csv_reader:
                    if fila:
                        datos = json.loads(fila[0])
                        clase_str = datos["class"]
                        atributos_str = datos["atributos"]

                        clase = globals().get(clase_str)
                        if clase:
                            vehiculo = clase(**atributos_str)
                            print(vehiculo)
                        else:
                            print(f"Clase {clase_str} no encontrada")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")


class Automovil(Vehiculo):
    def __init__(self, marca:str, modelo:str, n_ruedas:int, velocidad:int, cilindradas:int ):
        super().__init__(marca, modelo, n_ruedas)
        self.velocidad = velocidad
        self.cilindradas = cilindradas

    def __str__(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, n_ruedas: {self.n_ruedas}, velocidad: {self.velocidad} kms/hr, cilindradas: {self.cilindradas}")

class Bicicleta(Vehiculo):
    def __init__(self, marca: str, modelo:str , n_ruedas:int, tipo_uso:str ):
        super().__init__(marca, modelo, n_ruedas)
        self.tipo_uso = tipo_uso
    
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, n_ruedas: {self.n_ruedas}, Tipo de uso: {self.tipo_uso}"

class Motocicleta(Bicicleta):
    def __init__(self, marca: str, modelo:str , n_ruedas:int, tipo_uso:str, nro_radios:int, cuadro:str, motor:str):
        super().__init__(marca, modelo, n_ruedas, tipo_uso)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor
    
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, n_ruedas: {self.n_ruedas}, numero de radios: {self.nro_radios}, cuadro: {self.cuadro}, tipo de uso: {self.tipo_uso}"

class VehiculoParticular(Automovil):
    def __init__(self, marca:str, modelo:str, n_ruedas:int, velocidad:int, cilindradas:int, nro_puesto:int):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindradas)
        self.nro_puesto = nro_puesto

    def __str__(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, n_ruedas: {self.n_ruedas}, velocidad: {self.velocidad} kms/hr, cilindradas: {self.cilindradas}, nro_puesto: {self.nro_puesto}")

class VehiculoCarga(Automovil):
    def __init__(self, marca:str, modelo:str, n_ruedas:int, velocidad:int, cilindradas:int, peso_carga:int):
         super().__init__(marca, modelo, n_ruedas, velocidad, cilindradas)
         self.peso_carga = peso_carga

    def __str__(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, n_ruedas: {self.n_ruedas}, velocidad: {self.velocidad} kms/hr, cilindradas: {self.cilindradas}, peso de carga: {self.peso_carga}")


#para almacenar vehiculo
vehiculos = []

delay = 5  #tiempo de espera menu

# """ imprimir datos de automoviles """
def carga_archivo_vehiculo(nombre_archivo):
    """carga vehiculos desde csv """
    vehiculo.leer_datos_csv(nombre_archivo)

def leer_vehiculo():
    """muestra en pantalla los vehiculos ingresados"""
    print("\nDatos de los vehiculos ingresados: ")
    for vehiclo in vehiculos:
        print(vehiculo)
    time.sleep(delay)

def crear_automovil():
   
    nombre_archivo = "vehiculos.csv"
    
    """captura atributos del auto y crea el objeto Automovil"""
   
    marca = input("Inserte la marca del auto: ")
    modelo = input("Ingrese el modelo: ")
    n_ruedas = int(input("Inserte número de ruedas: "))
    velocidad = int(input("Inserte la velocidad del auto en km/hr: "))
    cilindradas = int(input("Inserte el cilindraje del auto en cc: "))

    #crea objeto automovil
    vehiculo = Automovil(marca, modelo, n_ruedas, velocidad, cilindradas)
    vehiculos.append(vehiculo)
    
    vehiculo.guardar_datos_csv(nombre_archivo)


def crear_vehiculo_particular():
   
    nombre_archivo = "vehiculos.csv"
    
    """captura atributos del vehiculo particular y crea el objeto Vehiculo PArticular"""
   
    marca = input("Inserte la marca del vehiculo particular: ")
    modelo = input("Ingrese el modelo: ")
    n_ruedas = int(input("Inserte número de ruedas: "))
    velocidad = int(input("Inserte la velocidad del auto en km/hr: "))
    cilindradas = int(input("Inserte el cilindraje del auto en cc: "))
    nro_puesto = int(input("Ingrese el número de puestos: "))
    
    #crea objeto vehiculo particular
    vehiculo = VehiculoParticular(marca, modelo, n_ruedas, velocidad, cilindradas, nro_puesto)
    vehiculos.append(vehiculo)
    
    vehiculo.guardar_datos_csv(nombre_archivo)

    
def crear_vehiculo_carga():
   
    nombre_archivo = "vehiculos.csv"
    
    """captura atributos del vehiculo particular y crea el objeto Vehiculo PArticular"""
   
    marca = input("Inserte la marca de vehiculo de carga: ")
    modelo = input("Ingrese el modelo: ")
    n_ruedas = int(input("Inserte número de ruedas: "))
    velocidad = int(input("Inserte la velocidad del auto en km/hr: "))
    cilindradas = int(input("Inserte el cilindraje del auto en cc: "))
    peso_carga = int(input("Ingrese el peso de carga en kg: "))
    
    #crea objeto vehiculo de carga
    vehiculo = VehiculoCarga(marca, modelo, n_ruedas, velocidad, cilindradas, peso_carga)
    vehiculos.append(vehiculo)
    
    vehiculo.guardar_datos_csv(nombre_archivo)


def crear_bicicleta():
   
    nombre_archivo = "vehiculos.csv"
    
    """captura atributos del auto y crea el objeto Automovil"""
   
    marca = input("Inserte la marca del bicicleta: ")
    modelo = input("Ingrese el modelo: ")
    n_ruedas = int(input("Inserte número de ruedas: "))
    tipo_uso = input("Ingrese el tipo de uso: ")
    
    #crea objeto bicicleta
    vehiculo = Bicicleta(marca, modelo, n_ruedas, tipo_uso)
    vehiculos.append(vehiculo)
    
    vehiculo.guardar_datos_csv(nombre_archivo)

def crear_motocicleta():
   
    nombre_archivo = "vehiculos.csv"
    
    """captura atributos del auto y crea el objeto Automovil"""
   
    marca = input("Inserte la marca del motocicleta: ")
    modelo = input("Ingrese el modelo: ")
    n_ruedas = int(input("Inserte número de ruedas: "))
    tipo_uso = input("Ingrese el tipo de uso: ")
    nro_radios = int(input("Ingrese el número de radios: "))
    cuadro = input("Ingrese el cuadro: ")
    motor = input("Ingrese el tipo de motor: ")
    

    #crea objeto Motocicleta
    vehiculo = Motocicleta(marca, modelo, n_ruedas, tipo_uso, nro_radios, cuadro, motor)
    vehiculos.append(vehiculo)
    
    vehiculo.guardar_datos_csv(nombre_archivo)



def salir():
    """mensaje de salida de sistema"""
    print("Gracias por utilizar el sistema.")##
   

def limpiar_consola():
    """limpia consola segun sistema"""
    sistema = platform.system() #platform captura el sistema enel que se trabaj
   
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def f_repetir(): #entrega falso o verdadero
    """solo entrega verdadero o falso dependiendo la opcion que se elige "s" o cualquier letra"""
    opcion = input("Si desea volver al menú ingrese [s], de lo contrario, presione cualquier tecla: ")    
    if opcion.lower() == "s":
        
   
        return True
    else:
        limpiar_consola()
        return False

 
def menu(): #entrega 
    """menu de  opciones registrar, leer o salir"""
    print("Menú...")
    print("1.- Registrar nuevo automovil.")
    print("2.- Registrar nuevo vehiculo particular.")
    print("3.- Registrar nuevo vehiculo de carga.")
    print("4.- Registrar nueva bicicleta.")
    print("5.- Registrar nueva motocicicleta.")
    print("6.- Ver vehiculos registerados.")
    print("7.- Salir")
    opcion = input("Ingrese la opción: [1, 2, 3, 4, 5, 6, 7]: ")
    limpiar_consola()

    if opcion == "1":
        crear_automovil() 
    elif opcion == "2":
        crear_vehiculo_particular()
    elif opcion == "3":
        crear_vehiculo_carga()
    elif opcion == "4":
        crear_bicicleta()
    elif opcion == "5":
        crear_motocicleta()
    elif opcion == "6":
        Vehiculo.leer_datos_csv("vehiculos.csv") 
    elif opcion == "7":    
        salir()           
    else:
        print("Opción inválida.")
        time.sleep(delay)
        limpiar_consola()
   

def main():
    """permite repetir el menu hasta que el usuario decide que no quiere seguir"""
    #carga_archivo_vehiculo("vehiculos.csv")
    repetir = True
    while repetir: #repite hasta que sea falso
        menu()
        repetir = f_repetir()
       
    salir()
   
main()
   
