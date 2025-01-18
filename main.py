
import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.init()
    clk = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player1.update(dt)
        player1.draw(screen)
        pygame.display.flip()
        dt = clk.tick(60)/1000


if __name__ == "__main__":
    main()

