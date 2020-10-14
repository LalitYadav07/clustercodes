
call singleion -nt 100 -r Tm3p.sipf 6 0 0 0   0 0 0


call convolute 6 8 results/Tm3p.sipf.trs 1 2 expdat/res50mev.dat 1 2 expdat\E_all_50mev_6k.xye > results/spectrum_all_6k_50mev.clc

python minimize.py
rem type results\spectrum_all_6k_50mev.clc
type statable.txt