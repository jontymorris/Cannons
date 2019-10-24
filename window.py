"""
Methods for managing a pygame window
"""

import pygame


def create_window():
    """
    Returns a new window
    """

    pygame.init()
    surface = pygame.display.set_mode((1920, 1080), 0, 32)

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
