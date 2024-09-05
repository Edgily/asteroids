import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # the 'game loop' where STUFF happens and screen is refreshed
    while True:
        pygame.Surface.fill(screen, (0, 0, 0, 1))

        for obj in updateable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)

        # 'refreshses' the screen, do everything before refreshing else ya won't see nuttin
        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick / 1000

        # check for window close, end process if closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
