class Evento:
    def __init__(self,nombre:str,fecha:str,hora:str) -> None:
        self.nombre=nombre
        self.fecha=fecha
        self.hora=hora
        
    def __str__(self) -> str:
        return f'El evento {self.nombre} ha sido programado para la fecha {self.fecha} en la hora {self.hora}'