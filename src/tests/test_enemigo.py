# tests/test_enemigo.py

import unittest
import sys
import os

# Agregar la ruta del directorio principal al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar la clase Enemigo del módulo correspondiente
from personajes.enemigo import Enemigo

class TestEnemigo(unittest.TestCase):
    def setUp(self):
        self.enemigo = Enemigo(100, 20, 10, 1, "Terrestre")

    def test_posicion_actual(self):
        self.assertEqual(self.enemigo.posicion_actual(), (0, 0))

    def test_atacar(self):
        personaje = MockPersonaje()
        self.enemigo.atacar(personaje)
        self.assertEqual(personaje.puntos_de_vida, 80)

    def test_defender(self):
        self.enemigo.defender(25)
        self.assertEqual(self.enemigo.puntos_de_vida, 85)

class MockPersonaje:
    def __init__(self):
        self.puntos_de_vida = 100

    def recibir_ataque(self, ataque):
        self.puntos_de_vida -= ataque

if __name__ == "__main__":
    unittest.main()
