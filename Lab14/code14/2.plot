set term png size 600, 400
#set size 0.5, 0.5
set output "2.png"
set title "Plot data from a file"
plot '2.data' with lines
