
import pygame
from PyEngine2.game import *
from PyEngine2.tile import *
from PyEngine2.camera import *

from PyEngine2.model import *
from PyEngine2.level_loader import *
from PyEngine2.replacements import *
from PyEngine2.animation import *
from window_engine_dat.window import *

from input_engine_dat.input import *

from render_engine_dat.renderer import *
from tiled_engine_dar.tiled import *

class gVoxel:
    def __init__(self, parent, name, properties, obj_class):
        self.parent = parent
        self.children = []
        self.name = name
        self.properties = properties
        self.obj_class = obj_class

    def addChildren(self,d):
        self.children.append(d)

    def resetParent(self,newParent):
        self.parent = newParent

    def removeChildren(self,d):
        self.children.remove(d)













