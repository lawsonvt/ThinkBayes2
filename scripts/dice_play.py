#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 19:53:52 2019

@author: pi
"""

import sys
import os

sys.path.append(os.path.abspath("/home/pi/Programming/ThinkBayes2/thinkbayes2/"))
sys.path.append(os.path.abspath("/home/pi/Programming/ThinkBayes2/scripts/"))

from dice import Dice

suite = Dice([4,6,8,12,20])

suite.Update(6) # if i roll a 6

suite.Items() # updated posteriors

for roll in [6,8,7,7,5,4]:  # a whole mess of roles
    suite.Update(roll)

suite.Items()
