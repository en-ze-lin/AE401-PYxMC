#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 15:19:30 2021

@author: enzelin
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
import random

a = mc.getBlock(x, y-1, z)
a2 = random.randint(4, 7)
b = random.choice([0, 81])
if a == 12:
    mc.setBlock(x, y, z, b)
else:
    mc.setBlocks(x, y, z, x+5, y, z+5, 38,a2)