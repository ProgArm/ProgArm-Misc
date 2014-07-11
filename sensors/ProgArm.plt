#!/usr/bin/gnuplot
set samples 21
set isosample 11
set xlabel "X axis" offset -3,-2
set ylabel "Y axis" offset 3,-2
set zlabel "Z axis" offset -5
set title "ProgArm data"
#set arrow 1 from 0,0,0 to 250,-10,30 nohead
set xrange [-1000:1000]
set yrange [-1000:1000]
set zrange [-1000:1000]

splot "< tail -1 C.dat" using 0:0:0:1:2:3 with vectors

pause 0.03
replot
reread
