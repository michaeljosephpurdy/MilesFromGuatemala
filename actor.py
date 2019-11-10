import pygame
from pygame import transform, image

class Actor:
    animations = []
    surface_object = None

    x = 0
    dx = 0
    width = 0

    y = 0
    dy = 0
    height = 0

    def __init__(self):
        self.surface_object = pygame.image.load('data/bat3.png')

    def update(self, dt):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.surface_object = pygame.transform.scale(self.surface_object, (40, 20))

    def draw(self):
        return (self.surface_object, (100, 100))
        # TODO: the heck is charX2?
        #return (self.surface_object, (charX2, 100))