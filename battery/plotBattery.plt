#!/usr/bin/env gnuplot
set terminal png transparent nocrop enhanced font arial 8 size 1200,1200
set output 'battery.png'

set multiplot layout 3, 1 title "Battery Stats"

set xdata time
#set ydata time
#set yrange [0:]
set autoscale y

set timefmt x "%s"
#set timefmt y "%s"

set format x "%H:%M    %F"
#set format y "%H:%M"
set xtics 60*60*3 rotate by -60
set mxtics 2
set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"

set xlabel ""
set ylabel "mAh"

plot 'battery' using 1:2 with linespoints pt 7 ps 0.4

set ylabel "Volts"
#set yrange [0:5]
set autoscale y
plot 'battery' using 1:4 with linespoints pt 7 ps 0.4

set ylabel "°C"
set autoscale y
plot 'battery' using 1:6 with linespoints pt 7 ps 0.4

unset multiplot
