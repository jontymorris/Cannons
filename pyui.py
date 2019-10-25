"""
Make user interfaces with ease
"""

import pygame


class Label:
    """
    Object for displaying text
    """

    def __init__(self, surface, text, position, font_info):
        self.surface = surface

        font = pygame.font.Font(font_info[0], font_info[1])
        self.label = font.render(text, True, font_info[2])

        self.rect = self.label.get_rect()
        self.rect.center = position
        self.rect = self.rect.move(self.rect.width/2, self.rect.height/2)

    def render(self):
        """
        Draws the text
        """

        self.surface.blit(self.label, self.rect)
