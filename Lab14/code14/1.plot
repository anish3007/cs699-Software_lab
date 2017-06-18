set term png font "arial,15" size 600, 400
# set size 0.5, 0.5
set output "1.png"
plot [-1:15] log(x) linetype 4
