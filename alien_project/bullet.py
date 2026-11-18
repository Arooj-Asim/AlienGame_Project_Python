import pygame
# Pygame's Sprite class provides functionality for managing game objects
# can manage as part of sprite groups.
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen

        # this creates bullet rectangle
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top


        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

       
    def update(self):
     ''''move bullets towards upward'''
    # Update the decimal position of the bullet.
     self.y -= self.speed_factor
     # Update the rect position.
     self.rect.y = self.y 

    def draw_bullet(self):
     """Draw the bullet to the screen."""
     pygame.draw.rect(self.screen, self.color, self.rect)           