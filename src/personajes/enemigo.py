# src/personajes/enemigo.py

class Enemigo:
    def __init__(self, puntos_de_vida, ataque, defensa, nivel, tipo, inventario=None):
        self.puntos_de_vida = puntos_de_vida
        self.ataque = ataque
        self.defensa = defensa
        self.nivel = nivel
        self.tipo = tipo
        self.inventario = inventario if inventario is not None else []

    def posicion_actual(self):
        # Lógica para obtener la posición actual del enemigo
        return (0, 0)

    def atacar(self, personaje):
        # Lógica para que el enemigo ataque al personaje
        personaje.recibir_ataque(self.ataque)

    def defender(self, ataque):
        # Lógica para que el enemigo se defienda
        dano = max(0, ataque - self.defensa)
        self.puntos_de_vida = max(0, self.puntos_de_vida - dano)
