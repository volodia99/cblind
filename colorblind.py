import numpy as np
import scipy.special as ss
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from cycler import cycler

def fccolorblind(number_of_plots):
    prop_cycle=plt.rcParams['axes.prop_cycle']
    clist=prop_cycle.by_key()['color']

    if(number_of_plots<=4):
        colorscheme=['#4477AA','#CC6677','#DDCC77','#117733']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots>4 and number_of_plots<=12):
        colorscheme=['#332288','#88CCEE','#117733','#DDCC77','#CC6677','#AA4499','#44AA99','#999933','#882255','#661100','#6699CC','#AA4466']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    else:
        colorscheme=clist
        print("OUT OF RANGE[1-12] : COLORBLIND MODE DEACTIVATED ---> DEFAULT MODE")
    return(colorscheme)

def huescale(number_of_plots, *option):
    #SET DEFAULT VALUES IF NO OPTIONAL ARGUMENT
    hue='None'
    #OPTIONS
    for argument in option:
        if argument=='blue':
            hue='blue'
        if argument=='bluegreen':
            hue='bluegreen'
        if argument=='green':
            hue='green'
        if argument=='gold':
            hue='gold'
        if argument=='brown':
            hue='brown'
        if argument=='rose':
            hue='rose'
        if argument=='purple':
            hue='purple'

    if(number_of_plots<=3):
        if hue=='blue':
            colorscheme=['#114477','#4477AA','#77AADD']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        if hue=='bluegreen':
            colorscheme=['#117777','#44AAAA','#77CCCC']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        if hue=='green':
            colorscheme=['#117744','#44AA77','#88CCAA']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        if hue=='gold':
            colorscheme=['#777711','#AAAA44','#DDDD77']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        if hue=='brown':
            colorscheme=['#774411','#AA7744','#DDAA77']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        if hue=='rose':
            colorscheme=['#771122','#AA4455','#DD7788']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        if hue=='purple':
            colorscheme=['#771155','#AA4488','#CC99BB']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
        if hue=='None':
            colorscheme=['#D95F0E','#FEC44F','#FFF7BC']
            plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)

    prop_cycle=plt.rcParams['axes.prop_cycle']
    clist=prop_cycle.by_key()['color']

    if(number_of_plots==4):
        colorscheme=['#CC4C02','#FB9A29','#FED98E','#FFFBD5']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    if(number_of_plots==5):
        colorscheme=['#993404','#D95F0E','#FB9A29','#FED98E','#FFFBD5']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    if(number_of_plots==6):
        colorscheme=['#993404','#D95F0E','#FB9A29','#FEC44F','#FEE391','#FFFBD5']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    if(number_of_plots==7):
        colorscheme=['#8C2D04','#CC4C02','#EC7014','#FB9A29','#FEC44F','#FEE391','#FFFBD5']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    if(number_of_plots==8):
        colorscheme=['#8C2D04','#CC4C02','#EC7014','#FB9A29','#FEC44F','#FEE391','#FFF7BC','#FFFFE5']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    if(number_of_plots==9):
        colorscheme=['#662506','#993404','#CC4C02','#EC7014','#FB9A29','#FEC44F','#FEE391','#FFF7BC','#FFFFE5']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    if(number_of_plots>3 and number_of_plots<=9 and hue!='None'):
        print("ONLY OCHERSCALE FOR MORE THAN 3 PLOTS")
    if(number_of_plots>9):
        colorscheme=clist
        print("OUT OF RANGE[1-9] : COLORBLIND MODE DEACTIVATED ---> DEFAULT MODE")
    return(colorscheme)

def rbscale(number_of_plots):
    prop_cycle=plt.rcParams['axes.prop_cycle']
    clist=prop_cycle.by_key()['color']

    if(number_of_plots==3):
        colorscheme=['#99C7EC','#FFFAD2','#F5A275']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==4):
        colorscheme=['#008BCE','#B4DDF7','#F9BD7E','#D03232']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==5):
        colorscheme=['#008BCE','#B4DDF7','#FFFAD2','#F9BD7E','#D03232']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==6):
        colorscheme=['#3A89C9','#99C7EC','#E6F5FE','#FFE3AA','#F5A275','#D24D3E']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==7):
        colorscheme=['#3A89C9','#99C7EC','#E6F5FE','#FFFAD2','#FFE3AA','#F5A275','#D24D3E']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==8):
        colorscheme=['#3A89C9','#77B7E5','#B4DDF7','#E6F5FE','#FFE3AA','#F9BD7E','#ED875E','#D24D3E']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==9):
        colorscheme=['#3A89C9','#77B7E5','#B4DDF7','#E6F5FE','#FFFAD2','#FFE3AA','#F9BD7E','#ED875E','#D24D3E']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==10):
        colorscheme=['#3D52A1','#3A89C9','#77B7E5','#B4DDF7','#E6F5FE','#FFE3AA','#F9BD7E','#ED875E','#D24D3E','#AE1C3E']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==11):
        colorscheme=['#3D52A1','#3A89C9','#77B7E5','#B4DDF7','#E6F5FE','#FFFAD2','#FFE3AA','#F9BD7E','#ED875E','#D24D3E','#AE1C3E']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    else:
        colorscheme=clist
        print("OUT OF RANGE[3-11] : COLORBLIND MODE DEACTIVATED ---> DEFAULT MODE")
    return(colorscheme)

def rainbow(number_of_plots):
    prop_cycle=plt.rcParams['axes.prop_cycle']
    clist=prop_cycle.by_key()['color']

    if(number_of_plots==4):
        colorscheme=['#404096','#57A3AD','#DEA73A','#D92120']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==5):
        colorscheme=['#404096','#529DB7','#7DB874','#E39C37','#D92120']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==6):
        colorscheme=['#404096','#498CC2','#63AD99','#BEBC48','#E68B33','#D92120']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==7):
        colorscheme=['#781C81','#3F60AE','#539EB6','#6DB388','#CAB843','#E78532','#D92120']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==8):
        colorscheme=['#781C81','#3F56A7','#4B91C0','#5FAA9F','#91BD61','#D8AF3D','#E77C30','#D92120']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==9):
        colorscheme=['#781C81','#3F4EA1','#4683C1','#57A3AD','#6DB388','#B1BE4E','#DFA53A','#E7742F','#D92120']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==10):
        colorscheme=['#781C81','#3F479B','#4277BD','#529DB7','#62AC9B','#86BB6A','#C7B944','#E39C37','#E76D2E','#D92120']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==11):
        colorscheme=['#781C81','#404096','#416CB7','#4D95BE','#5BA7A7','#6EB387','#A1BE56','#D3B33F','#E59435','#E6682D','#D92120']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    elif(number_of_plots==12):
        colorscheme=['#781C81','#413B93','#4065B1','#488BC2','#55A1B1','#63AD99','#7FB972','#B5BD4C','#D9AD3C','#E68E34','#E6642C','#D92120']
        plt.rcParams['axes.prop_cycle'] = cycler('color', colorscheme)
    else:
        colorscheme=clist
        print("OUT OF RANGE[4-12] : COLORBLIND MODE DEACTIVATED ---> DEFAULT MODE")
    return(colorscheme)

def colorfunction(nfiles,function,printed,*options):
    solid = (0, ())
    loosely_dotted = (0, (1, 10))
    dotted = (0, (1, 5))
    densely_dotted = (0, (1, 1))

    loosely_dashed = (0, (5, 10))
    dashed = (0, (5, 5))
    densely_dashed = (0, (5, 1))

    loosely_dashdotted = (0, (3, 10, 1, 10))
    dashdotted = (0, (3, 5, 1, 5))
    densely_dashdotted = (0, (3, 1, 1, 1))

    loosely_dashdotdotted = (0, (3, 10, 1, 10, 1, 10))
    dashdotdotted = (0, (3, 5, 1, 5, 1, 5))
    densely_dashdotdotted = (0, (3, 1, 1, 1, 1, 1))

    color=[]
    style=[]
    estyle=[]
    for argument in options:
        if argument=='blue':
            option='blue'
        if argument=='bluegreen':
            option='bluegreen'
        if argument=='green':
            option='green'
        if argument=='gold':
            option='gold'
        if argument=='brown':
            option='brown'
        if argument=='rose':
            option='rose'
        if argument=='purple':
            option='purple'

    if printed=='c':
        estyle=[solid]*nfiles
        if function=='fccolorblind':
            color=fccolorblind(nfiles)
        elif function=='rbscale':
            color=rbscale(nfiles)
        elif function=='rainbow':
            color=rainbow(nfiles)
        elif function=='huescale':
            color=huescale(nfiles,*options)

    if (printed=='b&w'):
        color=['black']*nfiles
    if (printed=='blue'):
        color=['#4477AA']*nfiles
    if (printed=='red'):
        color=['#CC6677']*nfiles
    if (printed=='yellow'):
        color=['#DDCC77']*nfiles
    if (printed=='green'):
        color=['#117733']*nfiles
    if (printed=='b&w' or printed=='blue'  or printed=='red' or printed=='yellow' or printed=='green'):
        style = [solid,dashed,dotted,dashdotted,dashdotdotted,densely_dashed,densely_dotted,densely_dashdotted,densely_dashdotdotted,loosely_dashed,loosely_dotted,loosely_dashdotted,loosely_dashdotdotted]
        if(nfiles > 13):
            print('CAREFUL : MAXIMUM 13 DIFFERENT LINESTYLES')
            style = style*int(np.ceil(nfiles/13))
        estyle = style[0:nfiles]
        default_cycler=(cycler(color=color)+cycler(linestyle=estyle))
        plt.rc('axes', prop_cycle=default_cycler)

    return(color,estyle)

def cbmap(function):
    x=np.linspace(0.,1.,1000)
    if function=='rbscale':
        red=0.237-2.13*x+26.92*x**2-65.5*x**3+63.5*x**4-22.36*x**5
        green=((0.572+1.524*x-1.811*x**2)/(1.-0.291*x+0.1574*x**2))**2
        blue=(1./(1.579-4.03*x+12.92*x**2-31.4*x**3+48.6*x**4-23.36*x**5))
    if function=='rainbow':
        red = (0.472-0.567*x+4.05*x**2)/(1.+8.72*x-19.17*x**2+14.1*x**3)
        green = 0.108932-1.22635*x+27.284*x**2-98.577*x**3+163.3*x**4-131.395*x**5+40.634*x**6
        blue = 1./(1.97+3.54*x-68.5*x**2+243*x**3-297*x**4+125*x**5)
    if function=='huescale':
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

    cbcmap = mcolors.LinearSegmentedColormap('cmap_%s' %(function), cdict)
    return(cbcmap)

def cbmap_discrete(function):
    cbcmap = cbmap(function)

    cmaplist = [cbcmap(i) for i in range(cbcmap.N)]
    cbcmap_n = cbcmap.from_list('cbcmap_n', cmaplist, cbcmap.N)
    return(cbcmap_n)

def norm_discrete(data, function, nbin):
    bounds=np.linspace(data.min(),data.max(),nbin+1)
    cbcmap_n = cbmap_discrete(function)
    norm=mcolors.BoundaryNorm(bounds,cbcmap_n.N)
    if(nbin>=cbcmap_n.N):
        print('CAREFUL : ONLY %d DIFFERENT COLORS IN THIS COLORMAP' %(cbcmap_n.N))
    return(norm)

def mapping(fig,ax,data2d,function,extent):
    im=ax.imshow(data2d, cmap=cbmap(function), aspect='auto', extent=extent)
    fig.colorbar(im)

def mapping_discrete(fig,ax,data2d,function,extent,nbin):
    im = ax.imshow(data2d, cmap=cbmap_discrete(function), norm=norm_discrete(data2d,function,nbin), aspect='auto', extent=extent)
    fig.colorbar(im)

def test_fccolorblind(ny):
    nx=100
    x=np.linspace(0,10, nx)
    y=np.zeros((ny,nx), dtype=int)
    color=fccolorblind(ny)

    for i in range(ny):
        for j in range(nx):
            y[i][j]=x[j]+i
        # plt.plot(x,y[i], color[i], linewidth=2.0)
        plt.plot(x,y[i], linewidth=2.0)

    plt.show()

def test_huescale(ny, *option):
    #SET DEFAULT VALUES IF NO OPTIONAL ARGUMENT
    hue='None'
    #OPTION
    for argument in option:
        if argument=='blue':
            hue='blue'
        if argument=='bluegreen':
            hue='bluegreen'
        if argument=='green':
            hue='green'
        if argument=='gold':
            hue='gold'
        if argument=='brown':
            hue='brown'
        if argument=='rose':
            hue='rose'
        if argument=='purple':
            hue='purple'

    nx=100
    x=np.linspace(0,10, nx)
    y=np.zeros((ny,nx), dtype=int)
    color=huescale(ny, *option)

    for i in range(ny):
        for j in range(nx):
            y[i][j]=x[j]+i
        # plt.plot(x,y[i], color[i], linewidth=2.0)
        plt.plot(x,y[i], linewidth=2.0)

    plt.show()

def test_rbscale(ny):
    nx=100
    x=np.linspace(0,10, nx)
    y=np.zeros((ny,nx), dtype=int)
    color=rbscale(ny)

    for i in range(ny):
        for j in range(nx):
            y[i][j]=x[j]+i
        # plt.plot(x,y[i], color[i], linewidth=2.0)
        plt.plot(x,y[i], linewidth=2.0)

    plt.show()

def test_rainbow(ny):
    nx=100
    x=np.linspace(0,10, nx)
    y=np.zeros((ny,nx), dtype=int)
    color=rainbow(ny)

    for i in range(ny):
        for j in range(nx):
            y[i][j]=x[j]+i
        # plt.plot(x,y[i], color[i], linewidth=2.0)
        plt.plot(x,y[i], linewidth=2.0)

    plt.show()

def test_mapping(function):
    fig,ax=plt.subplots()

    r = np.arange(-np.pi, np.pi, 0.1)
    t = np.arange(0, 2*np.pi, 0.1)
    extent = [r[0],r[-1],t[0],t[-1]]
    X, Y = np.meshgrid(r, t)
    data = np.cos(X) * np.sin(Y) * 10

    mapping(fig,ax,data,function,extent)
    plt.show()

def test_mapping_discrete(function,nbin):
    fig,ax=plt.subplots()

    r = np.arange(-np.pi, np.pi, 0.1)
    t = np.arange(0, 2*np.pi, 0.1)
    extent = [r[0],r[-1],t[0],t[-1]]
    X, Y = np.meshgrid(r, t)
    data = np.cos(X) * np.sin(Y) * 10

    mapping_discrete(fig,ax,data,function,extent,nbin)
    plt.show()
