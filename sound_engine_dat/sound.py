
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
from GLState import *
from gvoxels.gvoxel import *
from sound_engine_dat.sound import *

PyEngineInit()
PyEngineMixerInit()

class Sound:
    def __init__(self,filename,volume):
        self.sound = pygame.mixer.Sound(filename)
        self.sound.set_volume(volume)
        self.sound_length = self.sound.get_length()
        self.sound_raw = self.sound.get_raw()
        self.sound_num_channels = self.sound.get_num_channels()

    def StartPlaying(self,loops,maxtime,fade_ms):
        self.sound.play(loops,maxtime,fade_ms)

    def Fade(self,time):
        self.sound.fadeout(time)

    def StopPlaying(self):
        self.sound.stop()

    def ResetVolume(self,newVolume):
        self.sound.set_volume(newVolume)

    def FindVolume(self):
        return self.sound.get_volume()


