"""
Contains the class for the gameplay screen
"""

import colors


class GameContext:
    """
    Used for the gameplay screen
    """

    def __init__(self, surface, switch_context):
        self.surface = surface
        self.switch_context = switch_context

    def mouse_release(self):
        """
        Handles for the mouse release
        """

    def update(self):
        """
        Updates the gameplay
        """

    def render(self):
        """
        Draws the gameplay
        """

        self.surface.fill(colors.BROWN)
