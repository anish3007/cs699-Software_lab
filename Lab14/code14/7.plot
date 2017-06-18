set terminal pngcairo font "serial,10" size 800, 800 
set output '7.png'
set boxwidth 0.75
set style fill solid
set title "Sale of cars in India, as of June 2015"
plot "7.data" using 2:xtic(1) with histogram
