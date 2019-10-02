import pygame,sys,os
from level import Level
import random
from utils import direction_to_rowcol
from game_object import GameObject

class Apple(GameObject):
    def __init__(self, row, col):
        super().__init__(row, col)
