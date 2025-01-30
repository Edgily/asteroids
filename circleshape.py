import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        x, y = self.position

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, circle_shape):
        distance_between = self.position.distance_to(circle_shape.position)
        combined_radius = self.radius + circle_shape.radius
        if distance_between <= combined_radius:
            return True
        else:
            return False
