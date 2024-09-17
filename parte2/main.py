from vehiculo import VehiculoParticular 
from vehiculo import VehiculoCarga
from vehiculo import Bicicleta
from vehiculo import Motocicleta
from vehiculo import Automovil
from vehiculo import Vehiculo


particular = VehiculoParticular("Ford", "Fiesta", 4, "180", "500", 5) 
carga = VehiculoCarga("Daft Trucks", "G 38", 10, 120, "1000", "20000") 
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21) 
print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

print("Motocicleta es instancia con relación a Vehículo:", isinstance(motocicleta, Vehiculo) ) 
print(" Motocicleta es instancia con relación a Automovil:", isinstance(motocicleta, Automovil)) 
print("Motocicleta es instancia con relación a Vehículo particular:", isinstance(motocicleta, VehiculoParticular)) 
print("Motocicleta es instancia con relación a Vehículo de Carga: ", isinstance(motocicleta, VehiculoCarga)) 
print(" Motocicleta es instancia con relación a Bicicleta:", isinstance(motocicleta, Bicicleta)) 
print("Motocicleta es instancia con relación a Motocicleta:", isinstance(motocicleta, Motocicleta))