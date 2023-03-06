"""Animación de personaje con uso de sprites.

Este ejemplo muestra como crear una animación de un personaje
usando sprites. El personaje se mueve con las teclas de dirección.

Autores:
    - Ángel Ricardo Gutierrez Meza (201847467)
    - Crhistian André Díaz Bonfigli Pastrana (201829189)
"""

from typing import Tuple, Union
from enum import Enum
from os import listdir
from os.path import join, isfile
import pygame

Coordinate = Tuple[int, int]

Direction = Enum("Direction", "left right up down")

WIDTH, HEIGHT = 800, 600

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

PLAYER_SIZE = (32, 32)
PLAYER_VELOCITY = 5

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Sprites")


def flip(sprites: Tuple[pygame.Surface, ...]) -> Tuple[pygame.Surface, ...]:
    """Invierte los sprites"""
    return tuple(pygame.transform.flip(s, True, False) for s in sprites)


def get_sprites(sprite_sheet: pygame.Surface, size: Coordinate) -> Tuple[pygame.Surface, ...]:
    """Obtiene los sprites de un sprite sheet"""
    sprites = []

    for i in range(0, sprite_sheet.get_width(), size[0]):
        surface = pygame.Surface(size, pygame.SRCALPHA, 32)
        rect = pygame.Rect(i, 0, size[0], size[1])
        surface.blit(sprite_sheet, (0, 0), rect)
        sprites.append(surface)

    return tuple(sprites)


def load_sprites(
        directory: str,
        size: Coordinate,
        flipped: bool = False
) -> dict[str, Tuple[pygame.Surface, ...]]:
    """Carga los sprites de un directorio"""
    path = join("images", directory)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = get_sprites(sprite_sheet, size)
        name = image.replace(".png", "")

        if flipped:
            all_sprites[name + "_right"] = sprites
            all_sprites[name + "_left"] = flip(sprites)
        else:
            all_sprites[name] = sprites

    return all_sprites


class Player(pygame.sprite.Sprite):
    """Representa al jugador"""

    def __init__(self, start: Coordinate, size: Coordinate) -> None:
        """Inicializa el jugador"""
        super().__init__()

        self.color = RED
        self.velocity = PLAYER_VELOCITY
        self.rect = pygame.Rect(start, size)
        self.mask = None
        self.direction: Union[Direction, None] = None
        self.animation_count = 0

    def move(self, keys: pygame.key.ScancodeWrapper) -> None:
        """Mueve al jugador"""
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
            self.set_direction(Direction.left)
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
            self.set_direction(Direction.right)
        elif keys[pygame.K_UP]:
            self.rect.y -= self.velocity
            self.set_direction(Direction.up)
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.velocity
            self.set_direction(Direction.down)
        else:
            self.set_direction(None)

    def set_direction(self, direction: Union[Direction, None]) -> None:
        """Cambia la dirección del jugador"""
        if self.direction != direction:
            self.direction = direction
            self.animation_count = 0

    def draw(self) -> None:
        """Dibuja al jugador"""
        pygame.draw.rect(screen, self.color, self.rect)


def draw(player: Player) -> None:
    """Dibuja todos los elementos en la pantalla"""
    screen.fill(BLACK)

    player.draw()

    pygame.display.flip()


def handle_movement(player: Player) -> None:
    """Maneja el movimiento del jugador"""
    keys = pygame.key.get_pressed()
    player.move(keys)


def main() -> None:
    """Función principal del juego"""
    running = True

    clock = pygame.time.Clock()

    player = Player((WIDTH // 2, HEIGHT // 2), PLAYER_SIZE)

    while running:
        clock.tick(FPS)

        draw(player)

        handle_movement(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()


if __name__ == "__main__":
    main()
