# src/escenarios/escenario.py

class Escenario:
    def __init__(self, territorio, areas, ubicacion_enemigos=None, ubicacion_objetos=None, vendedor=None):
        self.territorio = territorio
        self.areas = areas
        self.ubicacion_enemigos = ubicacion_enemigos if ubicacion_enemigos is not None else []
        self.ubicacion_objetos = ubicacion_objetos if ubicacion_objetos is not None else []
        self.vendedor = vendedor

    def ubicar_enemigos(self, enemigos):
        # Lógica para ubicar enemigos en el escenario
        self.ubicacion_enemigos.extend(enemigos)

    def ubicar_objetos(self, objetos):
        # Lógica para ubicar objetos en el escenario
        self.ubicacion_objetos.extend(objetos)

    def agregar_zona_venta(self, vendedor):
        # Lógica para agregar una zona de venta al escenario
        self.vendedor = vendedor

