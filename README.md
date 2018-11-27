# colorblind
A colorblind-friendly python module that allows optimal color choice for plotting multiple curves  
Version: 1.7  
Author: Gaylor Wafflard-Fernandez  
Author-email: gwafflard@irap.omp.eu

**INSTALLATION OF THE COLORBLIND MODULE**  
_DOWNLOAD colorblind-x.x.tar.gz_  
tar xvzf colorblind-x.x.tar.gz  
_FROM THE colorblind-x.x directory, run_  
python setup.py install

**USE OF THE COLORBLIND MODULE**  
import colorblind as cb  
_4 functions for now  
4 test functions_

color1 = cb.fccolorblind(nb_of_plots)  
_from 1 to 12 plots [DISTINCT COLORS]_  
cb.test_fccolorblind(nb_of_plots)

color2 = cb.huescale(nb_of_plots, \*option)  
_from 1 to 9 plots [FOR SEQUENTIAL DATA]_  
cb.test_huescale(nb_of_plots, \*option)  
_With option ***'blue','bluegreen','green',  
'gold','brown','rose','purple'*** for less than 3 plots_

color3 = cb.rbscale(nb_of_plots)  
_from 3 to 11 plots [FOR DIVERGING DATA]_  
cb.test_rbscale(nb_of_plots)

color4 = cb.rainbow(nb_of_plots)  
_from 4 to 12 plots [RAINBOW SCHEME]_  
cb.test_rainbow(nb_of_plots)

`color, linestyle = cb.colorfunction(nb_of_plots,function,printed, \*options)`  
_13 different linestyles  
function : ***'fccolorblind', 'rbscale', 'rainbow', 'huescale'***  
printed : ***'c'*** (color => solid lines + different colors),  
***'b&w'*** (black and white => black color + different linestyles)  
***'blue'*** ([color1] blue + different linestyles)  
***'red'*** ([color1] red + different linestyles)  
***'yellow'*** ([color1] yellow + different linestyles)  
***'green'*** ([color1] green + different linestyles)  
options if function='huescale' and nb_of_plots<=3_

**REFERENCE**  
Paul Tol. 2012. "Colour Schemes." SRON Technical Note, SRON/EPS/TN/09-002.  
https://personal.sron.nl/~pault/data/colourschemes.pdf
