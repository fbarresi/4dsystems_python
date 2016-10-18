#!/bin/python
'''
Python wrapper for
4DSystems' Diablo16 & Picaso Displays

Copyright (C) 2016 by Xose Pérez <xose dot perez at gmail dot com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
from DiabloSerial import DiabloSerial
from DiabloConstants import *

def callback(errcode, errbyte):
    print "ERROR: ", errcode, errbyte
    sys.exit(1)

if __name__ == "__main__":
    diablo = DiabloSerial(2000, True, callback)
    if diablo:
        diablo.OpenComm('/dev/ttyUSB0', 9600)
        print "Model:", diablo.sys_GetModel()
        print "Version:", diablo.sys_GetVersion()
        diablo.gfx_Cls()
        diablo.putstr("HELLO WORLD")
        diablo.gfx_Button(1, 20, 40, GRAY, WHITE, FONT3, 3, 3, "Press Me")
        diablo.gfx_Circle(60, 160, 10, GRAY)
        diablo.gfx_Polyline(4, [140, 140, 150, 160], [10, 20, 10, 30], GRAY)
