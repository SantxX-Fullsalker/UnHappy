import pygame
import sys
import os
import time
import random
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.personaje import Personaje
from src.enemigo import Enemigo
from src.objeto import Objeto
from src.escenario import Escenario

pygame.init()

# Configuración de pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("UnHappy")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)  # Definición del color oro

# Fuente
font = pygame.font.Font(None, 36)



def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    click = False
    while True:
        screen.fill(BLACK)
        draw_text('Menú Principal', font, WHITE, screen, SCREEN_WIDTH // 2 - 90, SCREEN_HEIGHT // 2 - 200)
        mx, my = pygame.mouse.get_pos()

        button_play = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 25, 110, 50)
        pygame.draw.rect(screen, GREEN if button_play.collidepoint((mx, my)) else WHITE, button_play)
        draw_text('Jugar', font, BLACK, screen, SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 15)

        if button_play.collidepoint((mx, my)):
            if click:
                character_selection()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def character_selection():
    click = False
    while True:
        screen.fill(BLACK)
        draw_text('Escoge tu clase:', font, WHITE, screen, SCREEN_WIDTH // 2 - 90, SCREEN_HEIGHT // 2 - 200)
        mx, my = pygame.mouse.get_pos()

        button_arquero = pygame.Rect(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 25, 100, 50)
        button_mago = pygame.Rect(SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2 - 25, 100, 50)
        pygame.draw.rect(screen, GREEN if button_arquero.collidepoint((mx, my)) else WHITE, button_arquero)
        pygame.draw.rect(screen, GREEN if button_mago.collidepoint((mx, my)) else WHITE, button_mago)
        draw_text('Arquero', font, BLACK, screen, SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 15)
        draw_text('Mago', font, BLACK, screen, SCREEN_WIDTH // 2 + 120, SCREEN_HEIGHT // 2 - 15)

        if button_arquero.collidepoint((mx, my)):
            if click:
                personaje = Personaje(7, 16, 13, 1, [['Arco', '', ''], ['', '', ''], ['', '', '']], SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                personaje.cadencia_disparo = 1  # 1 disparo por segundo
                game_loop(personaje)
        if button_mago.collidepoint((mx, my)):
            if click:
                personaje = Personaje(10, 8, 7, 1, [['Bastón', '', ''], ['', '', ''], ['', '', '']], SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                personaje.cadencia_disparo = 0.5  # 2 disparos por segundo
                game_loop(personaje)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def generar_enemigos(n, personaje):
    enemigos = []
    for _ in range(n):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        while math.hypot(x - personaje.x, y - personaje.y) < 100:  # Asegura que los enemigos no se generen demasiado cerca
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
        enemigos.append({'x': x, 'y': y, 'dx': 0, 'dy': 0})
    return enemigos

def generar_objetos(n, personaje):
    objetos = []
    for _ in range(n):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        while math.hypot(x - personaje.x, y - personaje.y) < 100:  # Asegura que los objetos no se generen demasiado cerca
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
        objetos.append({'x': x, 'y': y, 'nombre': 'oro'})
    return objetos

def game_loop(personaje):
    running = True
    last_shot_time = 0
    inventario_abierto = False
    enemigos = generar_enemigos(5, personaje)  # Genera 5 enemigos
    objetos = generar_objetos(3, personaje)  # Genera 3 objetos
    reloj = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    inventario_abierto = not inventario_abierto
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            personaje.mover("arriba")
        if keys[pygame.K_s]:
            personaje.mover("abajo")
        if keys[pygame.K_a]:
            personaje.mover("izquierda")
        if keys[pygame.K_d]:
            personaje.mover("derecha")

        if inventario_abierto:
            draw_inventory(personaje.inventario)

        pygame.display.update()
        reloj.tick(60)

        mx, my = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:  # Botón izquierdo del ratón
            current_time = time.time()
            if current_time - last_shot_time >= 1 / personaje.cadencia_disparo:
                personaje.disparar(mx, my)
                last_shot_time = current_time

        screen.fill(BLACK)

        # Dibujar personaje
        pygame.draw.rect(screen, WHITE, (personaje.x, personaje.y, 20, 20))

        # Dibujar balas
        for bala in personaje.balas:
            bala['x'] += bala['dx']
            bala['y'] += bala['dy']
            pygame.draw.circle(screen, RED, (int(bala['x']), int(bala['y'])), 5)

        # Dibujar enemigos
        for enemigo in enemigos:
            pygame.draw.rect(screen, RED, (enemigo['x'], enemigo['y'], 20, 20))

            # Colisión con el personaje
            if pygame.Rect(enemigo['x'], enemigo['y'], 20, 20).colliderect(pygame.Rect(personaje.x, personaje.y, 20, 20)):
                personaje.recibir_ataque(1)
                if personaje.puntos_de_vida <= 0:
                    running = False

        # Eliminar enemigos al recibir disparos
        for bala in personaje.balas:
            bala['x'] += bala['dx']
            bala['y'] += bala['dy']
            pygame.draw.circle(screen, RED, (int(bala['x']), int(bala['y'])), 5)

            # Detectar colisión entre balas y enemigos
            for enemigo in enemigos[:]:
                if pygame.Rect(enemigo['x'], enemigo['y'], 20, 20).collidepoint((bala['x'], bala['y'])):
                    enemigos.remove(enemigo)  # Eliminar enemigo
                    personaje.balas.remove(bala)  # Eliminar bala
                    break

        # Hacer que los enemigos se dirijan hacia el personaje
        for enemigo in enemigos:
            dx = personaje.x - enemigo['x']
            dy = personaje.y - enemigo['y']
            dist = math.hypot(dx, dy)
            if dist != 0:
                dx /= dist
                dy /= dist
            enemigo['x'] += dx * 4.0  
            enemigo['y'] += dy * 4.0

        # Dibujar objetos
        for objeto in objetos:
            pygame.draw.circle(screen, GOLD, (objeto['x'], objeto['y']), 10)

            # Colisión con el personaje
            if pygame.Rect(objeto['x'] - 10, objeto['y'] - 10, 20, 20).colliderect(pygame.Rect(personaje.x, personaje.y, 20, 20)):
                personaje.recolectar('oro')
                objetos.remove(objeto)

        pygame.display.flip()

    # Mostrar pantalla de reaparecer
    respawn_menu(personaje)

def respawn_menu(personaje):
    click = False
    while True:
        screen.fill(BLACK)
        draw_text('Has muerto', font, RED, screen, SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2 - 50)

        mx, my = pygame.mouse.get_pos()

        # Botón respawn
        button_respawn = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 50, 125, 50)
        pygame.draw.rect(screen, GREEN if button_respawn.collidepoint((mx, my)) else WHITE, button_respawn)
        draw_text('Reintentar', font, BLACK, screen, SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2 + 60)
        
        if button_respawn.collidepoint((mx, my)):
            if click:
                personaje.puntos_de_vida = 10  # Restaurar puntos de vida
                personaje.limpiar_inventario()  # Limpiar el inventario
                game_loop(personaje)    

        # Botón exit
        button_exit = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 120, 125, 50)
        pygame.draw.rect(screen, GREEN if button_exit.collidepoint((mx, my)) else WHITE, button_exit)
        draw_text('Salir', font, BLACK, screen, SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 + 130)

        if button_exit.collidepoint((mx, my)):  # Lógica del botón exit
            if click:
                pygame.quit()
                sys.exit()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def draw_inventory(inventario):
    draw_text('Inventario:', font, WHITE, screen, SCREEN_WIDTH // 2 - 50, 50)

    for i in range(3):
        for j in range(3):
            x = SCREEN_WIDTH // 2 - 90 + j * 60
            y = SCREEN_HEIGHT // 2 - 90 + i * 60
            pygame.draw.rect(screen, WHITE, (x, y, 50, 50), 2)
            item = inventario[i][j]
            if item:
                draw_text(item[0], font, WHITE, screen, x + 15, y + 15)

if __name__ == "__main__":
    main_menu()

# Main execution
main_menu()
