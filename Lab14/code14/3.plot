set term png size 800, 600
#set size 0.5, 0.5
set output "3.png"
set title "Plot multiple columns of data from a file"
plot '3.data' using 1:2 with lines, '3.data' using 1:3 with lines, '3.data' using 1:4 with lines
