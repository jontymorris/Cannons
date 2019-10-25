"""
Program entry point
"""

import pygame
import window
import home


class Program:
    """
    Class for managing the program
    """

    def __init__(self):
        self.surface = window.create_window()
        self.clock = window.create_clock()
        self.is_running = True

        self.context = home.HomeContext(self.surface)

    def poll_events(self):
        """
        Iterates through the window events
        """

        for event in window.poll_events():
            # check for exit
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.is_running = False

    def game_loop(self):
        """
        Runs the game loop
        """

        while self.is_running:
            self.context.update()
            self.context.render()
            self.poll_events()

            pygame.display.update()
            self.clock.tick(60)

        window.close()


# start the game
if __name__ == '__main__':
    Program().game_loop()
