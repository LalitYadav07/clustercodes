###For cluster 
import os
from scipy import optimize
import random
from os import path
#import pandas as pd
import subprocess
import numpy as np
import time
from multiprocessing import Process
#import matplotlib.pyplot as plt
#from scipy.interpolate import interp1d
import sys
#jobid = int(os.environ['SLURM_ARRAY_TASK_ID']) 
#basepath=os.getcwd()
#dir=basepath+'/parallel%s' % str(jobid)
#os.chdir(dir)
#random.seed(jobid)

def Energy6k_peaks():
    file = np.loadtxt("results/Tm3p.sipf.trs", skiprows=81, usecols=(5, 7))
    energy = file[:, 0]
    intensity = file[:, 1]
    relevant_E = np.array([], dtype=np.float64)
    relevant_I = np.array([], dtype=np.float64)
    maxIntensity = 0

    # take out onlyt positive energy with non zero intensity
    for E, I in zip(energy, intensity):
        if E > 0 and I > 0:
            relevant_E = np.append(relevant_E, E)
            relevant_I = np.append(relevant_I, I)
        if E > 8.8 and E < 10.1:
            maxIntensity = maxIntensity + I
    return relevant_E, relevant_I, maxIntensity


def sta_sus(Chi): 
    sta= abs(Chi[0]- 0.00825)# 45K
    return sta*5000


def sta_6k(E, I, maxIntensity):
    E_region = np.zeros(shape=(10, 15))  # assuming not more than 10 levels occur in same region
    I_region = np.zeros(shape=(10, 15))
    i, j, k, l, m, n, o, p, q, r, s = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    if maxIntensity !=0:
        for enr, intensity in zip(E, I):

            if enr > 7 and enr < 13:
                print(i)
                E_region[0, i] = enr
                I_region[0, i] = intensity
                i += 1

            if enr > 13 and enr < 19:
                E_region[1, j] = enr
                I_region[1, j] = intensity
                j += 1

            if enr > 18 and enr < 20:
                E_region[2, k] = enr
                I_region[2, k] = intensity
                k += 1
            if enr > 20 and enr < 23:
                E_region[3, l] = enr
                I_region[3, l] = intensity
                l += 1

            if enr > 23 and enr < 28:
                E_region[4, m] = enr
                I_region[4, m] = intensity
                m += 1

            if enr > 28 and enr < 38:
                E_region[5, n] = enr
                I_region[5, n] = intensity
                n += 1

            if enr > 38 and enr < 50:
                E_region[6, o] = enr
                I_region[6, o] = intensity
                o += 1

            if enr > 50 and enr < 70:
                print(p)
                E_region[7, p] = enr
                I_region[7, p] = intensity
                p += 1
            if enr > 70 and enr < 100:
                E_region[8, q] = enr
                I_region[8, q] = intensity
                q += 1

            if enr > 100 and enr < 200:
                E_region[9, r] = enr
                I_region[9, r] = intensity
                r += 1

    E_sta = np.zeros(shape=(10, 1))  # assuming not more than 10 levels occur in same region
    I_sta = np.zeros(shape=(10, 1))
    I_exp = np.array([98, 100, 0.031, 0.001, 0.89, 0.937, 0.01, 1, 1, 1])
    E_exp = [9.26, 15.5, 18.5, 0, 25, 33, 0, 57, 90, 0]
    factor = np.array([10, 10, 20, 100, 10, 10, 10, 10, 10, 10])

    for a in [0, 1, 2, 4, 5, 7, 8]:
        if I_region[a, :].sum() > 0:
            position = E_region[a, :] @ I_region[a, :] / I_region[a, :].sum()
            E_sta[a] = abs(position - E_exp[a]) * 10
            I_sta[a] = abs((I_region[a, :].sum() / maxIntensity * 100 - I_exp[a]) * factor[a])
        else:
            E_sta[a] = 100
            I_sta[a] = 100
    if I_region[3, :].sum() > 0.001:
        I_sta[3] = 100
    if I_region[6, :].sum() > 0.001:
        I_sta[6] = 100
    if I_region[9, :].sum() > 1:
        I_sta[6] = 100

    total_sta = I_sta.sum() + E_sta.sum()
    return total_sta


def Matching150k(E, I, maxIntensity):
    int1, int2, int3, int4, int5= 0,0,0,0,0
    for enr , intensity  in zip(E, I): 
        if enr>8.5 and enr< 12 : # and intensity> 0.33* maxIntensity:
            int1= int1+ intensity   
        if enr > 14 and enr< 18 : #and intensity> 0.* maxIntensity:          
            int2= int2+ intensity           
        if enr> 23 and enr< 100 and intensity> 0.2* maxIntensity:
            return -1  
        if enr>.5 and enr<6  and intensity> 0.2* maxIntensity: 
            return -1
 #   total_sta= w1*abs(d1)+ w2*abs(d2) + w3*abs(d3) + w4* abs(d4) + w5*abs(d5)
    if abs((int1-int2)/int1) < 0.5 :   
        return abs((int1-int2)/int1)
    else: 
        return -1  
        
        
def substitute_blm(b20,b40,b43,b60,b63,b66):
    f=open("Tm3p.sipf", "r")
    lines= f.readlines()
    lines[128]="B20="+str(b20)+"\n"
    lines[129]="B40="+str(b40)+"\n"
    lines[130]="B43="+str(b43)+"\n"
    lines[131]="B60="+str(b60)+"\n"
    lines[132]="B63="+str(b63)+"\n"
    lines[133]="B66="+str(b66)+"\n"
    f.close()
    f=open("Tm3p.sipf", "w")
    f.writelines( lines)
    f.close()



def blm_pool(BB20):
    subprocess.call(['./loadmcphase'], shell=True )
   # fluctuation = [-.05,-0.03,-0.02, -.01, 0, 0.01, 0.02, 0.03,0.04,0.05]
    B20=BB20
    f= open("greenblm4.txt","w+")
    f.write("counter4 , b20 , 	 b40 , 	 b43 , 	 b60 , 	b63,  	b66,    ****   chi_stars,   	sta6k, 	   sta150k,   Steptime \n")
    f.close() 

    B40= -.0051
    B43= -0.18
    B60= -0.00014
    B63= .00137
    B66= -0.0011
 
    counter4=1
    skipper63, skipper60, skipper43 =1 ,1 ,1
    total=1
    start_time = time.time()
    b20=B20
    b40=B40
    
    while b40< -0.0007:
        b43=B43#+ B43*sample(fluctuation,1)[0] 
        while b43< -0.024:
                skipper43=0
            
                b60=B60#+B60*sample(fluctuation,1)[0]
                while b60 < -8.88*10**(-6):
                        skipper60=0


                        b63=B63#+ B63*sample(fluctuation, 1)[0]
                        while b63> 6.45*10**(-5):
                                skipper63=0


                                b66=B66#+ B66*sample(fluctuation, 1)[0]
                                while b66<  -5.53*10**(-5):
                                        substitute_blm(b20,b40,b43,b60,b63,b66)
                                        subprocess.call([ './calcsta6k'], shell=True )
                                        #subprocess.call(['sh', './calcsta6k'], shell=True )
                                        data6k= Energy_peaks() #return E I and max 

                                        sta6k=Matching6k(data6k[0], data6k[1],data6k[2])
                                        if sta6k != -1: 
                                            
                                            subprocess.call(['./calcsta150k'], shell=True )
                                           # subprocess.call(['sh', './calcsta150k'], shell=True )
                                            data= Energy_peaks() #return E I and max   
                                            sta150k=Matching150k(data[0], data[1],data[2])  
                                            if sta150k != -1:
                                                subprocess.call([ './sus_4star_python'], shell=True)
                                                #subprocess.call(['sh', './sus_4star_python'], shell=True)
                                                Chi_file=np.loadtxt("results/sus_4point.clc", usecols=(1,8))
                                                chi_stars=Chi_matching(Chi_file[:,1])
                                               
                                                if chi_stars>=2:   
                                                     file_greenblm4=open('greenblm4.txt','a')
                                                     np.savetxt(file_greenblm4, [[counter4,b20, b40, b43, b60, b63, b66, chi_stars, sta6k, sta150k, (time.time() - start_time)/total]])
                                                     counter4=counter4+1
                                                     file_greenblm4.close()
						    
                                        total=total+1
                                        

                                       
                                        if sta6k==-1:
                                            step_b66=0.80
                                        if sta6k!=-1:
                                            step_b66=0.85
                                            skipper63=1

                                        b66=b66*step_b66
                                #Time checking
                               # file_time=open('time.txt','a')
                                #np.savetxt(file_time, [[counter3,b20, b40, b43, b60, b63, b66, (time.time() - start_time)/total, step_b66, skipper63]])
                                #file_time.close()
                                if skipper63==1:
                                    step_b63=0.9
                                    skipper60=1 
                                if skipper63==0:
                                    step_b63=0.8
                                b63= b63*step_b63

                        if skipper60==1:
                            step_b60=0.9
                            skipper43=1
                        if skipper60==0:
                            step_b60=0.8
                        b60=b60*step_b60
                if skipper43==1:
                    step_b43=0.9
                if skipper43==0:
                    step_b43=0.8
                b43=b43*step_b43
        
        b40=b40*.85
        
    print ("total"+str(total) + " time per iteration = " + str((time.time() - start_time)/ total))
    f= open("greenblm4.txt","a")
    f.write("This is time when script finished :  %d\r\n" % ((time.localtime())))
    f.close()  


data6k= Energy6k_peaks() #return E I and max
sta6k=sta_6k(data6k[0], data6k[1],data6k[2])
print("sta="+str(sta6k))
print("HAHAHAHAHAH HOPHOHOHOHOHO#")
file_greenblm4=open('statable.txt','a')

f = open("statable.txt", "w")
f.write("sta="+str(sta6k))
f.close()
if sta6k<2000:
    file_greenblm4=open('staplot.txt','a')
    np.savetxt(file_greenblm4, [[time.time(),sta6k]])
    file_greenblm4.close()


#boundary=((b20*dn,b20*up), (b40*dn,b40*up), (b43*dn,b43*up), (b60*dn,b60*up), (b63*dn,b63*up), (b66*dn,b66*up))
#Blm=np.array(-0.5, -0.0027, -0.018, -0.000021, 0.00088, -0.000096)
#print(Blm)
#boundary=((Blm[0]*dn, Blm[0]*up), (Blm[1]*dn, Blm[1]*up), (Blm[2]*dn,Blm[2]*up), (Blm[3]*dn, Blm[3]*up), ( Blm[4]*dn,Blm[4]*up), (Blm[5]*dn,Blm[5]*up))
#print(boudary)
#print(optimize.minimize(min_fun, Blm, bounds=boundary))
						    


   

