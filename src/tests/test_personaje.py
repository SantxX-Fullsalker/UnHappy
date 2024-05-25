# tests/test_personaje.py

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from personajes.personaje import Personaje


class TestPersonaje(unittest.TestCase):
    def setUp(self):
        self.personaje = Personaje(100, 20, 10, 1)

    def test_posicion_actual(self):
        self.assertEqual(self.personaje.posicion_actual(), (0, 0))

    def test_atacar(self):
        enemigo = Personaje(50, 15, 5, 1)
        self.personaje.atacar(enemigo)
        self.assertEqual(enemigo.puntos_de_vida, 35)

    def test_recibir_ataque(self):
        self.personaje.recibir_ataque(25)
        self.assertEqual(self.personaje.puntos_de_vida, 85)

    def test_recolectar(self):
        objeto = "espada"
        self.personaje.recolectar(objeto)
        self.assertIn(objeto, self.personaje.inventario)

    def test_usar(self):
        objeto = MockObjeto()
        self.personaje.recolectar(objeto)
        self.personaje.usar(objeto)
        self.assertNotIn(objeto, self.personaje.inventario)

    def test_vender(self):
        objeto = MockObjeto()
        self.personaje.recolectar(objeto)
        self.personaje.vender(objeto)
        self.assertNotIn(objeto, self.personaje.inventario)

    def test_subir_nivel(self):
        self.personaje.subir_nivel({'ataque': 5, 'defensa': 3})
        self.assertEqual(self.personaje.nivel, 2)
        self.assertEqual(self.personaje.ataque, 25)
        self.assertEqual(self.personaje.defensa, 13)

class MockObjeto:
    def usar(self, personaje):
        pass

    def vender(self):
        pass

if __name__ == "__main__":
    unittest.main()
