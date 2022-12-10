import numpy as np
from matplotlib import pyplot as plt
plt.switch_backend('agg')
import random
import io,os
from matplotlib.figure import Figure
from flask import Response

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


def dec2bin(n):
    return "{0:b}".format(int(n))


def resolute(bit,resol, x):
    x = int(dec2bin(x))
    res = list(map(int, str(x)))
    fixed_res=res.copy()
    counter=0
    #for 16bit
    if (resol == 0):
        while counter <= 7:
            res.extend(fixed_res)
            if counter == 3:
                res.reverse()
            counter+=1
        del res[255:305]
        if(len(res)!=256):
            res.append(1)
            print(len(res))
        del resol,fixed_res
        bit=16
        shaper(res,bit)

    #32bit
    elif (resol == 2):
        while counter <= 20:
            res.extend(fixed_res)
            if counter> 10:
                res.reverse()
                random.shuffle(res)
            counter+=1
            if counter >= 17:
                res.extend(res)
        print(len(res))
        del res[16384:]
        if(len(res)!= 16384):
            res.append(1)
            print(len(res))
        del resol,fixed_res
        bit=128
        shaper(res,bit)

        #32bit
    elif (resol == 3):
        while counter <= 16:
            res.extend(fixed_res)
            if counter > 8:
                res.reverse()
                random.shuffle(res)
            counter+=1
            if counter >= 7:
                res.extend(res)            
        print(len(res))
        del res[262144:]
        if(len(res)!= 262144):
            res.append(1)
            print(len(res))
        del resol,fixed_res
        bit=512
        shaper(res,bit)


def shaper(res, bit):
    nump = np.array(res)                   
    del res
    new = np.reshape(nump, (bit,-1))
    # print(new)                           
    del nump
    img = plt.imshow(new, cmap=random.choice(cmap))
    plt.axis('off')
    plt.savefig('foo.png', bbox_inches='tight')
    del new



# x = input("Enter your phone number")
x = 9867981859
resol = 0
x = int(dec2bin(x))
res = list(map(int, str(x)))
bit=0
cmap = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']




# print("\nLength", len(res),"\n",)




