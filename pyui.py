"""
Make user interfaces with ease
"""

import pygame
import assets
import colors


class Label:
    """
    Object for displaying text
    """

    def __init__(self, surface, text, position, font_info):
        self.surface = surface

        font = pygame.font.Font(font_info[0], font_info[1])
        self.label = font.render(text, True, font_info[2])
        self.shadow = font.render(text, True, colors.BLACK)

        self.rect = self.label.get_rect()
        self.rect.center = position
        self.rect = self.rect.move(self.rect.width/2, self.rect.height/2)

        self.shadow_rect = self.rect.move(2, 2)

    def render(self):
        """
        Draws the text
        """

        self.surface.blit(self.shadow, self.shadow_rect)
        self.surface.blit(self.label, self.rect)


class Image:
    """
    Object for displaying an image
    """

    def __init__(self, surface, path, position, size):
        self.surface = surface

        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect()
        self.rect.center = position
        self.rect = self.rect.move(self.rect.width/2, self.rect.height/2)

    def render(self):
        """
        Renders the image
        """

        self.surface.blit(self.image, self.rect)


class Button:
    """
    Object for managing a button
    """

    def __init__(self, surface, text, position):
        self.is_active = False
        self.button_width = 500
        self.button_height = 100

        # create the images
        self.image_normal = Image(
            surface,
            assets.BUTTON_NORMAL,
            position,
            (self.button_width, self.button_height)
        )

        self.image_active = Image(
            surface,
            assets.BUTTON_ACTIVE,
            position,
            (self.button_width, self.button_height)
        )

        # create the label
        self.label = Label(
            surface,
            text,
            position,
            (assets.ABOVE_FONT, 50, colors.WHITE)
        )

        # center the label
        self.label.rect = self.label.rect.move(
            -self.label.rect.width/2, -self.label.rect.height/2)
        self.label.rect = self.label.rect.move(
            self.button_width/2, self.button_height/2)
        self.label.shadow_rect = self.label.rect.move(2, 2)

    def update(self):
        """
        Updates the button
        """

        mouse_pos = pygame.mouse.get_pos()
        button_rect = self.image_normal.rect

        # is mouse over button?
        self.is_active = button_rect.collidepoint(mouse_pos)

    def render(self):
        """
        Draws the button
        """

        if self.is_active:
            self.image_active.render()
        else:
            self.image_normal.render()

        self.label.render()
