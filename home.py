"""
Contains the class for the game's home screen
"""

import pygame
import pyui
import assets


class HomeContext:
    """
    Used for the game's home screen
    """

    def __init__(self, surface):
        self.surface = surface

        # play soundtrack
        pygame.mixer.music.load(assets.HOME_SOUND)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        # create the interface
        self.desert_image = pyui.Image(
            surface, assets.DESERT_IMAGE, (0, 0), (1920, 1080))
        self.cannon_image = pyui.Image(
            surface, assets.CANNON_IMAGE, (520, 200), (880, 468))
        self.play_button = pyui.Button(
            surface, 'Play Cannons', (710, 750))

    def update(self):
        """
        Updates the home screen
        """

        self.play_button.update()

    def render(self):
        """
        Draws the home screen
        """

        self.desert_image.render()
        self.cannon_image.render()
        self.play_button.render()
