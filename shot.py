import pygame
from constants import * 
from circleshape import * 

class Shot(CircleShape):
    def __init__(self, position, velocity):
        x, y = position
        radius = SHOT_RADIUS
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt