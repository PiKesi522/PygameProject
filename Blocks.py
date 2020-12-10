import pygame
from pygame._sprite import AbstractGroup
from pygame.rect import Rect
from pygame.math import Vector2

from BaseBlock import BaseBlock
from Settings import *


class GeneralBlock(BaseBlock):
    def _is_collide(self, group: pygame.sprite.Group) -> bool:
        return pygame.sprite.spritecollide(self, group, False)

    def move(self, direction: Vector2, group):
        if self.is_move() and self.is_control():
            self.location += direction
            self.rect = Rect(self.location.x, self.location.y, CELL_SIZE_X, CELL_SIZE_Y)

            if self.location.x < 0 or self.location.x >= WORLD_MAX_X * CELL_SIZE_X or self.location.y < 0 \
                    or self.location.y >= WORLD_MAX_Y * CELL_SIZE_Y \
                    or self._is_collide(group):
                self.location -= direction
                self.rect = Rect(self.location.x, self.location.y, CELL_SIZE_X, CELL_SIZE_Y)


class YouVerbBlock(BaseBlock):
    def __init__(self, id: str,text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str):
        super().__init__(id, text, moveable, controllable, location, texture)
        self.word = word
        self._controllable = False
        self.moveable = True
    '''if(blocks) -> block.controllable = True'''
    '''baba.YouVerbBlock(...)'''

class HotVerbBlock(BaseBlock):
    def __init__(self, id: str,text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str):
        super().__init__(id, text, moveable, controllable, location, texture)
        self.word = word
        self._controllable = False
        self.moveable = True
    '''if(melt) -> defeat'''
    '''Lava.HotVerbBlock(...)'''


class StopVerbBlock(BaseBlock):
    def __init__(self, id: str,text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str):
        super().__init__(id, text, moveable, controllable, location, texture)
        self.word = word
        self._controllable = False
        self.moveable = True
    '''if(block) -> block.moveable = False'''
    '''Wall.StopVerbBlock(...)'''

class PushVerbBlock(BaseBlock):
    def __init__(self, id: str,text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str):
        super().__init__(id, text, moveable, controllable, location, texture)
        self.word = word
        self._controllable = False
        self.moveable = True
    '''if(block) -> block.moveable = True'''
    '''Stone.PushVerbBlock(...)'''


class WinVerbBlock(BaseBlock):
    def __init__(self, id: str,text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str):
        super().__init__(id, text, moveable, controllable, location, texture)
        self.word = word
        self._controllable = False
        self.moveable = True
    '''if(touch) -> win'''
    '''Flag.WinVerbBlock(...)'''


class DefeatVerbBlock(BaseBlock):
    def __init__(self, id: str,text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str):
        super().__init__(id, text, moveable, controllable, location, texture)
        self.word = word
        self._controllable = False
        self.moveable = True
    '''if(touch) -> defeat'''
    '''Skull.DefeatVerbBlock(...)'''


class MeltVerbBlock(BaseBlock):
    def __init__(self, id: str,text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str):
        super().__init__(id, text, moveable, controllable, location, texture)
        self.word = word
        self._controllable = False
        self.moveable = True
    '''if(touch -> hot) -> defeat'''
    '''xxx.MeltVerbBlock(...)'''


class IsBlock(BaseBlock):
    def __init__(self, id: str,text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str):
        super().__init__(id, text, moveable, controllable, location, texture)
        self.word = word
        self._controllable = False
        self.moveable = True


class BabaNounBlock(BaseBlock):
    def __init__(self, id: str,text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str):
        super().__init__(id, text, moveable, controllable, location, texture)
        self.word = word
        self._controllable = False
        self.moveable = True


class RockNounBlock(BaseBlock):
    def __init__(self, id: str,text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str):
        super().__init__(id, text, moveable, controllable, location, texture)
        self.word = word
        self._controllable = False
        self.moveable = True


class WallNounBlock(BaseBlock):
    def __init__(self, id: str,text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str):
        super().__init__(id, text, moveable, controllable, location, texture)
        self.word = word
        self._controllable = False
        self.moveable = True


class FlagNounBlock(BaseBlock):
    def __init__(self, id: str,text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str):
        super().__init__(id, text, moveable, controllable, location, texture)
        self.word = word
        self._controllable = False
        self.moveable = True

class SkullNounBlock(BaseBlock):
    def __init__(self, id: str,text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str):
        super().__init__(id, text, moveable, controllable, location, texture)
        self.word = word
        self._controllable = False
        self.moveable = True

class LavaNounBlock(BaseBlock):
    def __init__(self, id: str,text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str):
        super().__init__(id, text, moveable, controllable, location, texture)
        self.word = word
        self._controllable = False
        self.moveable = True