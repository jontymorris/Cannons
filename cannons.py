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

        # display the home screen
        self.switch_context(home.HomeContext)

    def switch_context(self, new_context):
        """
        Changse the screen context
        """

        self.context = new_context(self.surface, self.switch_context)

    def poll_events(self):
        """
        Iterates through the window events
        """

        for event in window.poll_events():
            # check for exit
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.is_running = False

            # mouse release
            elif event.type == pygame.MOUSEBUTTONUP:
                self.context.mouse_release()

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
