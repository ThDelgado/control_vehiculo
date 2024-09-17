class Vehiculo:
    def __init__(self, marca: str, modelo:str , n_ruedas:int ):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas

    def __str__(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, n_ruedas: {self.n_ruedas}")
    

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



class Automovil(Vehiculo):
    def __init__(self, marca:str, modelo:str, n_ruedas:int, velocidad:int, cilindradas:int ):
        super().__init__(marca, modelo, n_ruedas)
        self.velocidad = velocidad
        self.cilindradas = cilindradas

    def __str__(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, n_ruedas: {self.n_ruedas}, velocidad: {self.velocidad} kms/hr, cilindradas: {self.cilindradas}")

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

