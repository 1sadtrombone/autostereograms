import numpy as np
import matplotlib.pyplot as plt

from autostereogram.converter import StereogramConverter

def display(img):
    plt.clf()
    plt.imshow(img, interpolation='none', cmap='gray')

def make_pattern(shape=(16,16), levels=255):
    return np.random.randint(0, levels-1, shape)

def make_dm_square(height=255, shape=(600,800), corners=[(250, 350), (350, 450)]):

    dm = np.zeros(shape, dtype=int)
    x = np.arange(shape[0])
    y = np.arange(shape[1])
    xx, yy = np.meshgrid(x, y, indexing='ij')
    dm += (xx < corners[0][0]) * (xx > corners[1][0]) * (yy < corners[0][1]) * (yy > corners[1][1])
    dm *= height

    return dm

def make_dm_circle(height=255, shape=(600,800), r=100, center=None):

    if center == None:
        center = (shape[0]//2, shape[1]//2)
    
    dm = np.zeros(shape, dtype=int)
    x = np.arange(shape[0])
    y = np.arange(shape[1])
    xx, yy = np.meshgrid(x, y, indexing='ij')
    rr = np.sqrt((xx-center[0])**2 + (yy-center[1])**2)
    dm += (rr > r)
    dm *= height

    return dm
    
def make_asg(dm, converter):

    # for each row in dm
    #   for each column in dm
    #     if colnum < pattern width:
    #       asg[r,c] = pattern[r%pattern_height,c] # copy over pattern raw
    #     else:
    #       shift = int(dm[r,c] * amp * pattern_width) # so amp is in units of pat width
    #       # not sure if that's necessary
    #       asg[r,c] = asg[r, c - pattern_width + shift]

    pass


if __name__=="__main__":
    converter = StereogramConverter()
        
    plt.figure()
    
    display(converter.convert_depth_to_stereogram(make_dm_circle()))
    
    plt.show()
