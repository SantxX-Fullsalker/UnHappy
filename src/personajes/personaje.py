# src/personajes/personaje.py

class Personaje:
    def __init__(self, puntos_de_vida, ataque, defensa, nivel, inventario=None):
        self.puntos_de_vida = puntos_de_vida
        self.ataque = ataque
        self.defensa = defensa
        self.nivel = nivel
        self.inventario = inventario if inventario is not None else []

    def posicion_actual(self):
        # Aquí se definiría la lógica para obtener la posición actual del personaje
        return (0, 0)

    def atacar(self, enemigo):
        # Lógica para atacar a un enemigo
        enemigo.recibir_ataque(self.ataque)

    def recibir_ataque(self, ataque):
        # Lógica para recibir un ataque
        dano = max(0, ataque - self.defensa)
        self.puntos_de_vida = max(0, self.puntos_de_vida - dano)

    def recolectar(self, objeto):
        # Lógica para recolectar un objeto
        self.inventario.append(objeto)

    def usar(self, objeto):
        # Lógica para usar un objeto
        if objeto in self.inventario:
            objeto.usar(self)
            self.inventario.remove(objeto)

    def vender(self, objeto):
        # Lógica para vender un objeto
        if objeto in self.inventario:
            # Suponiendo que hay un método vender en el objeto
            objeto.vender()
            self.inventario.remove(objeto)

    def subir_nivel(self, atributos):
        # Lógica para subir de nivel y mejorar atributos
        self.nivel += 1
        for atributo, incremento in atributos.items():
            setattr(self, atributo, getattr(self, atributo) + incremento)


