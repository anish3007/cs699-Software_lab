set terminal pngcairo font "serial,10" size 800, 800 
set output '9.png'

set title "3-D Plot of data from file"
set xlabel "X"
set ylabel "Y"

splot '9.data' using 1:2:3 with lines
