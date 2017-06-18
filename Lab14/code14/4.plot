set terminal pngcairo font "serial,10" size 800, 800 
set output '4.png'
set datafile separator ','
stats '4.data' u 2 noout

ang(x)=x*360.0/STATS_sum
perc(x)=x*100.0/STATS_sum

set size square
set xrange [-1:1.5]
set yrange [-1.25:1.25]
set style fill solid 1

unset border
unset tics
unset key

Ai=0.0; Bi=0.0;
mid = 0.0;
i=0; j=0;
yi=0.0; yi2=0.0;

plot '4.data' u (0):(0):(1):(Ai):(Ai=Ai+ang($2)):(i=i+1) with circle linecolor var,\
     '4.data' u (1.5):(yi=yi+0.5/STATS_records):($1) w labels,\
     '4.data' u (1.3):(yi2=yi2+0.5/STATS_records):(j=j+1) w p pt 5 ps 2 linecolor var,\
     '4.data' u (mid=Bi+ang($2)*pi/360.0, Bi=2.0*mid-Bi, 0.5*cos(mid)):(0.5*sin(mid)):(sprintf('%.0f (%.1f\%)', $2, perc($2))) w labels
