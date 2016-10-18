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

from ctypes import *
from BaseSerial import BaseSerial

class PicasoSerial(BaseSerial):

    def library(self):
        return cdll.LoadLibrary("libs/libpicasoSerial.so")

    def definitions(self):
        definitions = super(PicasoSerial, self).definitions()
        definitions['CloseComm'] = [None, []]
        definitions['busIn'] = [c_uint16, []]
        definitions['busOut'] = [None, [c_uint16]]
        definitions['busRead'] = [c_uint16, []]
        definitions['busSet'] = [None, [c_uint16]]
        definitions['busWrite'] = [None, [c_uint16]]
        definitions['putStr'] = [c_uint16, [c_char_p]]
        return definitions
