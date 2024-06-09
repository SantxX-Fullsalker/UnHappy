import pygame
import math

class Personaje:
    def __init__(self, puntos_de_vida, ataque, defensa, nivel, inventario=None, x=0, y=0, cadencia_disparo=1):
        self.puntos_de_vida = puntos_de_vida
        self.ataque = ataque
        self.defensa = defensa
        self.nivel = nivel
        self.inventario = inventario if inventario is not None else [['' for _ in range(3)] for _ in range(3)]
        self.arma_inicial = inventario[0][0] if inventario and inventario[0] else ''
        self.x = x
        self.y = y
        self.cadencia_disparo = cadencia_disparo
        self.balas = []  # Lista para almacenar las balas disparadas

    def posicion_actual(self):
        return (self.x, self.y)

    def mover(self, direccion):
        if direccion == "arriba":
            self.y -= 3.38
        elif direccion == "abajo":
            self.y += 3.38
        elif direccion == "izquierda":
            self.x -= 3.38
        elif direccion == "derecha":
            self.x += 3.38

    def disparar(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.hypot(dx, dy)
        if distance != 0:
            dx /= distance
            dy /= distance
        speed = 10  # Velocidad de la bala
        bala = {'x': self.x, 'y': self.y, 'dx': dx * speed, 'dy': dy * speed}
        self.balas.append(bala)

    def recibir_ataque(self, danio):
        self.puntos_de_vida -= danio

    def atacar(self, enemigo):
        enemigo.recibir_ataque(self.ataque)

    def recolectar(self, objeto):
        for i in range(3):
            for j in range(3):
                if self.inventario[i][j] == '':
                    self.inventario[i][j] = objeto
                    return
        print("Inventario lleno")

    def subir_nivel(self, mejoras):
        self.nivel += 1
        for atributo, incremento in mejoras.items():
            if hasattr(self, atributo):
                setattr(self, atributo, getattr(self, atributo) + incremento)

    def usar(self, objeto):
        for i in range(3):
            for j in range(3):
                if self.inventario[i][j] == objeto:
                    # Definir efectos del objeto
                    if objeto == 'pocion':
                        self.puntos_de_vida += 5
                    self.inventario[i][j] = ''
                    return

    def vender(self, objeto):
        for i in range(3):
            for j in range(3):
                if self.inventario[i][j] == objeto:
                    self.inventario[i][j] = ''
                    return
        # Incrementar algún recurso del personaje, ej: oro

    def limpiar_inventario(self):
        self.inventario = [['' for _ in range(3)] for _ in range(3)]
        if self.arma_inicial:
            self.inventario[0][0] = self.arma_inicial