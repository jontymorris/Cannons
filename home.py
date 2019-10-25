"""
Contains the class for the game's home screen
"""

import pyui
import colors
import assets


class HomeContext:
    """
    Used for the game's home screen
    """

    def __init__(self, surface):
        self.test_label = pyui.Label(
            surface,
            'Hello there',
            (0, 100),
            (assets.ABOVE_FONT, 12, colors.BLUE)
        )

    def update(self):
        """
        Updates the home screen
        """

    def render(self):
        """
        Draws the home screen
        """

        self.test_label.render()
