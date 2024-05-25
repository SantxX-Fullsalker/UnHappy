# tests/test_escenario.py

import unittest
import sys
import os

# Asegura que el directorio src está en el path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from escenarios.escenario import Escenario
from personajes.personaje import Personaje
from personajes.enemigo import Enemigo
from objetos.objeto import Objeto

class MockVendedor:
    def __init__(self):
        self.inventario = []

    def comprar(self, objeto):
        self.inventario.append(objeto)

class TestEscenario(unittest.TestCase):
    def setUp(self):
        self.escenario = Escenario("Bosque", ["Zona 1", "Zona 2"])

    def test_ubicar_enemigos(self):
        enemigos = [Enemigo(100, 20, 10, 1, "Orco")]
        self.escenario.ubicar_enemigos(enemigos)
        self.assertIn(enemigos[0], self.escenario.ubicacion_enemigos)

    def test_ubicar_objetos(self):
        objetos = [Objeto("Espada", "arma", 100, 10)]
        self.escenario.ubicar_objetos(objetos)
        self.assertIn(objetos[0], self.escenario.ubicacion_objetos)

    def test_agregar_zona_venta(self):
        vendedor = MockVendedor()
        self.escenario.agregar_zona_venta(vendedor)
        self.assertEqual(self.escenario.vendedor, vendedor)

if __name__ == "__main__":
    unittest.main()
