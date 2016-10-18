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

//------------------------------------------------------------------------------
// Baud divisor rates for setbaud(n)
//------------------------------------------------------------------------------
MIDI = 9
BAUD_110 = 0
BAUD_300 = 1
BAUD_600 = 2
BAUD_1200 = 3
BAUD_2400 = 4
BAUD_4800 = 5
BAUD_9600 = 6
BAUD_14400 = 7
BAUD_19200 = 8
BAUD_31250 = 9
BAUD_38400 = 10
BAUD_56000 = 11
BAUD_57600 = 12
BAUD_115200 = 13
BAUD_128000 = 14
BAUD_256000 = 15
BAUD_300000 = 16
BAUD_375000 = 17
BAUD_500000 = 18
BAUD_600000 = 19

//------------------------------------------------------------------------------
// Generic constants
//------------------------------------------------------------------------------
ENABLE = 1
DISABLE = 0
HI = 1
LO = 0
INPUT = 1
OUTPUT = 0
ON = 1
OFF = 0

//------------------------------------------------------------------------------
// Pin related constants
//------------------------------------------------------------------------------
IO1_PIN = 1
IO2_PIN = 2
IO3_PIN = 3
IO4_PIN = 4
IO5_PIN = 5
BUS_RD_PIN = 4
BUS_WR_PIN = 5
BACKLITE = 6
AUDIO_ENABLE = 7
BUS_0 = 8
BUS_1 = 9
BUS_2 = 10
BUS_3 = 11
BUS_4 = 12
BUS_5 = 13
BUS_6 = 14
BUS_7 = 15

//------------------------------------------------------------------------------
// gfx_Set() related constants
//------------------------------------------------------------------------------
PEN_SIZE = 16
BACKGROUND_COLOUR = 17
OBJECT_COLOUR = 18
CLIPPING = 19
TRANSPARENT_COLOUR = 20
TRANSPARENCY = 21
FRAME_DELAY = 22
SCREEN_MODE = 23
OUTLINE_COLOUR = 24
CONTRAST = 25
LINE_PATTERN = 26
COLOUR_MODE = 27
BEVEL_WIDTH = 28
BEVEL_SHADOW = 29
X_ORIGIN = 30
Y_ORIGIN = 31

//------------------------------------------------------------------------------
// gfx_Get() related constants
//------------------------------------------------------------------------------
X_MAX = 0
Y_MAX = 1
LEFT_POS = 2
TOP_POS = 3
RIGHT_POS = 4
BOTTOM_POS = 5
X_ORG = 6
Y_ORG = 7

SOLID = 0
OUTLINE = 1
STYLE1 = 2
STYLE2 = 3

LANDSCAPE = 0
LANDSCAPE_R = 1
PORTRAIT = 2
PORTRAIT_R = 3

COLOUR8 = 1
COLOUR16 = 0

DOWN = 0
UP = 1
HIDE = 2
SELECT = 3
SELECT_MULTIPLE = 4

BUTTON_DOWN = 0
BUTTON_UP = 1

SLIDER_SUNKEN = 0
SLIDER_RAISED = 1
SLIDER_HIDE = 2

PROGRESSBAR_RAISED = 0xFFFF
PROGRESSBAR_SUNKEN = 0xFFFE
PROGRESSBAR_HIDE = 2

PANEL_SUNKEN = 0
PANEL_RAISED = 1
PANEL_HIDE = 2

//------------------------------------------------------------------------------
// txt_Set() related constants
//------------------------------------------------------------------------------
TEXT_COLOUR = 0
TEXT_BACKGROUND = 1
TEXT_HIGHLIGHT = 1
FONT_ID = 2
FONT_SIZE = 2
TEXT_WIDTH = 3
TEXT_HEIGHT = 4
TEXT_XGAP = 5
TEXT_YGAP = 6
TEXT_PRINTDELAY = 7
TEXT_OPACITY = 8
TEXT_BOLD = 9
TEXT_ITALIC = 10
TEXT_INVERSE = 11
TEXT_UNDERLINED = 12
TEXT_ATTRIBUTES = 13
TEXT_WRAP = 14

//------------------------------------------------------------------------------
// txt_Set() related arguments
// NB:- FONT4 must be inherited if required,
// eg #inherit "FONT4.fnt"
//------------------------------------------------------------------------------
FONT1 = 0
FONT2 = 1
FONT3 = 2

TRANSPARENT = 0
OPAQUE = 1

BOLD = 16
ITALIC = 32
INVERSE = 64
UNDERLINED = 128

//------------------------------------------------------------------------------
// touch_Set() related constants
//------------------------------------------------------------------------------
TOUCH_ENABLE = 0
TOUCH_DISABLE = 1
TOUCH_REGIONDEFAULT = 2

//------------------------------------------------------------------------------
// touch_Get() related constants
//------------------------------------------------------------------------------
TOUCH_STATUS = 0
TOUCH_GETX = 1
TOUCH_GETY = 2
NOTOUCH = 0
TOUCH_PRESSED = 1
TOUCH_RELEASED = 2
TOUCH_MOVING = 3

//------------------------------------------------------------------------------
// Image control offset related constants
//------------------------------------------------------------------------------
IMG_COUNT = 0
IMG_ENTRYLEN = 1
IMG_MODE = 2
IMG_GCI_FILENAME = 3
IMG_DAT_FILENAME = 4
IMG_GCIFILE_HANDLE = 5

//------------------------------------------------------------------------------
// Image attribute flags
// for img_SetAttributes(...) and img_ClearAttributes(...)
//------------------------------------------------------------------------------
I_ENABLED = 0x8000
I_DARKEN = 0x4000
I_LIGHTEN = 0x2000
I_TOUCHED = 0x1000
I_Y_LOCK = 0x0800
I_X_LOCK = 0x0400
I_TOPMOST = 0x0200
I_STAYONTOP = 0x0100
I_MOVIE = 0x0080
I_NOGROUP = 0x0040
I_TOUCH_DISABLE = 0x0020
I_COLOUR16 = 0x0010

ALL = 0xFFFF

//------------------------------------------------------------------------------
// Image control entry offsets
//------------------------------------------------------------------------------
IMAGE_LOWORD = 0
IMAGE_HIWORD = 1
IMAGE_XPOS = 2
IMAGE_YPOS = 3
IMAGE_WIDTH = 4
IMAGE_HEIGHT = 5
IMAGE_FLAGS = 6
IMAGE_DELAY = 7
IMAGE_FRAMES = 8
IMAGE_INDEX = 9
IMAGE_CLUSTER = 10
IMAGE_SECTOR = 11
IMAGE_TAG = 12
IMAGE_TAG2 = 13

//------------------------------------------------------------------------------
// DISK struct offsets
//------------------------------------------------------------------------------
DISK_FIRST_SECT_LO = 0
DISK_FIRST_SECT_HI = 1
DISK_FAT_LO = 2
DISK_FAT_HI = 3
DISK_ROOT_LO = 4
DISK_ROOT_HI = 5
DISK_DATA_LO = 6
DISK_DATA_HI = 7
DISK_MAXCLUS_LO = 8
DISK_MAXCLUS_HI = 9
DISK_MAXROOT = 10
DISK_FATSIZE = 11
DISK_FATCOPIES = 12
DISK_SECT_PER_CLUS = 13
DISK_TYPE = 14
DISK_BUF = 15

//------------------------------------------------------------------------------
// FILE struct offsets
//------------------------------------------------------------------------------
FILE_FIRST_CLUSTER = 0
FILE_CURR_CLUSTER = 1
FILE_CURR_SECTOR = 2
FILE_CURR_SECTOR_POS = 3
FILE_CURR_SECTOR_TOP = 4
FILE_SEEK_POS_LO = 5
FILE_SEEK_POS_HI = 6
FILE_SIZE_LO = 7
FILE_SIZE_HI = 8
FILE_TIME = 9
FILE_DATE = 10
FILE_NAME = 11
FILE_MODE = 17
FILE_ATTRIBUTES = 18
FILE_PAGEFLAG = 19
FILE_ENTRY = 20
FILE_DISK = 21
FILE_BUFFER = 22

//------------------------------------------------------------------------------
// Timer control related constants
//------------------------------------------------------------------------------
TIMER0 = 0
TIMER1 = 1
TIMER2 = 2
TIMER3 = 3
TIMER4 = 4
TIMER5 = 5
TIMER6 = 6
TIMER7 = 7

//------------------------------------------------------------------------------
// I2C timing related constants
//------------------------------------------------------------------------------
I2C_SLOW = 0
I2C_MED = 1
I2C_FAST = 2

//------------------------------------------------------------------------------
// spi_Init(...)  mode arguments
//------------------------------------------------------------------------------
SPI_SLOW = 2
SPI_MED = 1
SPI_FAST = 0
RXMODE_0 = 0
RXMODE_1 = 1
CKMODE_0 = 0
CKMODE_1 = 1
CKMODE_2 = 2
CKMODE_3 = 3

//------------------------------------------------------------------------------
// System WORD variables accesible with peekW and pokeW or pointer access
// Note that the txt_Set variables (0-15) and gfx_set variables (16-31)
// can also be accessed with peekW and pokeW
//------------------------------------------------------------------------------
RANDOM_LO = 32
RANDOM_HI = 33
SYSTEM_TIMER_LO = 34
SYSTEM_TIMER_HI = 35
TMR0 = 36
TMR1 = 37
TMR2 = 38
TMR3 = 39
TMR4 = 40
TMR5 = 41
TMR6 = 42
TMR7 = 43
SYS_X_MAX = 44
SYS_Y_MAX = 45
GFX_XMAX = 46
GFX_YMAX = 47
GFX_LEFT = 48
GFX_TOP = 49
GFX_RIGHT = 50
GFX_BOTTOM = 51
GFX_X1 = 52
GFX_Y1 = 53
GFX_X2 = 54
GFX_Y2 = 55
GFX_X_ORG = 56
GFX_Y_ORG = 57
GFX_HILITE_LINE = 58
GFX_LINE_COUNT = 59
GFX_LAST_SELECTION = 60
GFX_HILIGHT_BACKGROUND = 61
GFX_HILIGHT_FOREGROUND = 62
GFX_BUTTON_FOREGROUND = 63
GFX_BUTTON_BACKGROUND = 64
GFX_BUTTON_MODE = 65
GFX_TOOLBAR_HEIGHT = 66
GFX_STATUSBAR_HEIGHT = 67
GFX_LEFT_GUTTER_WIDTH = 68
GFX_RIGHT_GUTTER_WIDTH = 69
GFX_PIXEL_SHIFT = 70
GFX_RECT_X1 = 71
GFX_RECT_Y1 = 72
GFX_RECT_X2 = 73
GFX_RECT_Y2 = 74
GFX_THUMB_PERCENT = 75
GFX_THUMB_BORDER_DARK = 76
GFX_THUMB_BORDER_LIGHT = 77
TOUCH_XMINCAL = 78
TOUCH_YMINCAL = 79
TOUCH_XMAXCAL = 80
TOUCH_YMAXCAL = 81
IMG_WIDTH = 82
IMG_HEIGHT = 83
IMG_FRAME_DELAY = 84
IMG_FLAGS = 85
IMG_FRAME_COUNT = 86
IMG_PIXEL_COUNT_LO = 87
IMG_PIXEL_COUNT_HI = 88
IMG_CURRENT_FRAME = 89
MEDIA_ADDRESS_LO = 90
MEDIA_ADDRESS_HI = 91
MEDIA_SECTOR_LO = 92
MEDIA_SECTOR_HI = 93
MEDIA_SECTOR_COUNT = 94
TEXT_XPOS = 95
TEXT_YPOS = 96
TEXT_MARGIN = 97
TXT_FONT_ID = 98
TXT_FONT_MAX = 99
TXT_FONT_OFFSET = 100
TXT_FONT_WIDTH = 101
TXT_FONT_HEIGHT = 102
GFX_TOUCH_REGION_X1 = 103
GFX_TOUCH_REGION_Y1 = 104
GFX_TOUCH_REGION_X2 = 105
GFX_TOUCH_REGION_Y2 = 106
GFX_CLIP_LEFT_VAL = 107
GFX_CLIP_TOP_VAL = 108
GFX_CLIP_RIGHT_VAL = 109
GFX_CLIP_BOTTOM_VAL = 110
GFX_CLIP_LEFT = 111
GFX_CLIP_TOP = 112
GFX_CLIP_RIGHT = 113
GFX_CLIP_BOTTOM = 114
GRAM_PIXEL_COUNT_LO = 115
GRAM_PIXEL_COUNT_HI = 116
TOUCH_RAW_X = 117
TOUCH_RAW_Y = 118
GFX_LAST_CHAR_WIDTH = 119
GFX_LAST_CHAR_HEIGHT = 120
GFX_LAST_STR_WIDTH = 121
GFX_LAST_STR_HEIGHT = 122

//------------------------------------------------------------------------------
// FILEIO Error Code Constants
//------------------------------------------------------------------------------
FE_OK = 0
FE_IDE_ERROR = 1
FE_NOT_PRESENT = 2
FE_PARTITION_TYPE = 3
FE_INVALID_MBR = 4
FE_INVALID_BR = 5
FE_DISK_NOT_MNTD = 6
FE_FILE_NOT_FOUND = 7
FE_INVALID_FILE = 8
FE_FAT_EOF = 9
FE_EOF = 10
FE_INVALID_CLUSTER = 11
FE_DIR_FULL = 12
FE_DISK_FULL = 13
FE_FILE_OVERWRITE = 14
FE_CANNOT_INIT = 15
FE_CANNOT_READ_MBR = 16
FE_MALLOC_FAILED = 17
FE_INVALID_MODE = 18
FE_FIND_ERROR = 19
FE_INVALID_FNAME = 20
FE_INVALID_MEDIA = 21
FE_SECTOR_READ_FAIL = 22
FE_SECTOR_WRITE_FAIL = 23

//------------------------------------------------------------------------------
// 16 bit RGB (565) Colour Chart
// Original work by 4D Forum Member: skadoo
//------------------------------------------------------------------------------

ALICEBLUE = 0xF7DF
ANTIQUEWHITE = 0xFF5A
AQUA = 0x07FF
AQUAMARINE = 0x7FFA
AZURE = 0xF7FF
BEIGE = 0xF7BB
BISQUE = 0xFF38
BLACK = 0x0000
BLANCHEDALMOND = 0xFF59
BLUE = 0x001F
BLUEVIOLET = 0x895C
BROWN = 0xA145
BURLYWOOD = 0xDDD0
CADETBLUE = 0x5CF4
CHARTREUSE = 0x7FE0
CHOCOLATE = 0xD343
CORAL = 0xFBEA
CORNFLOWERBLUE = 0x64BD
CORNSILK = 0xFFDB
CRIMSON = 0xD8A7
CYAN = 0x07FF
DARKBLUE = 0x0011
DARKCYAN = 0x0451
DARKGOLDENROD = 0xBC21
DARKGRAY = 0xAD55
DARKGREEN = 0x0320
DARKKHAKI = 0xBDAD
DARKMAGENTA = 0x8811
DARKOLIVEGREEN = 0x5345
DARKORANGE = 0xFC60
DARKORCHID = 0x9999
DARKRED = 0x8800
DARKSALMON = 0xECAF
DARKSEAGREEN = 0x8DF1
DARKSLATEBLUE = 0x49F1
DARKSLATEGRAY = 0x2A69
DARKTURQUOISE = 0x067A
DARKVIOLET = 0x901A
DEEPPINK = 0xF8B2
DEEPSKYBLUE = 0x05FF
DIMGRAY = 0x6B4D
DODGERBLUE = 0x1C9F
FIREBRICK = 0xB104
FLORALWHITE = 0xFFDE
FORESTGREEN = 0x2444
FUCHSIA = 0xF81F
GAINSBORO = 0xDEFB
GHOSTWHITE = 0xFFDF
GOLD = 0xFEA0
GOLDENROD = 0xDD24
GRAY = 0x8410
GREEN = 0x0400
GREENYELLOW = 0xAFE5
HONEYDEW = 0xF7FE
HOTPINK = 0xFB56
INDIANRED = 0xCAEB
INDIGO = 0x4810
IVORY = 0xFFFE
KHAKI = 0xF731
LAVENDER = 0xE73F
LAVENDERBLUSH = 0xFF9E
LAWNGREEN = 0x7FE0
LEMONCHIFFON = 0xFFD9
LIGHTBLUE = 0xAEDC
LIGHTCORAL = 0xF410
LIGHTCYAN = 0xE7FF
LIGHTGOLD = 0xFFDA
LIGHTGREEN = 0x9772
LIGHTGREY = 0xD69A
LIGHTPINK = 0xFDB8
LIGHTSALMON = 0xFD0F
LIGHTSEAGREEN = 0x2595
LIGHTSKYBLUE = 0x867F
LIGHTSLATEGRAY = 0x7453
LIGHTSTEELBLUE = 0xB63B
LIGHTYELLOW = 0xFFFC
LIME = 0x07E0
LIMEGREEN = 0x3666
LINEN = 0xFF9C
MAGENTA = 0xF81F
MAROON = 0x8000
MEDIUMAQUAMARINE = 0x6675
MEDIUMBLUE = 0x0019
MEDIUMORCHID = 0xBABA
MEDIUMPURPLE = 0x939B
MEDIUMSEAGREEN = 0x3D8E
MEDIUMSLATEBLUE = 0x7B5D
MEDIUMSPRINGGREEN = 0x07D3
MEDIUMTURQUOISE = 0x4E99
MEDIUMVIOLETRED = 0xC0B0
MIDNIGHTBLUE = 0x18CE
MINTCREAM = 0xF7FF
MISTYROSE = 0xFF3C
MOCCASIN = 0xFF36
NAVAJOWHITE = 0xFEF5
NAVY = 0x0010
OLDLACE = 0xFFBC
OLIVE = 0x8400
OLIVEDRAB = 0x6C64
ORANGE = 0xFD20
ORANGERED = 0xFA20
ORCHID = 0xDB9A
PALEGOLDENROD = 0xEF55
PALEGREEN = 0x9FD3
PALETURQUOISE = 0xAF7D
PALEVIOLETRED = 0xDB92
PAPAYAWHIP = 0xFF7A
PEACHPUFF = 0xFED7
PERU = 0xCC27
PINK = 0xFE19
PLUM = 0xDD1B
POWDERBLUE = 0xB71C
PURPLE = 0x8010
RED = 0xF800
ROSYBROWN = 0xBC71
ROYALBLUE = 0x435C
SADDLEBROWN = 0x8A22
SALMON = 0xFC0E
SANDYBROWN = 0xF52C
SEAGREEN = 0x2C4A
SEASHELL = 0xFFBD
SIENNA = 0xA285
SILVER = 0xC618
SKYBLUE = 0x867D
SLATEBLUE = 0x6AD9
SLATEGRAY = 0x7412
SNOW = 0xFFDF
SPRINGGREEN = 0x07EF
STEELBLUE = 0x4416
TAN = 0xD5B1
TEAL = 0x0410
THISTLE = 0xDDFB
TOMATO = 0xFB08
TURQUOISE = 0x471A
VIOLET = 0xEC1D
WHEAT = 0xF6F6
WHITE = 0xFFFF
WHITESMOKE = 0xF7BE
YELLOW = 0xFFE0
YELLOWGREEN = 0x9E66
