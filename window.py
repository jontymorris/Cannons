"""
Methods for managing a pygame window
"""

import pygame


def create_window():
    """
    Returns a new fullscreen window
    """

    pygame.init()
    pygame.font.init()

    surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    return surface


def create_clock():
    """
    Returns a new clock
    """

    return pygame.time.Clock()


def poll_events():
    """
    Returns the pygame events
    """

    return pygame.event.get()


def close():
    """
    Closes all the pygame windows
    """

    pygame.quit()
