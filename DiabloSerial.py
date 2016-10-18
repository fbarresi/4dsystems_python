'''
Python wrapper for
4DSystems' Diablo16 & Picaso Displays

Copyright (C) 2016 by Xose Perez <xose dot perez at gmail dot com>

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

from ctypes import *
from BaseSerial import BaseSerial

class DiabloSerial(BaseSerial):

    def library(self):
        return cdll.LoadLibrary("libs/libdiabloSerial.so")

    def definitions(self):
        definitions = super(DiabloSerial, self).definitions()
        definitions['bus_Read8'] = [c_uint16, []]
        definitions['bus_Write8'] = [None, [c_uint16]]
        definitions['putstr'] = [c_uint16, [c_char_p]]
        return definitions
