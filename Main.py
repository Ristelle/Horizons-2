import SoundWrapper
from Utils import *
version = ["0.0.1 ", "Pre - Alpha"]
versionstring = ''.join(version)
"""
Stepload
Where:
1 (Setup)
2 (Pre Init)
3 (Init)
4 (Post Init)
5 (Cleanup and run game)
"""
print("Starting GalaxyTest Version : " + versionstring)
print("Stepload : 1")
SoundWrapper.init()

print("StepLoad : 2")