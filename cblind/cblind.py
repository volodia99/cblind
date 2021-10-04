import sys
from cycler import cycler

import numpy as np
import scipy.special as ss
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from matplotlib import cm

from rich import print as rprint

PALETTES = ("rbscale", "rainbow", "huescale")
PALETTES_FULL = (*PALETTES,*tuple([i+"_r" for i in PALETTES]))

STYLES = {
    "solid" : (0, ()),
    "dashed" : (0, (5, 5)),
    "densely_dashed" : (0, (5, 1)),
    "loosely_dashed" : (0, (5, 10)),

    "dotted" : (0, (1, 5)),
    "densely_dotted" : (0, (1, 1)),
    "loosely_dotted" : (0, (1, 10)),

    "dashdotted" : (0, (3, 5, 1, 5)),
    "densely_dashdotted" : (0, (3, 1, 1, 1)),
    "loosely_dashdotted" : (0, (3, 10, 1, 10)),

    "dashdotdotted" : (0, (3, 5, 1, 5, 1, 5)),
    "densely_dashdotdotted" : (0, (3, 1, 1, 1, 1, 1)),
    "loosely_dashdotdotted" : (0, (3, 10, 1, 10, 1, 10)),
}

def print_warn(message):
    """
    adapted from idefix_cli (cmt robert)
    https://github.com/neutrinoceros/idefix_cli
    """
    rprint(f":eyes: [bold red]Warning[/] {message}", file=sys.stderr)

class Colorplots:
    def cblind(self, ncurves):
        stylescheme = [STYLES[key] for key in list(STYLES.keys())]
        stylescheme = stylescheme[0:ncurves]
        # stylescheme = [STYLES["solid"]]*ncurves
        prop_cycle = plt.rcParams['axes.prop_cycle']
        clist = prop_cycle.by_key()['color']
        if(ncurves<=4):
            colorscheme = ['#4477AA','#CC6677','#DDCC77','#117733']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves>4 and ncurves<=12):
            colorscheme = ['#332288','#88CCEE','#117733','#DDCC77','#CC6677','#AA4499','#44AA99','#999933','#882255','#661100','#6699CC','#AA4466']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves>12 and ncurves<=156):
            colorscheme = ['#332288','#88CCEE','#117733','#DDCC77','#CC6677','#AA4499','#44AA99','#999933','#882255','#661100','#6699CC','#AA4466']
            colorscheme = colorscheme[0:ncurves]
            plt.rcParams['axes.prop_cycle'] = cycler('linestyle', stylescheme)*cycler('color', colorscheme)
            print_warn("out of range [1-12]: changed the linestyle")
        else:
            colorscheme = clist
            print_warn("out of range [1-156]: coloblind mode deactivated")
        return(colorscheme, stylescheme)

    def huescale(self, ncurves, *args):
        stylescheme = [STYLES["solid"]]*ncurves
        #SET DEFAULT VALUES IF NO OPTIONAL ARGUMENT
        hue = "None"
        #OPTIONS
        possible_args = ("blue", "bluegreen", "green", "gold", "brown", "rose", "purple")
        for arg in args:
            if arg in possible_args:
                hue = arg
            else:
                raise NotImplementedError(
                    f"arg '{arg}' not implemented yet in huescale function"
                )

        if(ncurves<=3):
            if hue=='blue':
                colorscheme = ['#114477','#4477AA','#77AADD']
                plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
            if hue=='bluegreen':
                colorscheme = ['#117777','#44AAAA','#77CCCC']
                plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
            if hue=='green':
                colorscheme = ['#117744','#44AA77','#88CCAA']
                plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
            if hue=='gold':
                colorscheme = ['#777711','#AAAA44','#DDDD77']
                plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
            if hue=='brown':
                colorscheme = ['#774411','#AA7744','#DDAA77']
                plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
            if hue=='rose':
                colorscheme = ['#771122','#AA4455','#DD7788']
                plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
            if hue=='purple':
                colorscheme = ['#771155','#AA4488','#CC99BB']
                plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
            if hue=='None':
                colorscheme = ['#D95F0E','#FEC44F','#FFF7BC']
                plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)

        prop_cycle = plt.rcParams['axes.prop_cycle']
        clist = prop_cycle.by_key()['color']

        if(ncurves==4):
            colorscheme = ['#CC4C02','#FB9A29','#FED98E','#FFFBD5']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        if(ncurves==5):
            colorscheme = ['#993404','#D95F0E','#FB9A29','#FED98E','#FFFBD5']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        if(ncurves==6):
            colorscheme = ['#993404','#D95F0E','#FB9A29','#FEC44F','#FEE391','#FFFBD5']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        if(ncurves==7):
            colorscheme = ['#8C2D04','#CC4C02','#EC7014','#FB9A29','#FEC44F','#FEE391','#FFFBD5']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        if(ncurves==8):
            colorscheme = ['#8C2D04','#CC4C02','#EC7014','#FB9A29','#FEC44F','#FEE391','#FFF7BC','#FFFFE5']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        if(ncurves==9):
            colorscheme = ['#662506','#993404','#CC4C02','#EC7014','#FB9A29','#FEC44F','#FEE391','#FFF7BC','#FFFFE5']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        if(ncurves>3 and ncurves<=9 and hue!='None'):
            print_warn("only ocherscale for more than 3 plots")
        if(ncurves>9):
            colorscheme = clist
            print_warn("out of range [1-9]: coloblind mode deactivated")
        return(colorscheme, stylescheme)

    def rbscale(self, ncurves):
        stylescheme = [STYLES["solid"]]*ncurves
        prop_cycle=plt.rcParams['axes.prop_cycle']
        clist=prop_cycle.by_key()['color']

        if(ncurves==3):
            colorscheme = ['#99C7EC','#FFFAD2','#F5A275']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==4):
            colorscheme = ['#008BCE','#B4DDF7','#F9BD7E','#D03232']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==5):
            colorscheme = ['#008BCE','#B4DDF7','#FFFAD2','#F9BD7E','#D03232']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==6):
            colorscheme = ['#3A89C9','#99C7EC','#E6F5FE','#FFE3AA','#F5A275','#D24D3E']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==7):
            colorscheme = ['#3A89C9','#99C7EC','#E6F5FE','#FFFAD2','#FFE3AA','#F5A275','#D24D3E']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==8):
            colorscheme = ['#3A89C9','#77B7E5','#B4DDF7','#E6F5FE','#FFE3AA','#F9BD7E','#ED875E','#D24D3E']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==9):
            colorscheme = ['#3A89C9','#77B7E5','#B4DDF7','#E6F5FE','#FFFAD2','#FFE3AA','#F9BD7E','#ED875E','#D24D3E']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==10):
            colorscheme = ['#3D52A1','#3A89C9','#77B7E5','#B4DDF7','#E6F5FE','#FFE3AA','#F9BD7E','#ED875E','#D24D3E','#AE1C3E']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==11):
            colorscheme = ['#3D52A1','#3A89C9','#77B7E5','#B4DDF7','#E6F5FE','#FFFAD2','#FFE3AA','#F9BD7E','#ED875E','#D24D3E','#AE1C3E']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        else:
            colorscheme = clist
            print_warn("out of range [3-11]: coloblind mode deactivated")
        return(colorscheme, stylescheme)

    def rainbow(self, ncurves):
        stylescheme = [STYLES["solid"]]*ncurves
        prop_cycle=plt.rcParams['axes.prop_cycle']
        clist=prop_cycle.by_key()['color']

        if(ncurves==4):
            colorscheme = ['#404096','#57A3AD','#DEA73A','#D92120']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==5):
            colorscheme = ['#404096','#529DB7','#7DB874','#E39C37','#D92120']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==6):
            colorscheme = ['#404096','#498CC2','#63AD99','#BEBC48','#E68B33','#D92120']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==7):
            colorscheme = ['#781C81','#3F60AE','#539EB6','#6DB388','#CAB843','#E78532','#D92120']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==8):
            colorscheme = ['#781C81','#3F56A7','#4B91C0','#5FAA9F','#91BD61','#D8AF3D','#E77C30','#D92120']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==9):
            colorscheme = ['#781C81','#3F4EA1','#4683C1','#57A3AD','#6DB388','#B1BE4E','#DFA53A','#E7742F','#D92120']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==10):
            colorscheme = ['#781C81','#3F479B','#4277BD','#529DB7','#62AC9B','#86BB6A','#C7B944','#E39C37','#E76D2E','#D92120']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==11):
            colorscheme = ['#781C81','#404096','#416CB7','#4D95BE','#5BA7A7','#6EB387','#A1BE56','#D3B33F','#E59435','#E6682D','#D92120']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        elif(ncurves==12):
            colorscheme = ['#781C81','#413B93','#4065B1','#488BC2','#55A1B1','#63AD99','#7FB972','#B5BD4C','#D9AD3C','#E68E34','#E6642C','#D92120']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        else:
            colorscheme = clist
            print_warn("out of range [4-12]: coloblind mode deactivated")
        return(colorscheme, stylescheme)

    def monocolor(self, ncurves, *args):
        possible_args = ("b&w", "blue", "red", "yellow", "green", "purple")
        printing = "b&w"
        for arg in args:
            if arg in possible_args:
                printing = arg
            else:
                raise NotImplementedError(
                    f"arg '{arg}' not implemented yet in monocolor function"
                )

        if (printing=='b&w'):
            colorscheme=['black']*ncurves
        if (printing=='blue'):
            colorscheme=['#4477AA']*ncurves
        if (printing=='red'):
            colorscheme=['#CC6677']*ncurves
        if (printing=='yellow'):
            colorscheme=['#DDCC77']*ncurves
        if (printing=='green'):
            colorscheme=['#117733']*ncurves
        if (printing=='purple'):
            colorscheme=['#771155']*ncurves

        if printing in possible_args:
            stylescheme = [
                STYLES["solid"], 
                STYLES["dashed"], 
                STYLES["dotted"], 
                STYLES["dashdotted"], 
                STYLES["dashdotdotted"], 
                STYLES["densely_dashed"], 
                STYLES["densely_dotted"], 
                STYLES["densely_dashdotted"], 
                STYLES["densely_dashdotdotted"], 
                STYLES["loosely_dashed"], 
                STYLES["loosely_dotted"], 
                STYLES["loosely_dashdotted"], 
                STYLES["loosely_dashdotdotted"],
            ]
            if(ncurves>13):
                print_warn("maximum 13 different linestyles")
                stylescheme = stylescheme*int(np.ceil(ncurves/13))
            stylescheme = stylescheme[0:ncurves]
            default_cycler=(cycler(color=colorscheme)+cycler(linestyle=stylescheme))
            plt.rc('axes', prop_cycle=default_cycler)
        return(colorscheme,stylescheme)

def reversed_cmap(cmap, name = 'my_cmap_r', nbin=None):
    if nbin is None:
        nbin=256
    reverse = []                  
    k = []                          

    for key in cmap._segmentdata:    
        k.append(key)
        channel = cmap._segmentdata[key]
        data = []
        for t in channel:                    
            data.append((1-t[0],t[2],t[1]))            
        reverse.append(sorted(data))    

    LinearL = dict(zip(k,reverse))
    my_cmap_r = mcolors.LinearSegmentedColormap(name, LinearL, N=nbin) 
    return my_cmap_r

def _get_cbmap(palette, nbin=None):
    if nbin is None:
        nbin=256
    x=np.linspace(0.,1.,nbin)
    if palette not in PALETTES_FULL:
        raise NotImplementedError(
            f"palette '{palette}' not implemented yet in _get_cbmap function"
        )
    palette_tmp = palette
    if palette[-2:]=="_r":
        palette_tmp = palette[:-2]

    if palette_tmp=="rbscale":
        red=0.237-2.13*x+26.92*x**2-65.5*x**3+63.5*x**4-22.36*x**5
        green=((0.572+1.524*x-1.811*x**2)/(1.-0.291*x+0.1574*x**2))**2
        blue=(1./(1.579-4.03*x+12.92*x**2-31.4*x**3+48.6*x**4-23.36*x**5))
    elif palette_tmp=='rainbow':
        red = (0.472-0.567*x+4.05*x**2)/(1.+8.72*x-19.17*x**2+14.1*x**3)
        green = 0.108932-1.22635*x+27.284*x**2-98.577*x**3+163.3*x**4-131.395*x**5+40.634*x**6
        blue = 1./(1.97+3.54*x-68.5*x**2+243*x**3-297*x**4+125*x**5)
    elif palette_tmp=='huescale':
        red = 1.-0.392*(1.+ss.erf((x-0.869)/0.255))
        green = 1.021-0.456*(1.+ss.erf((x-0.527)/0.376))
        blue = 1.-0.493*(1.+ss.erf((x-0.272)/0.309))

    redline=[]
    greenline=[]
    blueline=[]
    for i in range(len(x)):
        redline.append((x[i],red[i],red[i]))
        greenline.append((x[i],green[i],green[i]))
        blueline.append((x[i],blue[i],blue[i]))

    cdict = {'red':   redline,
             'green': greenline,
             'blue': blueline}

    cbcmap = mcolors.LinearSegmentedColormap(f"{palette_tmp}", cdict, N=nbin)
    if palette[-2:]=="_r":
        cbcmap = reversed_cmap(cbcmap, name=f"{palette}_r", nbin=nbin)
    return(cbcmap)

def cbmap(palette=None, nbin=None):
    if palette not in PALETTES_FULL:
        palette = cm.get_cmap(palette, nbin)
    else:
        palette = _get_cbmap(palette, nbin)
    return palette

def mapping(fig, ax, data2d, palette=None, nbin=None):
    im=ax.imshow(data2d, cmap=cbmap(palette=palette, nbin=nbin), aspect='auto')
    fig.colorbar(im)

def test_cblind(ny):
    nx=100
    x=np.linspace(0,10, nx)
    y=np.zeros((ny,nx), dtype=int)
    color, linestyle = Colorplots().cblind(ny)

    fig, ax = plt.subplots()
    for i in range(ny):
        for j in range(nx):
            y[i][j]=x[j]+i
        # plt.plot(x,y[i], color[i], linewidth=2.0)
        ax.plot(x,y[i], linewidth=1.5)

    plt.show()

def test_huescale(ny, *args):
    nx=100
    x=np.linspace(0,10, nx)
    y=np.zeros((ny,nx), dtype=int)
    color, linestyle = Colorplots().huescale(ny, *args)

    fig, ax = plt.subplots()
    for i in range(ny):
        for j in range(nx):
            y[i][j]=x[j]+i
        # plt.plot(x,y[i], color[i], linewidth=2.0)
        ax.plot(x,y[i], linewidth=2.0)

    plt.show()

def test_rbscale(ny):
    nx=100
    x=np.linspace(0,10, nx)
    y=np.zeros((ny,nx), dtype=int)
    color, linestyle = Colorplots().rbscale(ny)

    fig, ax = plt.subplots()
    for i in range(ny):
        for j in range(nx):
            y[i][j]=x[j]+i
        # plt.plot(x,y[i], color[i], linewidth=2.0)
        ax.plot(x,y[i], linewidth=2.0)

    plt.show()

def test_rainbow(ny):
    nx=100
    x=np.linspace(0,10, nx)
    y=np.zeros((ny,nx), dtype=int)
    color, linestyle = Colorplots().rainbow(ny)

    fig, ax = plt.subplots()
    for i in range(ny):
        for j in range(nx):
            y[i][j]=x[j]+i
        # plt.plot(x,y[i], color[i], linewidth=2.0)
        ax.plot(x,y[i], linewidth=2.0)

    plt.show()

def test_monocolor(ny, *args):
    nx=100
    x=np.linspace(0,10, nx)
    y=np.zeros((ny,nx), dtype=int)
    color, linestyle = Colorplots().monocolor(ny, *args)

    fig, ax = plt.subplots()
    for i in range(ny):
        for j in range(nx):
            y[i][j]=x[j]+i
        # plt.plot(x,y[i], color[i], linewidth=2.0)
        ax.plot(x,y[i], linewidth=1.0)

    plt.show()

def test_mapping(palette=None,nbin=None):
    fig, ax = plt.subplots()

    r = np.arange(-np.pi, np.pi, 0.1)
    t = np.arange(0, 2*np.pi, 0.1)
    X, Y = np.meshgrid(r, t)
    data = np.cos(X) * np.sin(Y) * 10

    mapping(fig, ax, data, palette=palette, nbin=nbin)
    plt.show()
