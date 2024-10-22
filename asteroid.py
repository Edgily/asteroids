from constants import *
from circleshape import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    # def split(self):
    #     self.kill()
    #     if self.radius <= ASTEROID_MIN_RADIUS:
    #         return

    #     random_angle = random.uniform(20, 50)
    #     angle_1 = self.velocity.rotate(random_angle)
    #     angle_2 = self.velocity.rotate(-random_angle)

    #     new_radius = self.radius - ASTEROID_MIN_RADIUS

    #     new_asteroid_1 = Asteroid(self.x, self.y, new_radius)
    #     new_asteroid_1.velocity = angle_1 * 1.2
    #     new_asteroid_2 = Asteroid(self.x, self.y, new_radius)
    #     new_asteroid_2.velocity = angle_2 * 1.2

    #     print(new_asteroid_1.x, new_asteroid_1.y)\
        
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2