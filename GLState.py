ENGINE_TRUE = True
ENGINE_FALSE = False
ENGINE_2D = "2D"
ENGINE_3D = "3D"
ENGINE_NOTHING = None
ENGINE_ = "Engine"
ENGINE_STARTPOS = (0,0)


def ENGINE_STRING(string):
    return string

def ENGINE_VEC2(value1,value2):
    values = (value1,value2)
    return values

def ENGINE_VEC3(v1,v2,v3):
    values = (v1,v2,v3)
    return values

def ENGINE_IMAGE(image):
    return image

