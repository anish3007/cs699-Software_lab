set term png size 600, 400
# set size 0.5, 0.5
set output "figure1.png"
plot [-15:15] sin(x) linetype 4
