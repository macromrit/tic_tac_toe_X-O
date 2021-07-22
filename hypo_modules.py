#importing numpy
try:
    from numpy import *
except:
    print('error-> phase-I')

def first_row(z: array) -> bool:
    if z[0, 0] == z[0,1] == z[0, 2]:
        val = True
    else:
        val = False
    
    return val, z[0,0]

    
def second_row(z: array) -> bool:
    if z[1, 0] == z[1,1] == z[1, 2]:
        val = True
    else:
        val = False
    
    return val, z[1,0]

    
def third_row(z: array) -> bool:
    if z[2, 0] == z[2,1] == z[2, 2]:
        val = True
    else:
        val = False
    
    return val, z[2,0]

    
def first_clmn(z: array) -> bool:
    if z[0, 0] == z[1,0] == z[2, 0]:
        val = True
    else:
        val = False
    
    return val, z[0,0]

    
def second_clmn(z: array) -> bool:
    if z[0, 1] == z[1,1] == z[2, 1]:
        val = True
    else:
        val = False
    
    return val, z[0,1]

    
def third_clmn(z: array) -> bool:
    if z[0, 2] == z[1,2] == z[2, 2]:
        val = True
    else:
        val = False
    
    return val, z[0,2]

    
def left_diag(z: array) -> bool:
    if z[0, 0] == z[1,1] == z[2, 2]:
        val = True
    else:
        val = False
    
    return val, z[0,0]

    
def right_diag(z: array) -> bool:
    if z[0, 2] == z[1,1] == z[2, 0]:
        val = True
    else:
        val = False
    
    return val, z[0,2]


def swap_val_func(x: int,
            char: str,
            z: array) -> None:
    
    if x ==1:   
        z[0,0] = char
    
    elif x ==2:   
        z[0,1] = char
    
    elif x ==3:   
        z[0,2] = char
    
    elif x ==4:   
        z[1,0] = char
    
    elif x ==5:   
        z[1,1] = char

    elif x ==6:   
        z[1,2] = char

    elif x ==7:   
        z[2,0] = char

    elif x ==8:   
        z[2,1] = char
    
    elif x ==9:   
        z[2,2] = char
    
    else:
        pass

    return 