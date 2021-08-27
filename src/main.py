import sys
import pygame

from src.app import App


class Main:
    __pygame_window: pygame.Surface
    __app: App

    def __init__(self):
        pygame.init()
        self.__pygame_window = pygame.display.set_mode((800, 400))
        self.__app = App()
        self.__run()

    def __run(self):
        while True:
            self.__event_loop()
            self.__update()
            self.__render()

    @staticmethod
    def __event_loop():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def __update(self):
        self.__app.update()

    def __render(self):
        self.__app.render()


if __name__ == '__main__':
    Main()
