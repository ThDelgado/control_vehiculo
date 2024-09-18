import os
import platform
import time


class Vehiculo:
    def __init__(self, marca: str, modelo:str , n_ruedas:int ):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas

    def __str__(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, n_ruedas: {self.n_ruedas}")
    

class Automovil(Vehiculo):
    def __init__(self, marca:str, modelo:str, n_ruedas:int, velocidad:int, cilindradas:int ):
        super().__init__(marca, modelo, n_ruedas)
        self.velocidad = velocidad
        self.cilindradas = cilindradas

    def __str__(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, n_ruedas: {self.n_ruedas}, velocidad: {self.velocidad} kms/hr, cilindradas: {self.cilindradas}")





#para almacenar vehiculo
vehiculos = []

delay = 2  #tiempo de espera menu

# """ imprimir datos de automoviles """
def leer_automovil():
    """imprime en pantalla los vehiculos ingresados """
    print("Datos de los vehículos ingresados: ")
    for vehiculo in vehiculos:
        print(vehiculo)
    time.sleep(delay)##


 
def registrar_automovil(indice):
    """captura atributos del auto y crea el objeto Automovil"""
    print(f" Datos del automóvil {indice +1}")
    marca = input("Inserte la marca del auto: ")
    modelo = input("Ingrese el modelo: ")
    n_ruedas = int(input("Inserte número de ruedas: "))
    velocidad = int(input("Inserte la velocidad del auto en km/hr: "))
    cilindradas = int(input("Inserte el cilindraje del auto en cc: "))
    return Automovil(marca, modelo, n_ruedas, velocidad, cilindradas)



def cantidad_registros():
    """Determina cuantos registros queremos hacer de los automoviles y los ingresa a una lista, muestra los registro que se han hecho"""

    try:
        numero_vehiculos = int(input("¿Cuantos vehículos deseas insertar? "))
        for i in range(numero_vehiculos):
            vehiculo = registrar_automovil(i)
            vehiculos.append(vehiculo)
    
    except Exception as e:
        print("Ha ocurrido un error.", e)
    
    leer_automovil()
   

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
        limpiar_consola()
   
        return True
    else:
        limpiar_consola()
        return False




 
def menu(): 
    """menu de tres opciones registrar, leer o salir"""
    print("Menú...")
    print("1.- Registrar nuevo automovil.")
    print("2.- Leer Automovil.")
    print("3.- Salir")
    opcion = input("Ingrese la opción: [1, 2, 3]: ")
    limpiar_consola()

    if opcion == "1":
        cantidad_registros()
        limpiar_consola()
    
    elif opcion == "2":
        leer_automovil()
        limpiar_consola()
    
    elif opcion == "3":
        salir()

    else:
        print("Opción inválida.")
        time.sleep(delay)
        limpiar_consola()
   
 
 
def main():
    """permite repetir el menu hasta que el usuario decide que no quiere seguir"""
    repetir = True
    while repetir: #repite hasta que sea falso
        menu()
        repetir = f_repetir()
       
    salir()
   
main()
   
