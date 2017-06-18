set terminal pngcairo font "serial,10" size 800, 800 
set output '8.png'

set title "3-D Plot  of x^2-y^2"
set xrange [-2:2]
set yrange [-2:2]
set xlabel "X"
set ylabel "Y"

splot x**2-y**2
