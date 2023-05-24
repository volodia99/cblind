# cblind
[![PyPI](https://img.shields.io/pypi/v/cblind)](https://pypi.org/project/cblind/)

A colorblind-friendly python module that allows color choice for plotting multiple curves  
Works only with python 3  
8 colormaps are now available to map 2D fields  
Version: 2.2.4
Author: Gaylor Wafflard-Fernandez  
Author-email: gaylor.wafflard@univ-grenoble-alpes.fr

## Installation

Install with `pip`

```
pip install cblind
```

To import cblind:

```python
import cblind as cb
```

## Usage for plotting

10 palette functions to plot curves are available for now in the Colorplots class, with the corresponding test plotting functions.  

### cblind

```python
color, linestyle = cb.Coloplots().cblind(nb_of_plots)
```

from 1 to 12 plots [DISTINCT COLORS]. For more than 12 plots, the linestyle is changed.  

```python
cb.test_cblind(nb_of_plots)
```

![cblind](https://github.com/Volodia99/cblind/raw/master/imgs/cblind.png)

### contrast

```python
color, linestyle = cb.Coloplots().contrast(nb_of_plots)
```

for less than 4 contrast plots [DISTINCT COLORS]. For more than 12 plots, the linestyle is changed.  

```python
cb.test_contrast(nb_of_plots)
```

![contrast](https://github.com/Volodia99/cblind/raw/master/imgs/contrast.png)

### huescale

```python
color, linestyle = cb.Coloplots().huescale(nb_of_plots, *option)
```

from 1 to 9 plots [SEQUENTIAL DATA]. With option "blue","bluegreen","green", "gold","brown","rose","purple" for less than 3 plots, otherwise ocherscale.  

```python
cb.test_huescale(nb_of_plots, *option)
```

![huescale](https://github.com/Volodia99/cblind/raw/master/imgs/huescale.png)

### rbscale

```python
color, linestyle = cb.Coloplots().rbscale(nb_of_plots)
```

from 3 to 11 plots [DIVERGING DATA].  

```python
cb.test_rbscale(nb_of_plots)
```

![rbscale](https://github.com/Volodia99/cblind/raw/master/imgs/rbscale.png)

### rainbow

```python
color, linestyle = cb.Coloplots().rainbow(nb_of_plots)
```

from 4 to 12 plots [RAINBOW SCHEME].  

```python
cb.test_rainbow(nb_of_plots)
```

![rainbow](https://github.com/Volodia99/cblind/raw/master/imgs/rainbow.png)

### extreme_rainbow

```python
color, linestyle = cb.Coloplots().extreme_rainbow(nb_of_plots)
```

from 1 to 34 plots [RAINBOW SCHEME].  

```python
cb.test_extreme_rainbow(nb_of_plots)
```

![extreme_rainbow](https://github.com/Volodia99/cblind/raw/master/imgs/extreme_rainbow.png)

### solstice

```python
color, linestyle = cb.Coloplots().solstice(nb_of_plots)
```

for less than 11 plots [DIVERGING DATA]  

```python
cb.test_solstice(nb_of_plots)
```

![solstice](https://github.com/Volodia99/cblind/raw/master/imgs/solstice.png)

### bird

```python
color, linestyle = cb.Coloplots().bird(nb_of_plots)
```

for less than 9 plots [DIVERGING DATA]  

```python
cb.test_bird(nb_of_plots)
```

![bird](https://github.com/Volodia99/cblind/raw/master/imgs/bird.png)

### pregunta

```python
color, linestyle = cb.Coloplots().pregunta(nb_of_plots)
```

for less than 9 plots [DIVERGING DATA]  

```python
cb.test_pregunta(nb_of_plots)
```

![pregunta](https://github.com/Volodia99/cblind/raw/master/imgs/pregunta.png)

### monocolor

```python
color, linestyle = cb.Coloplots().monocolor(nb_of_plots, *option)
```

from 1 to 13 monochromatic plots [MONOCOLOR/PRINTING] with different linestyles. With option "b&w", "blue", "red", "yellow", "green", "purple".

```python
cb.test_monocolor(nb_of_plots, *option)
```

![monocolor](https://github.com/Volodia99/cblind/raw/master/imgs/monocolor.png)

## Usage for colormaps

8 cblind palettes are available for now : "cb.rbscale", "cb.rainbow", "cb.extreme_rainbow", "cb.huescale", 
"cb.solstice", "cb.bird", "cb.pregunta", "cb.iris", but also all colormaps from matplotlib + "\_r" variants for reverse colormaps.  

```python
cmap = cb.cbmap(palette, nbin)
```

The `nbin` argument is used to discretize the colormaps.  

![colormaps](https://github.com/Volodia99/cblind/raw/master/imgs/colormaps.png)

To test the colormaps, you can try:

```python
cb.test_mapping(palette, nbin)
```

### Example with a field `data2d`

```python
import numpy as np
import matplotlib.pyplot as plt
data2d = np.repeat(np.linspace(0,1,100),20).reshape(100,20).T

fig, ax = plt.subplots()
im = ax.imshow(data2d, cmap=cb.cbmap("cb.rainbow_r", nbin=10), aspect='auto')
fig.colorbar(im)
plt.show()
```

### Basic mapping function

```python
cb.mapping(fig,ax,data2d,extent,palette=palette,nbin=nbin)
```

**REFERENCE**  
Paul Tol. 2012. "Colour Schemes." SRON Technical Note, SRON/EPS/TN/09-002.  
https://personal.sron.nl/~pault/data/colourschemes.pdf
