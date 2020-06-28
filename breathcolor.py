import random
from colour import Color
import os
import time
import re

red = Color("red")

green = Color("green")

blue = Color("blue")

rg = list(red.range_to(green, 30))
gb = list(green.range_to(blue, 30))
br = list(blue.range_to(red, 30))

while True:
    for c in rg:
        time.sleep(0.05)
        os.system("rivalcfg -c '"+str(c)+"'")
    for i in gb:
        time.sleep(0.05)
        os.system("rivalcfg -c '"+str(i)+"'")
    for j in br:
        time.sleep(0.05)
        os.system("rivalcfg -c '"+str(j)+"'")

