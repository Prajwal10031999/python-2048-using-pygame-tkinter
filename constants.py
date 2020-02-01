BLACK = (0,0,0)
RED = (255,0,0)
ORANGE = (255,152,0)
DEEP_ORANGE = (255,87,34)
BROWN = (121,85,72)
GREEN = (0,128,0)
L_GREEN = (139,195,74)
TEAL = (0,150,136)
BLUE  = (33,150,136)
PURPLE = (156,39,176)
PINK = (234,30,99)
DEEP_PURPLE = (103,58,183)


color_dict = {
    0:BLACK,
    2:RED,
    4:GREEN,
    8:PURPLE,
    16:DEEP_PURPLE,
    32:DEEP_ORANGE,
    64:TEAL,
    128:L_GREEN,
    256:PINK,
    512:ORANGE,
    1024:BLACK,
    2048:BROWN
}

def getColor(i):
    return color_dict[i]
