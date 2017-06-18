set terminal pngcairo font "serial,10" size 800, 800 
set output '5.png'
set boxwidth 0.5
set style fill solid
set title "Population of Australian cities (millions), as of June 2012"
plot "5.data" using 2:xtic(1) with boxes
