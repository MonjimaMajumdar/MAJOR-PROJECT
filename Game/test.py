import random

import pygame.draw
from pygame import Vector2

from Game.Node import Node
from utils.utils import utils

class Graph:
    def __init__ (self,count = 10, nodeDst = 200,  nearDst = 400, farDst = 600):
        self.nodes = []
        self.count = count
        self.nodeDst = nodeDst
        
        for i in range(0, count):
            
