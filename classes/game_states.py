import pygame

class GameStates():
    def __init__(self,setting):
        self.setting=setting
        self.reset_states()
        self.game_active=False


    def reset_states(self):
        self.ship_left=self.setting.ship_left
        self.score = 0