call singleion -M -r Tm3p.sipf 02 0 0 0.1 0 0 0 > results\sus_a.clc
call singleion -M -r Tm3p.sipf 05 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 10 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 12 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 15 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 20 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 35 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 40 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 45 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 50 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 55 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 60 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 65 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 70 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 80 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 90 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 100 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 110 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 120 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 130 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 140 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 150 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 160 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 180 0 0 0.1 0 0 0 >> results\sus_a.clc


call singleion -M -r Tm3p.sipf 200 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 230 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 250 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 280 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 300 0 0 0.1 0 0 0 >> results\sus_a.clc

call singleion -M -r Tm3p.sipf 310 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 320 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 330 0 0 0.1 0 0 0 >> results\sus_a.clc
call singleion -M -r Tm3p.sipf 360 0 0 0.1 0 0 0 >> results\sus_a.clc


call factcol 9 0.5582 results\sus_a.clc
call factcol 9 10 results\sus_a.clc   rem divide by applied field

rem call convolute 2 9 results\sus_a.clc 1 2 expdat\chi.txt > results\sus_sta.clc
rem type results\sus_sta.clc

call display 2 9 results\sus_a.clc 1 2 expdat\chi.txt

