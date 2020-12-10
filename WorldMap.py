import pygame

from pygame.math import Vector2
from pygame.rect import Rect

from Blocks import *
from GameRule import GameRuleObserver
from Settings import *


class GameState():
    def __init__(self):
        self.worldSize = Vector2(WORLD_MAX_X, WORLD_MAX_Y)
        self.playerState = False  # 游戏状态，True表示获胜状态
        self.units = [
            GeneralBlock("baba", False, False, True, True, Vector2(360, 270), 'pics/baba_0_1.png'),

            BabaNounBlock("text_baba", True, False, True, False, Vector2(270, 150), 'pics/text_baba_0_1.png', 'baba'),
            IsBlock("text_is1", True, False, True, False, Vector2(300, 150), 'pics/text_is_0_1.png', 'is'),
            YouVerbBlock("text_you", True, False, True, False, Vector2(330, 150), 'pics/text_you_0_1.png', 'you'),

            GeneralBlock("rock1", False, False, True, False, Vector2(690, 150), 'pics/rock_0_1.png'),
            GeneralBlock("rock2", False, False, True, False, Vector2(660, 150), 'pics/rock_0_1.png'),
            GeneralBlock("rock3", False, False, True, False, Vector2(690, 180), 'pics/rock_0_1.png'),
            GeneralBlock("rock4", False, False, True, False, Vector2(660, 180), 'pics/rock_0_1.png'),
            RockNounBlock("text_rock", True, False, True, False, Vector2(540, 150), 'pics/text_rock_0_1.png', 'stone'),
            IsBlock("text_is2", True, False, True, False, Vector2(570, 150), 'pics/text_is_0_1.png', 'is'),
            PushVerbBlock("text_push", True, False, True, False, Vector2(600, 150), 'pics/text_push_0_1.png', 'push'),

            GeneralBlock("wall1", False, False, False, True, Vector2(420, 390), 'pics/wall_1_1.png'),
            GeneralBlock("wall2", False, False, False, True, Vector2(420, 360), 'pics/wall_4_1.png'),
            GeneralBlock("wall3", False, False, False, True, Vector2(390, 390), 'pics/wall_1_1.png'),
            GeneralBlock("wall4", False, False, False, True, Vector2(390, 360), 'pics/wall_4_1.png'),
            WallNounBlock("text_wall", True, False, True, False, Vector2(270, 390), 'pics/text_wall_0_1.png', 'wall'),
            IsBlock("text_is3", True, False, True, False, Vector2(300, 390), 'pics/text_is_0_1.png', 'is'),
            StopVerbBlock("text_stop", True, False, True, False, Vector2(330, 390), 'pics/text_stop_0_1.png', 'stop'),

            GeneralBlock("flag1", False, True, True, False, Vector2(660, 390), 'pics/flag_0_1.png'),
            GeneralBlock("flag2", False, True, True, False, Vector2(660, 360), 'pics/flag_0_1.png'),
            GeneralBlock("flag3", False, True, True, False, Vector2(690, 390), 'pics/flag_0_1.png'),
            GeneralBlock("flag4", False, True, True, False, Vector2(690, 360), 'pics/flag_0_1.png'),
            FlagNounBlock("text_flag", True, False, True, False, Vector2(540, 390), 'pics/text_flag_0_1.png', 'flag'),
            IsBlock("text_is4", True, False, True, False, Vector2(570, 390), 'pics/text_is_0_1.png', 'is'),
            WinVerbBlock("text_win", True, False, True, False, Vector2(600, 390), 'pics/text_win_0_1.png', 'win'),

            GeneralBlock("skull1", False, False, True, False, Vector2(690, 480), 'pics/skull_0_1.png'),
            GeneralBlock("skull2", False, False, True, False, Vector2(690, 510), 'pics/skull_0_1.png'),
            GeneralBlock("skull3", False, False, True, True, False, Vector2(660, 510), 'pics/skull_0_1.png'),
            GeneralBlock("skull4", False, False, True, False, Vector2(660, 480), 'pics/skull_0_1.png'),
            SkullNounBlock("text_skull", True, False, True, False, Vector2(540, 480), 'pics/text_skull_0_1.png', 'skull'),
            IsBlock("test_is5", True, False, True, False, Vector2(570, 480), 'pics/text_is_0_1.png', 'is'),
            DefeatVerbBlock("text_defeat", True, False, True, False, Vector2(600, 480), 'pics/text_defeat_0_1.png', 'defeat'),

            GeneralBlock("lava1", False, True, True, False, Vector2(390, 480), 'pics/water_0_1.png'),
            GeneralBlock("lava2", False, True, True, False, Vector2(420, 510), 'pics/water_0_1.png'),
            GeneralBlock("lava3", False, True, True, False, Vector2(390, 510), 'pics/water_0_1.png'),
            GeneralBlock("lava4", False, True, True, False, Vector2(420, 480), 'pics/water_0_1.png'),
            LavaNounBlock("text_lava", True, False, True, False, Vector2(270, 480), 'pics/text_lava_0_1.png', 'lava'),
            IsBlock("text_is6", True, False, True, False, Vector2(300, 480), 'pics/text_is_0_1.png', 'is'),
            HotVerbBlock("text_hot", True, False, True, False, Vector2(330, 480), 'pics/text_hot_0_1.png', 'hot'),

            BabaNounBlock("text_baba2", True, False, True, False, Vector2(270, 60), 'pics/text_baba_0_1.png', 'baba'),
            IsBlock("text_is7", True, False, True, False, Vector2(300, 60), 'pics/text_is_0_1.png', 'is'),
            MeltVerbBlock("text_melt", True, False, True, False, Vector2(330, 60), 'pics/text_melt_0_1.png', 'melt'),

            GeneralBlock("grass1", False, True, True, False, Vector2(0, 0), 'pics/grass_0_1.png'),
            GeneralBlock("grass2", False, True, True, False, Vector2(30, 0), 'pics/grass_0_1.png'),
            GeneralBlock("grass3", False, True, True, False, Vector2(0, 30), 'pics/grass_0_1.png'),
            GeneralBlock("grass4", False, True, True, False, Vector2(30, 30), 'pics/grass_0_1.png'),

        ]

        self.isBlockList = []
        for unit in self.units:
            if unit._text and unit.word == "is":
                self.isBlockList.append(unit)


class UserInterface():
    def __init__(self):
        pygame.init()
        self._gameState = GameState()
        self._cellSize = Vector2(CELL_SIZE_X, CELL_SIZE_Y)
        _windowSize = self._gameState.worldSize.elementwise() * self._cellSize
        self._window = pygame.display.set_mode((int(_windowSize.x), int(_windowSize.y)))
        self._clock = pygame.time.Clock()
        self._running = True
        self._moveCommand = Vector2(0, 0)

    def _update(self):
        for unit in self._gameState.units:
            testObserver = GameRuleObserver(self._gameState)

            if unit.is_control():
                testObserver._move(unit, self._moveCommand)
            if testObserver._is_win(self._gameState.units):
                print("Victory")

            '''
            test = GameRuleObserver(self._gameState)
            if unit._id == "testIs":
                print(test._is_win(self._gameState.isBlockList))
            '''


    def _process_input(self):
        self._moveCommand = Vector2(0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    self._running = False
                    break
                elif event.key == pygame.K_RIGHT:
                    self._moveCommand = RIGHT_DIRECTION
                elif event.key == pygame.K_LEFT:
                    self._moveCommand = LEFT_DIRECTION
                elif event.key == pygame.K_DOWN:
                    self._moveCommand = BOTTOM_DIRECTION
                elif event.key == pygame.K_UP:
                    self._moveCommand = TOP_DIRECTION

    def _render_unit(self, unit):
        self._window.blit(unit.texture, unit.location)

    def _render(self):
        self._window.fill(BACKGROUND_COLOR)  # 黑色背景

        for unit in self._gameState.units:
            self._render_unit(unit)

        pygame.display.update()

    def run(self):
        while self._running:
            self._process_input()
            self._update()
            self._render()
            self._clock.tick(60)


if __name__ == '__main__':
    ui = UserInterface()
    ui.run()

    pygame.quit()
