# colorblind
A colorblind-friendly python module that allows optimal color choice for plotting multiple curves  
Version: 1.7  
Author: Gaylor Wafflard-Fernandez  
Author-email: gwafflard@irap.omp.eu

**INSTALLATION OF THE COLORBLIND MODULE**  
FROM THE colorblind directory, run  
`python setup.py install`

**AVAILABLE FUNCTIONS**  
`import colorblind as cb`  
4 functions for now  
4 test functions

`color1 = cb.fccolorblind(nb_of_plots)`  
from 1 to 12 plots [DISTINCT COLORS]  
`cb.test_fccolorblind(nb_of_plots)`

`color2 = cb.huescale(nb_of_plots, \*option)`  
from 1 to 9 plots [FOR SEQUENTIAL DATA]  
`cb.test_huescale(nb_of_plots, \*option)`  
With option 'blue','bluegreen','green',  
'gold','brown','rose','purple' for less than 3 plots

`color3 = cb.rbscale(nb_of_plots)`  
from 3 to 11 plots [FOR DIVERGING DATA]  
`cb.test_rbscale(nb_of_plots)`

`color4 = cb.rainbow(nb_of_plots)`  
from 4 to 12 plots [RAINBOW SCHEME]  
`cb.test_rainbow(nb_of_plots)`

**USE OF THE COLORBLIND MODULE**  
#### **`color,linestyle = cb.colorfunction(nb_of_plots,function,printed,*options)`**  
13 different linestyles  
function : 'fccolorblind', 'rbscale', 'rainbow', 'huescale'  
printed : 'c' (color => solid lines + different colors),  
'b&w' (black and white => black color + different linestyles)  
'blue' ([color1] blue + different linestyles)  
'red' ([color1] red + different linestyles)  
'yellow' ([color1] yellow + different linestyles)  
'green' ([color1] green + different linestyles)  
options if function='huescale' and nb_of_plots<=3

**REFERENCE**  
Paul Tol. 2012. "Colour Schemes." SRON Technical Note, SRON/EPS/TN/09-002.  
https://personal.sron.nl/~pault/data/colourschemes.pdf
