
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

