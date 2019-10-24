"""
Program entry point
"""

import window


SURFACE = window.create_window()
CLOCK = window.create_clock()


def poll_events():
    """
    Iterates through the window events
    """

    for event in window.poll_events():
        # check for exit
        if event.type == 12:
            window.close()
            exit(0)


def update():
    """
    Updates the game
    """


def render():
    """
    Draws the game
    """


def game_loop():
    """
    Runs the game loop
    """

    while True:
        update()
        render()

        poll_events()
        CLOCK.tick(60)


if __name__ == '__main__':
    game_loop()
