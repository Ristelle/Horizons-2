

import pygame
import os
Resources = [['Ores'], ['energy']]
DoRender = 0
Freezeticking = 0
screenx = 1000
screeny = 500
Exit = False
Shipsprite = []
BackgroundSprite = []
UISprite = []
PlanetRender = []
uifiles = []
if os.environ.get('IsCI') is not None:
    screen = pygame.display.set_mode((screenx, screeny))
else:
    pass
Size = 0
Font = None
fontfile = (os.getcwd() + '\Resources\Fonts\\trench.ttf')