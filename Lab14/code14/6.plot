set terminal pngcairo font "serial,10" size 800, 800 
set output '6.png'
set boxwidth 0.05 absolute
set style fill solid 1.0 noborder
set title "Plot of Gaussian Frequency Distribution"
bin_width = 0.1;
bin_number(x) = floor(x/bin_width)
rounded(x) = bin_width * ( bin_number(x) + 0.5 )
plot '6.data' using (rounded($1)):(1) smooth frequency with boxes
