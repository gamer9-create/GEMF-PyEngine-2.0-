from pygame import *
from PyEngine2.game import *
from PyEngine2.tile import *
from PyEngine2.camera import *
from PyEngine2.model import *
from PyEngine2.level_loader import *
from PyEngine2.replacements import *


class input_handler:
    def __init__(self):
        self.arrow_keys_order = ["UP","DOWN","LEFT","RIGHT"]
        self.arrow_keys = [K_UP,K_DOWN,K_LEFT,K_RIGHT]
        self.wasd_keys = [K_w,K_a,K_s,K_d]
        self.wasd_keys_order = ["W","A","S","D"]
        self.Spacebar = K_SPACE
        self.E = K_e
        self.F = K_f
        self.R = K_r

    def IsKeyBeingPressed(self,key):
        keysObj = pygame.key.get_pressed()
        if keysObj[key]:
            return True
        else:
            return False




