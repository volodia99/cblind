# colorblind
A colorblind-friendly python module that allows optimal color choice for plotting multiple curves  
Works only with python 3  
3 optimal colormaps are now available to map 2D fields  
Version: 2.2
Author: Gaylor Wafflard-Fernandez  
Author-email: gaylor.wafflard@univ-grenoble-alpes.fr

**I. INSTALLATION**  
`pip install cblind`

**II. USAGE FOR PLOTTING**  
`import cblind as cb`
5 palette functions for now  
6 test plotting functions

`color, linestyle = cb.Coloplots().cblind(nb_of_plots)`  
from 1 to 12 plots [DISTINCT COLORS]  
For more than 12 plots, the linestyle is changed  
`cb.test_cblind(nb_of_plots)`

`color, linestyle = cb.Coloplots().huescale(nb_of_plots, \*option)`  
from 1 to 9 plots [SEQUENTIAL DATA]  
`cb.test_huescale(nb_of_plots, \*option)`  
With option 'blue','bluegreen','green',  
'gold','brown','rose','purple' for less than 3 plots, otherwise ocherscale

`color, linestyle = cb.Coloplots().rbscale(nb_of_plots)`  
from 3 to 11 plots [DIVERGING DATA]  
`cb.test_rbscale(nb_of_plots)`

`color, linestyle = cb.Coloplots().rainbow(nb_of_plots)`  
from 4 to 12 plots [RAINBOW SCHEME]  
`cb.test_rainbow(nb_of_plots)`

`color, linestyle = cb.Coloplots().monocolor(nb_of_plots, \*option)`  
from 1 to 13 plots [MONOCOLOR/PRINTING]  
monochromatic but different linestyles
`cb.test_monocolor(nb_of_plots, \*option)`
With option "b&w", "blue", "red", "yellow", "green", "purple"

**III. USAGE OF COLORMAPS**  
`cmap = cb.cbmap(palette, nbin)`  
palette : 'rbscale', 'rainbow', 'huescale' cf **II.**, but also all colormaps from matplotlib + "\_r" variants for reverse colormaps
nbin : discretization of the colormap
data2d : 2D field  

**a) Example, with a field `data2d`**  
`import matplotlib.pyplot as plt`  

`fig, ax = plt.subplots()`  
`im=ax.imshow(data2d, cmap=cb.cbmap("rainbow_r", nbin=10), aspect='auto')`  
`fig.colorbar(im)`  

`fig, ax = plt.subplots()`  
`im=ax.imshow(data2d, cmap=cb.cbmap("inferno"), aspect='auto')`
`fig.colorbar(im)`  

**b) Basic mapping functions**  
#### **`cb.mapping(fig,ax,data2d,extent,palette=palette,nbin=nbin)`**  
`cb.test_mapping(palette,nbin)`  

**REFERENCE**  
Paul Tol. 2012. "Colour Schemes." SRON Technical Note, SRON/EPS/TN/09-002.  
https://personal.sron.nl/~pault/data/colourschemes.pdf
