"""Animación de personaje con uso de sprites.

Este ejemplo muestra como crear una animación de un personaje
usando sprites. El personaje se mueve con las teclas de dirección.

Autores:
    - Ángel Ricardo Gutierrez Meza (201847467)
    - Crhistian André Díaz Bonfigli Pastrana (201829189)
"""

import pygame

WIDTH, HEIGHT = 800, 600

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Sprites")


def draw() -> None:
    """Dibuja todos los elementos en la pantalla"""
    screen.fill(BLACK)

    pygame.display.flip()


def main() -> None:
    """Función principal del juego"""
    running = True

    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()


if __name__ == "__main__":
    main()
