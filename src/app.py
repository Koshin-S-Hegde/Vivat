from src.game import Game
from src.menu import Menu


class App:
    __menu: Menu
    __game: Game
    __game_started: bool

    def __init__(self):
        self.__menu = Menu()
        self.__game = Game()
        self.__game_started = False

    def render(self):
        if self.__game_started:
            self.__game.render()
        else:
            self.__menu.render()

    def update(self):
        if self.__game_started:
            self.__game.update()
        else:
            self.__menu.update()
            self.__game_started = self.__menu.is_button_clicked()
