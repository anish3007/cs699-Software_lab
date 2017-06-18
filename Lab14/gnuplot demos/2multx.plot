set term png size 600, 400
# set size 0.5, 0.5
set output "figure2.png"
plot [-2*pi:2*pi] sin(x),cos(x),x linetype 4
