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

# ------------------------------------------------------------------------------
# txt_Set() related constants
# ------------------------------------------------------------------------------
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
TEXT_ANGLE = 15

# ------------------------------------------------------------------------------
# txt_Set() related arguments
# ------------------------------------------------------------------------------
FONT1 = 1
FONT2 = 2
FONT3 = 3

FONT_1 = 1
FONT_2 = 2
FONT_3 = 3
FONT_4 = 4
FONT_5 = 5
FONT_6 = 6
FONT_7 = 7
FONT_8 = 8
FONT_9 = 9
FONT_10 = 10
FONT_11 = 11

TRANSPARENT = 0
OPAQUE = 1

BOLD = 16
ITALIC = 32
INVERSE = 64
UNDERLINED = 128

# ------------------------------------------------------------------------------
# Single word array operations
# ------------------------------------------------------------------------------
OP1_NOP = 0
OP1_SET = 1
OP1_AND = 2
OP1_IOR = 3
OP1_XOR = 4
OP1_ADD = 5
OP1_SUB = 6
OP1_MUL = 7
OP1_DIV = 8
OP1_REV = 9
OP1_SHL = 10
OP1_SHR = 11
OP1_ROL = 12
OP1_ROR = 13

OP1_GRAY = 14
OP1_WHITEN = 15
OP1_BLACKEN = 16
OP1_LIGHTEN = 17
OP1_DARKEN = 18

# ------------------------------------------------------------------------------
# Dual word array operations
# ------------------------------------------------------------------------------
OP2_AND = 1
OP2_IOR = 2
OP2_XOR = 3
OP2_ADD = 4
OP2_SUB = 5
OP2_MUL = 6
OP2_DIV = 7
OP2_COPY = 8

OP2_BLEND = 9

# ------------------------------------------------------------------------------
# pin_Set(...) pin modes
# ------------------------------------------------------------------------------
PIN_INP = 0
PIN_INP_HI = 1
PIN_INP_LO = 2
PIN_OUT = 3
PIN_OUT_OD = 4
PIN_AN = 5
PIN_ANAVG = 6

# ------------------------------------------------------------------------------
# pin name
# ------------------------------------------------------------------------------
PA0 = 1
PA1 = 2
PA2 = 3
BUS_WR_PIN = 3
PA3 = 4
BUS_RD_PIN = 4
PA4 = 5
PA5 = 6
PA6 = 7
PA7 = 8
PA8 = 9
PA9 = 10
PA10 = 11
PA11 = 12
PA12 = 13
PA13 = 14
PA14 = 15
PA15 = 16
AUDIO_ENABLE = 17

# ------------------------------------------------------------------------------
# Bit position masks
# ------------------------------------------------------------------------------
M_PA0 = 0x0001
M_PA1 = 0x0002
M_PA2 = 0x0004
M_PA3 = 0x0008
M_PA4 = 0x0010
M_PA5 = 0x0020
M_PA6 = 0x0040
M_PA7 = 0x0080
M_PA8 = 0x0100
M_PA9 = 0x0200
M_PA10 = 0x0400
M_PA11 = 0x0800
M_PA12 = 0x1000
M_PA13 = 0x2000
M_PA14 = 0x4000
M_PA15 = 0x8000

# ------------------------------------------------------------------------------
# gfx_Set() related constants
# ------------------------------------------------------------------------------
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
BEVEL_RADIUS = 27
BEVEL_WIDTH = 28
BEVEL_SHADOW = 29
X_ORIGIN = 30
Y_ORIGIN = 31

# ------------------------------------------------------------------------------
# Built in fill pattern constants for function gfx_FillPattern
# ------------------------------------------------------------------------------
FILLPATTERN_0 = 0xFFE0
FILLPATTERN_1 = 0xFFE1
FILLPATTERN_2 = 0xFFE2
FILLPATTERN_3 = 0xFFE3
FILLPATTERN_4 = 0xFFE4
FILLPATTERN_5 = 0xFFE5
FILLPATTERN_6 = 0xFFE6
FILLPATTERN_7 = 0xFFE7
FILLPATTERN_8 = 0xFFE8
FILLPATTERN_9 = 0xFFE9
FILLPATTERN_10 = 0xFFEA
FILLPATTERN_11 = 0xFFEB
FILLPATTERN_12 = 0xFFEC
FILLPATTERN_13 = 0xFFED
FILLPATTERN_14 = 0xFFEE
FILLPATTERN_15 = 0xFFEF
FILLPATTERN_16 = 0xFFF0
FILLPATTERN_17 = 0xFFF1
FILLPATTERN_18 = 0xFFF2
FILLPATTERN_19 = 0xFFF3
FILLPATTERN_20 = 0xFFF4
FILLPATTERN_21 = 0xFFF5
FILLPATTERN_22 = 0xFFF6
FILLPATTERN_23 = 0xFFF7
FILLPATTERN_24 = 0xFFF8
FILLPATTERN_25 = 0xFFF9
FILLPATTERN_26 = 0xFFFA
FILLPATTERN_27 = 0xFFFB
FILLPATTERN_28 = 0xFFFC
FILLPATTERN_29 = 0xFFFD
FILLPATTERN_30 = 0xFFFE
FILLPATTERN_31 = 0xFFFF

PTN_EMPTY = 0xFFE0
PTN_SOLID = 0xFFE1
PTN_FINE_DOTS = 0xFFE2
PTN_MEDIUM_DOTS = 0xFFE3
PTN_COURSE_DOTS = 0xFFE4
PTN_BS_VERTICAL = 0xFFE5
PTN_BS_HORIZONTAL = 0xFFE6
PTN_COURSE_F_DIAGONAL = 0xFFE7
PTN_COURSE_B_DIAGONAL = 0xFFE8
PTN_COURSE_CROSS = 0xFFE9
PTN_COURSE_DIAGONALCROSS = 0xFFEA
PTN_BSVERTICAL = 0xFFEB
PTN_BSHORIZONTAL = 0xFFEC
PTN_FDIAGONAL = 0xFFED
PTN_BDIAGONAL = 0xFFEE
PTN_FINE_CROSS = 0xFFEF
PTN_FINE_DIAGONAL_CROSS = 0xFFF0
PTN_BRICKS = 0xFFF1
PTN_CARGONET = 0xFFF2
PTN_CIRCUITS = 0xFFF3
PTN_COBBLESTONES = 0xFFF4
PTN_DAISIES = 0xFFF5
PTN_DIZZY = 0xFFF6
PTN_FIELDEFFECT = 0xFFF7
PTN_KEY = 0xFFF8
PTN_ROUNDER = 0xFFF9
PTN_SCALES = 0xFFFA
PTN_STONE = 0xFFFB
PTN_THATCHES = 0xFFFC
PTN_TILE = 0xFFFD
PTN_WAFFLESREVENGE = 0xFFFE
PTN_CROSSES = 0xFFFF

# ------------------------------------------------------------------------------
# Gradient control constants
# ------------------------------------------------------------------------------
GRAD_DOWN = 0x20
GRAD_RIGHT = 0x30
GRAD_UP = 0x40
GRAD_LEFT = 0x50
GRAD_WAVE_VER = 0x60
GRAD_WAVE_HOR = 0x70

# ------------------------------------------------------------------------------
# Baud divisor rates for legacy setbaud(n);
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# I2C software emulation timing related constants
# ------------------------------------------------------------------------------
I2C_SLOW = 0
I2C_MED = 1
I2C_FAST = 2
I2C_10KHZ = 3
I2C_20HZ = 4
I2C_50KHZ = 5
I2C_250KHZ = 6

# ------------------------------------------------------------------------------
# Constants for SPI1, SPI2 an SPI3 "mode"
# ------------------------------------------------------------------------------
SPI8_MODE_0 = 0
SPI8_MODE_1 = 1
SPI8_MODE_2 = 2
SPI8_MODE_3 = 3
SPI8_MODE_4 = 4
SPI8_MODE_5 = 5
SPI8_MODE_6 = 6
SPI8_MODE_7 = 7
SPI16_MODE_0 = 8
SPI16_MODE_1 = 9
SPI16_MODE_2 = 10
SPI16_MODE_3 = 11
SPI16_MODE_4 = 12
SPI16_MODE_5 = 13
SPI16_MODE_6 = 14
SPI16_MODE_7 = 15

# ------------------------------------------------------------------------------
# Constants for SPI1, SPI2 an SPI3 "speed"
# ------------------------------------------------------------------------------
SPI_SPEED0 = 0
SPI_SPEED1 = 1
SPI_SPEED2 = 2
SPI_SPEED3 = 3
SPI_SPEED4 = 4
SPI_SPEED5 = 5
SPI_SPEED6 = 6
SPI_SPEED7 = 7
SPI_SPEED8 = 8
SPI_SPEED9 = 9
SPI_SPEED10 = 10
SPI_SPEED11 = 11
SPI_SPEED12 = 12
SPI_SPEED13 = 13
SPI_SPEED14 = 14
SPI_SPEED15 = 15

# ------------------------------------------------------------------------------
# Image control header offsets
# ------------------------------------------------------------------------------
IMG_COUNT = 0
IMG_ENTRYLEN = 1
IMG_MODE = 2
IMG_GCI_FILENAME = 3
IMG_DAT_FILENAME = 4
IMG_GCIFILE_HANDLE = 5

# ------------------------------------------------------------------------------
# Image control entry offsets
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Image attribute flags (in IMAGE_FLAGS)
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# touch_Set() related constants
# ------------------------------------------------------------------------------
TOUCH_ENABLE = 0
TOUCH_DISABLE = 1
TOUCH_REGIONDEFAULT = 2

# ------------------------------------------------------------------------------
# touch_Get() related constants
# ------------------------------------------------------------------------------
TOUCH_STATUS = 0
TOUCH_GETX = 1
TOUCH_GETY = 2
NOTOUCH = 0
TOUCH_PRESSED = 1
TOUCH_RELEASED = 2
TOUCH_MOVING = 3

# ------------------------------------------------------------------------------
# FILEIO Error Code Constants
# ------------------------------------------------------------------------------
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
FE_FILE_TIMEOUT = 26

# ------------------------------------------------------------------------------
# DISK struct offsets
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# FILE struct offsets
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Pin counter mode constants
# ------------------------------------------------------------------------------
COUNT_OFF = 0
COUNT_RISE = 1
COUNT_FALL = 2
COUNT_EDGE = 3

# ------------------------------------------------------------------------------
# PWM Constants
# ------------------------------------------------------------------------------
PWM_OFF = 0
PWM_PLAIN = 1
PWM_SERVO = 2

# ------------------------------------------------------------------------------
# Generic Constants
# ------------------------------------------------------------------------------
SPI1 = 1
SPI2 = 2
SPI3 = 3
ENABLE = 1
DISABLE = 0
HI = 1
LO = 0
ON = 1
OFF = 0
ALL = 0xFFFF

# ------------------------------------------------------------------------------
# gfx_Get() related constants
# ------------------------------------------------------------------------------
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

CHECKED = 0
UNCHECKED = 1

DOWN = 0
UP = 1
HIDE = 2
HYPER = 3

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
PANEL_FRAME = 3

# ------------------------------------------------------------------------------
# Timer control  related constants
# ------------------------------------------------------------------------------
TIMER0 = 0
TIMER1 = 1
TIMER2 = 2
TIMER3 = 3
TIMER4 = 4
TIMER5 = 5
TIMER6 = 6
TIMER7 = 7

# ------------------------------------------------------------------------------
#  System WORD variables accesible with peekW and pokeW or pointer access
#  Note that the txt_Set variables (0-15) and gfx_set variables (16-31)
#  can also be accessed with peekW and pokeW
# ------------------------------------------------------------------------------

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
PIN_COUNTER_PA4 = 123
PIN_COUNTER_PA5 = 124
PIN_COUNTER_PA6 = 125
PIN_COUNTER_PA7 = 126
PIN_COUNTER_PA8 = 127
PIN_COUNTER_PA9 = 128
PIN_EVENT_PA4 = 129
PIN_EVENT_PA5 = 130
PIN_EVENT_PA6 = 131
PIN_EVENT_PA7 = 132
PIN_EVENT_PA8 = 133
PIN_EVENT_PA9 = 134
QEN1_COUNTER_LO = 135
QEN1_COUNTER_HI = 136
QEN1_DELTA = 137
QEN2_COUNTER_LO = 138
QEN2_COUNTER_HI = 139
QEN2_DELTA = 140
FALSE_REASON = 141

# ------------------------------------------------------------------------------
# String processing constants
# ------------------------------------------------------------------------------
STR = 0x0080
CHR = 0x0081


# ============================================================================
# Number formatting bits
# ============================================================================
#  bit 15 14 13 12 11 10 9  8  7  6  5  4  3  2  1  0
#      |  |  |  |   \___ ___/  |  \  /  \_____ _____/
#      |  |  |  |       V      |   V          V
#      |  |  |  |       |      |   |          |
#      |  |  |  |  digit count |   |          |
#      |  |  |  |  (nb 0 = 16) |   |          |____BASE (usually 2,10 or 16)
#      |  |  |  |              |   |
#      |  |  |  |              |   |___reserved (not used on Goldelox)
#      |  |  |  |              |
#      |  |  |  |              |____ string indicatior
#      |  |  |  |                      0x80 = [STR]
#      |  |  |  |                      0x81 = [CHR]
#      |  |  |  |______
#      |  |  |           1 = leading zeros included
#      |  |  |           0 = leading zeros suppressed
#      |  |  |
#      |  |  |_______
#      |  |           1 = leading zero blanking
#      |  |
#      |  |_____ sign bit (0 = signed, 1 = unsigned)
#      |
#      |______ 1 = space before unsigned number

BIN = 0x0002
BIN1 = 0x0102
BIN2 = 0x0202
BIN3 = 0x0302
BIN4 = 0x0402
BIN5 = 0x0502
BIN6 = 0x0602
BIN7 = 0x0702
BIN8 = 0x0802
BIN9 = 0x0902
BIN10 = 0x0A02
BIN11 = 0x0B02
BIN12 = 0x0C02
BIN13 = 0x0D02
BIN14 = 0x0E02
BIN15 = 0x0F02
BIN16 = 0x0002

BINZ = 0x1002
BIN1Z = 0x1102
BIN2Z = 0x1202
BIN3Z = 0x1302
BIN4Z = 0x1402
BIN5Z = 0x1502
BIN6Z = 0x1602
BIN7Z = 0x1702
BIN8Z = 0x1802
BIN9Z = 0x1902
BIN10Z = 0x1A02
BIN11Z = 0x1B02
BIN12Z = 0x1C02
BIN13Z = 0x1D02
BIN14Z = 0x1E02
BIN15Z = 0x1F02
BIN16Z = 0x1002

BINZB = 0x2002
BIN1ZB = 0x2102
BIN2ZB = 0x2202
BIN3ZB = 0x2302
BIN4ZB = 0x2402
BIN5ZB = 0x2502
BIN6ZB = 0x2602
BIN7ZB = 0x2702
BIN8ZB = 0x2802
BIN9ZB = 0x2902
BIN10ZB = 0x2A02
BIN11ZB = 0x2B02
BIN12ZB = 0x2C02
BIN13ZB = 0x2D02
BIN14ZB = 0x2E02
BIN15ZB = 0x2F02
BIN16ZB = 0x2002

DEC = 0x050A
DEC1 = 0x010A
DEC2 = 0x020A
DEC3 = 0x030A
DEC4 = 0x040A
DEC5 = 0x050A

DECZ = 0x150A
DEC1Z = 0x110A
DEC2Z = 0x120A
DEC3Z = 0x130A
DEC4Z = 0x140A
DEC5Z = 0x150A

DECZB = 0x250A
DEC1ZB = 0x210A
DEC2ZB = 0x220A
DEC3ZB = 0x230A
DEC4ZB = 0x240A
DEC5ZB = 0x250A

UDEC = 0x450A
UDEC1 = 0x410A
UDEC2 = 0x420A
UDEC3 = 0x430A
UDEC4 = 0x440A
UDEC5 = 0x450A

UDECZ = 0x550A
UDEC1Z = 0x510A
UDEC2Z = 0x520A
UDEC3Z = 0x530A
UDEC4Z = 0x540A
UDEC5Z = 0x550A

UDECZB = 0x650A
UDEC1ZB = 0x610A
UDEC2ZB = 0x620A
UDEC3ZB = 0x630A
UDEC4ZB = 0x640A
UDEC5ZB = 0x650A

HEX = 0x1410
HEX1 = 0x1110
HEX2 = 0x1210
HEX3 = 0x1310
HEX4 = 0x1410

HEXZ = 0x0410
HEX1Z = 0x0110
HEX2Z = 0x0210
HEX3Z = 0x0310
HEX4Z = 0x0410

HEXZB = 0x2410
HEX1ZB = 0x2110
HEX2ZB = 0x2210
HEX3ZB = 0x2310
HEX4ZB = 0x2410

# ------------------------------------------------------------------------------
# 16 bit RGB (565) Colour Chart
# Original work by 4D Forum Member: skadoo
# ------------------------------------------------------------------------------

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
