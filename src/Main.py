import logging
import pygame
from src import Gconstants, gameclock, GameLoop, Utils, UI

logging.basicConfig(filename='latest.log', level=logging.INFO)

version = ["0.0.2", "Pre - Alpha"]
versionstring = ' '.join(version)
"""
Stepload
Where:
1 (Setup)
2 (Load core Module)
3 (Load Mods)
4 (Mod Interaction)
5 (Cleanup and run game)
"""
print("Starting GalaxyTest Version : " + versionstring)
print("Stepload : 1(Pygame Setup)")
UI.setupFont()
print("StepLoad : 2")
print("StepLoad : 3")
print("StepLoad : 4")
print("StepLoad : 5")
clock = gameclock.GameClock(
    update_callback=GameLoop.update(),
    frame_callback=GameLoop.draw(),
    pause_callback=GameLoop.forcefreeze()
)
while True:
    if Gconstants.Exit:
        Utils.safeexit()
    else:
        clock.tick()
