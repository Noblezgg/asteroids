
import pygame
from constants import *
from player import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clk = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asterioidfield = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for draw in drawable:
            draw.draw(screen)
        for update in updatable:
            update.update(dt)

        screen.fill("black")

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        dt = clk.tick(60)/1000

if __name__ == "__main__":
    main()

