import numpy as np
import matplotlib.pyplot as plt

import asg_maker
from autostereogram.converter import StereogramConverter

converter = StereogramConverter()

plt.ion()
fig = plt.figure()

N = 1000 # N frames total

hspeed = 5 # n depth units per frame

hs = np.arange(100, 200, hspeed,dtype=int)
dxs = np.arange(-50, 50, 100/hs.size, dtype=int)

hs = np.hstack((hs,np.flip(hs)))
dxs = np.hstack((dxs,np.flip(dxs)))

for i in range(hs.size*10):

    dm = asg_maker.make_dm_circle(height=hs[i%hs.size], center=(300, 400+dxs[i%dxs.size]))

    asg_maker.display(converter.convert_depth_to_stereogram(dm))
    fig.canvas.draw()
    fig.canvas.flush_events()

   
   
