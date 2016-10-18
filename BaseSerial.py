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
from BaseConstants import *

class BaseSerial(object):

    _prototypes = {}

    def definitions(self):

        return {

            'blitComtoDisplay': [None, [c_uint16, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]],
            'OpenComm': [c_int, [c_char_p, c_int]],
            'putCH': [None, [c_uint16]],
            'readString': [c_uint16, [c_uint16, c_char_p]],
            'setbaudWait': [None, [c_uint16]],
            'writeString': [c_uint16, [c_uint16, c_char_p]],

            'charheight': [c_uint16, [c_char]],
            'charwidth': [c_uint16, [c_char]],

            'file_CallFunction': [c_uint16, [c_uint16, c_uint16, POINTER(c_uint16)]],
            'file_Close': [c_uint16, [c_uint16]],
            'file_Count': [c_uint16, [c_char_p]],
            'file_Dir': [c_uint16, [c_char_p]],
            'file_Erase': [c_uint16, [c_char_p]],
            'file_Error': [c_uint16, []],
            'file_Exec': [c_uint16, [c_char_p, c_uint16, POINTER(c_uint16)]],
            'file_Exists': [c_uint16, [c_char_p]],
            'file_FindFirst': [c_uint16, [c_char_p]],
            'file_FindFirstRet': [c_uint16, [c_char_p, c_char_p]],
            'file_FindNext': [c_uint16, []],
            'file_FindNextRet': [c_uint16, [c_char_p]],
            'file_GetC': [c_char, [c_uint16]],
            'file_GetS': [c_uint16, [c_char_p, c_uint16, c_uint16]],
            'file_GetW': [c_uint16, [c_uint16]],
            'file_Image': [c_uint16, [c_uint16, c_uint16, c_uint16]],
            'file_Index': [c_uint16, [c_uint16, c_uint16, c_uint16, c_uint16]],
            'file_LoadFunction': [c_uint16, [c_char_p]],
            'file_LoadImageControl': [c_uint16, [c_char_p, c_char_p, c_uint16]],
            'file_Mount': [c_uint16, []],
            'file_Open': [c_uint16, [c_char_p, c_char]],
            'file_PlayWAV': [c_uint16, [c_char_p]],
            'file_PutC': [c_uint16, [c_char, c_uint16]],
            'file_PutS': [c_uint16, [c_char_p, c_uint16]],
            'file_PutW': [c_uint16, [c_uint16, c_uint16]],
            'file_Read': [c_uint16, [POINTER(c_uint16), c_uint16, c_uint16]],
            'file_Rewind': [c_uint16, [c_uint16]],
            'file_Run': [c_uint16, [c_char_p, c_uint16, POINTER(c_uint16)]],
            'file_ScreenCapture': [c_uint16, [c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]],
            'file_Seek': [c_uint16, [c_uint16, c_uint16, c_uint16]],
            'file_Size': [c_uint16, [c_uint16, POINTER(c_uint16), POINTER(c_uint16)]],
            'file_Tell': [c_uint16, [c_uint16, POINTER(c_uint16), POINTER(c_uint16)]],
            'file_Unmount': [None, []],
            'file_Write': [c_uint16, [c_uint16, POINTER(c_uint8), c_uint16]],

            'gfx_BevelShadow': [c_uint16, [c_uint16]],
            'gfx_BevelWidth': [c_uint16, [c_uint16]],
            'gfx_BGcolour': [c_uint16, [c_uint16]],
            'gfx_Button': [None, [c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_char_p]],
            'gfx_ChangeColour': [None, [c_uint16, c_uint16]],
            'gfx_CircleFilled': [None, [c_uint16, c_uint16, c_uint16, c_uint16]],
            'gfx_Circle': [None, [c_uint16, c_uint16, c_uint16, c_uint16]],
            'gfx_Clipping': [None, [c_uint16]],
            'gfx_ClipWindow': [None, [c_uint16, c_uint16, c_uint16, c_uint16]],
            'gfx_Cls': [None, []],
            'gfx_Contrast': [c_uint16, [c_uint16]],
            'gfx_EllipseFilled': [None, [c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]],
            'gfx_Ellipse': [None, [c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]],
            'gfx_FrameDelay': [c_uint16, [c_uint16]],
            'gfx_Get': [c_uint16, [c_uint16]],
            'gfx_GetPixel': [c_uint16, [c_uint16, c_uint16]],
            'gfx_Line': [None, [c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]],
            'gfx_LinePattern': [c_uint16, [c_uint16]],
            'gfx_LineTo': [None, [c_uint16, c_uint16]],
            'gfx_MoveTo': [None, [c_uint16, c_uint16]],
            'gfx_Orbit': [c_uint16, [c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]],
            'gfx_OutlineColour': [c_uint16, [c_uint16]],
            'gfx_Panel': [None, [c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]],
            'gfx_PolygonFilled': [None, [c_uint16, POINTER(c_uint16), POINTER(c_uint16), c_uint16]],
            'gfx_Polygon': [None, [c_uint16, POINTER(c_uint16), POINTER(c_uint16), c_uint16]],
            'gfx_Polyline': [None, [c_uint16, POINTER(c_uint16), POINTER(c_uint16), c_uint16]],
            'gfx_PutPixel': [None, [c_uint16, c_uint16, c_uint16]],
            'gfx_RectangleFilled': [None, [c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]],
            'gfx_Rectangle': [None, [c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]],
            'gfx_ScreenCopyPaste': [None, [c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]],
            'gfx_ScreenMode': [c_uint16, [c_uint16]],
            'gfx_SetClipRegion': [None, []],
            'gfx_Set': [None, [c_uint16, c_uint16]],
            'gfx_Slider': [c_uint16, [c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]],
            'gfx_Transparency': [c_uint16, [c_uint16]],
            'gfx_TransparentColour': [c_uint16, [c_uint16]],
            'gfx_TriangleFilled': [None, [c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]],
            'gfx_Triangle': [None, [c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]],

            'img_ClearAttributes': [c_uint16, [c_uint16, c_uint16, c_uint16]],
            'img_Darken': [c_uint16, [c_uint16, c_uint16]],
            'img_Disable': [c_uint16, [c_uint16, c_uint16]],
            'img_Enable': [c_uint16, [c_uint16, c_uint16]],
            'img_GetWord': [c_uint16, [c_uint16, c_uint16, c_uint16]],
            'img_Lighten': [c_uint16, [c_uint16, c_uint16]],
            'img_SetAttributes': [c_uint16, [c_uint16, c_uint16, c_uint16]],
            'img_SetPosition': [c_uint16, [c_uint16, c_uint16, c_uint16, c_uint16]],
            'img_SetWord': [c_uint16, [c_uint16, c_uint16, c_uint16, c_uint16]],
            'img_Show': [c_uint16, [c_uint16, c_uint16]],
            'img_Touched': [c_uint16, [c_uint16, c_uint16]],

            'media_Flush': [c_uint16, []],
            'media_Image': [None, [c_uint16, c_uint16]],
            'media_Init': [c_uint16, []],
            'media_RdSector': [c_uint16, [c_char_p]],
            'media_ReadByte': [c_uint16, []],
            'media_ReadWord': [c_uint16, []],
            'media_SetAdd': [None, [c_uint16, c_uint16]],
            'media_SetSector': [None, [c_uint16, c_uint16]],
            'media_VideoFrame': [None, [c_uint16, c_uint16, c_uint16]],
            'media_Video': [None, [c_uint16, c_uint16]],
            'media_WriteByte': [c_uint16, [c_uint16]],
            'media_WriteWord': [c_uint16, [c_uint16]],
            'media_WrSector': [c_uint16, [c_char_p]],

            'mem_Free': [c_uint16, [c_uint16]],
            'mem_Heap': [c_uint16, []],
            'peekM': [c_uint16, [c_uint16]],
            'pokeM': [None, [c_uint16, c_uint16]],

            'pin_HI': [c_uint16, [c_uint16]],
            'pin_LO': [c_uint16, [c_uint16]],
            'pin_Read': [c_uint16, [c_uint16]],
            'pin_Set': [c_uint16, [c_uint16, c_uint16]],

            'snd_BufSize': [None, [c_uint16]],
            'snd_Continue': [None, []],
            'snd_Pause': [None, []],
            'snd_Pitch': [c_uint16, [c_uint16]],
            'snd_Playing': [c_uint16, []],
            'snd_Stop': [None, []],
            'snd_Volume': [None, [c_uint16]],

            'sys_GetModel': [c_uint16, [c_char_p]],
            'sys_GetPmmC': [c_uint16, []],
            'sys_GetVersion': [c_uint16, []],
            'sys_Sleep': [c_uint16, [c_uint16]],

            'touch_DetectRegion': [None, [c_uint16, c_uint16, c_uint16, c_uint16]],
            'touch_Get': [c_uint16, [c_uint16]],
            'touch_Set': [None, [c_uint16]],

            'txt_Attributes': [c_uint16, [c_uint16]],
            'txt_BGcolour': [c_uint16, [c_uint16]],
            'txt_Bold': [c_uint16, [c_uint16]],
            'txt_FGcolour': [c_uint16, [c_uint16]],
            'txt_FontID': [c_uint16, [c_uint16]],
            'txt_Height': [c_uint16, [c_uint16]],
            'txt_Inverse': [c_uint16, [c_uint16]],
            'txt_Italic': [c_uint16, [c_uint16]],
            'txt_MoveCursor': [None, [c_uint16, c_uint16]],
            'txt_Opacity': [c_uint16, [c_uint16]],
            'txt_Set': [None, [c_uint16, c_uint16]],
            'txt_Underline': [c_uint16, [c_uint16]],
            'txt_Width': [c_uint16, [c_uint16]],
            'txt_Wrap': [c_uint16, [c_uint16]],
            'txt_Xgap': [c_uint16, [c_uint16]],
            'txt_Ygap': [c_uint16, [c_uint16]],

        }

    def library(self):
        return False

    def __init__(self, timeout = 2000, abortOnError = True, callback = None):

        libdiabloSerial = self.library()
        if not libdiabloSerial:
            raise Exception('Trying to instantiate an astract class')

        definitions = self.definitions()

        for name in definitions:
            prototype = libdiabloSerial[name]
            prototype.restype = definitions[name][0]
            prototype.argtypes = definitions[name][1]
            self._prototypes[name] = prototype

        c_int.in_dll(libdiabloSerial, 'TimeLimit4D').value = timeout
        c_int.in_dll(libdiabloSerial, 'Error_Abort4D').value = int(abortOnError)

        if callback:
            callback_prototype = CFUNCTYPE(c_int, c_int, c_uint8)
            callback_prototype.in_dll(libdiabloSerial, 'Callback4D').value = callback_prototype(callback)

    def __getattr__(self, name):
        if name in self._prototypes:
            return self._prototypes[name]
        return False

    def OpenComm(self, port, baudrate=9600):
        return self._prototypes['OpenComm'](port, baudrate)

    def blitComtoDisplay(self, x, y, width, height, data):
        array_type = c_uint16 * (width * height);
        return self._prototypes['blitComtoDisplay'](x, y, width, height, array_type(*data))

    def file_CallFunction(self, filename, arguments):
        argcount = len(arguments)
        array_type = c_uint16 * argcount
        return self._prototypes['file_CallFunction'](filename, c_uint16(argcount), array_type(*arguments))

    def file_Exec(self, filename, arguments):
        argcount = len(arguments)
        array_type = c_uint16 * argcount
        return self._prototypes['file_Exec'](filename, c_uint16(argcount), array_type(*arguments))

    def file_Read(self, size, handle):
        buffer = create_string_buffer(size)
        ret = self._prototypes['file_Read'](buffer, size, handle)
        return buffer.raw

    def file_Run(self, filename, arguments):
        argcount = len(arguments)
        array_type = c_uint16 * argcount
        return self._prototypes['file_Run'](filename, c_uint16(argcount), array_type(*arguments))

    def file_Size(self, handle):
        hi = c_uint16()
        lo = c_uint16()
        self._prototypes['file_Size'](handle, byref(hi), byref(lo))
        return lo + hi << 16

    def file_Tell(self, handle):
        hi = c_uint16()
        lo = c_uint16()
        self._prototypes['file_Tell'](handle, byref(hi), byref(lo))
        return lo + hi << 16

    def file_Write(self, text, handle):
        size = len(text)
        buffer = list(text)
        array_type = c_uint8 * size
        return self._prototypes['file_Write'](c_uint16(size), array_type(*buffer), handle)

    def gfx_Orbit(self, angle, distance):
        x = c_uint16()
        y = c_uint16()
        self._prototypes['gfx_Orbit'](angle, distance, byref(x), byref(y))
        return [x.value, y.value]

    def gfx_Polygon(self, num, x, y, color):
        array_type = c_uint16 * num;
        return self._prototypes['gfx_Polygon'](num, array_type(*x), array_type(*y), color)

    def gfx_PolygonFilled(self, num, x, y, color):
        array_type = c_uint16 * num;
        return self._prototypes['gfx_PolygonFilled'](num, array_type(*x), array_type(*y), color)

    def gfx_Polyline(self, num, x, y, color):
        array_type = c_uint16 * num;
        return self._prototypes['gfx_Polyline'](num, array_type(*x), array_type(*y), color)

    def sys_GetModel(self):
        model = create_string_buffer(30)
        ret = self._prototypes['sys_GetModel'](model)
        return model.raw
