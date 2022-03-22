#        *************************    
#        * Sublementary material *    
#        *************************    
#    
#        * -------------------------------------------------------------------- *    
#        * New determination of the production cross section                    *    
#        *            for secondary positrons and electrons in the Galaxy       *    
#        * -------------------------------------------------------------------- *    
#    
#          Luca Orusa, Mattia Di Mauro, Fiorenza Donato, and Michael Korsmeier    
#         *-------------------------------------------------------------------*    
#    
#          IF YOU USE THIS SCRIPT, PLEASE CITE THE PAPER.    
#    
#    
#          We provide the script to read the Final_table+.dat and  Final_table-.dat 
#          files that contain energy differential cross section $d\sigma_{ij}/dT$    
#          for cosmic-ray (CR) component i and intersellar medium (ISM)    
#          component j. 




import numpy as np
from math import *
import scipy.special as spys
from scipy.interpolate import interpn

#       * -------------------------------------------------------------------------------------------------------------- *
#       Here you can choose between positron and electron cross sections: write 'positron' for e^+ and 'electron' for e^-
#       * -------------------------------------------------------------------------------------------------------------- *

particle='electron'

#       * -------------------------------------------------------------------------------------------------------------- *
#       Here you can choose between best-fit, upper and lower band of the positron and electron cross sections: 
#       write 'best_fit' for the best-fit, 'upper' for the upper band and 'lower' for the lower band
#       * -------------------------------------------------------------------------------------------------------------- *

request='best-fit'

if(particle=='positron'):
    if(request=='best-fit'):
       table=np.loadtxt('supplementary_table_positrons_best_fit.dat')
    elif(request=='upper'):
       table=np.loadtxt('supplementary_table_positrons_upper_band.dat')
    elif(request=='lower'):
       table=np.loadtxt('supplementary_table_positrons_lower_band.dat')
elif(particle=='electron'):
    if(request=='best-fit'):
       table=np.loadtxt('supplementary_table_electrons_best_fit.dat')
    elif(request=='upper'):
       table=np.loadtxt('supplementary_table_electrons_upper_band.dat')
    elif(request=='lower'):
       table=np.loadtxt('supplementary_table_electrons_lower_band.dat')


#       * --------------------------------------------------------------- *
#       Here you can choose the projectile nuclei and the target nuclei:. 
#       
#       For projectile nuclei you can choose between:
#       p(Z= 1, A= 1), D(Z= 1, A= 2), He3 (Z= 2, A= 3), He4 (Z= 2, A= 4), C12 (Z= 6, A=12), C13 (Z= 6, A=13), C14 (Z= 6, A=14), N (Z= 7, A=15), O (Z= 7, A=16)
#       
#       For target nuclei you can choose between:
#       p(Z= 1, A= 1), He4 (Z= 2, A= 4)
#       * --------------------------------------------------------------- *


projectile_nuclei='p'
target_nuclei='p'


if(projectile_nuclei=='p' and target_nuclei=='p'):
    index=2
elif(projectile_nuclei=='p' and target_nuclei=='He4'):
    index=3
elif(projectile_nuclei=='D' and target_nuclei=='p'):
    index=4
elif(projectile_nuclei=='D' and target_nuclei=='He4'):
    index=5
elif(projectile_nuclei=='He3' and target_nuclei=='p'):
    index=6
elif(projectile_nuclei=='He3' and target_nuclei=='He4'):
    index=7
elif(projectile_nuclei=='He4' and target_nuclei=='p'):
    index=8
elif(projectile_nuclei=='He4' and target_nuclei=='He4'):
    index=9
elif(projectile_nuclei=='C12' and target_nuclei=='p'):
    index=10
elif(projectile_nuclei=='C12' and target_nuclei=='He4'):
    index=11
elif(projectile_nuclei=='C13' and target_nuclei=='p'):
    index=12
elif(projectile_nuclei=='C13' and target_nuclei=='He4'):
    index=13
elif(projectile_nuclei=='C14' and target_nuclei=='p'):
    index=14
elif(projectile_nuclei=='C14' and target_nuclei=='He4'):
    index=15
elif(projectile_nuclei=='N' and target_nuclei=='p'):
    index=16
elif(projectile_nuclei=='N' and target_nuclei=='He4'):
    index=17
elif(projectile_nuclei=='O' and target_nuclei=='p'):
    index=18
elif(projectile_nuclei=='O' and target_nuclei=='He4'):
    index=19

projectile_kinetic_energy=np.logspace(np.log10(0.1), np.log10(100000),120)
particle_kinetic_energy=np.logspace(np.log10(0.01), np.log10(10000),90)
cross_section=np.zeros((len(particle_kinetic_energy),len(projectile_kinetic_energy)))


count=0
for j in range(len(projectile_kinetic_energy)):
    cross_section[:,j]=table[count:count+90,index]
    count=count+90


#       * ------------------------------------------------------------------------------------------------------ *
#       This function provide the differential cross section dsigma/dT_e, where T_e is the particle (e^+ or e^-) 
#       kinetic energy and T_p is the kinetic energy per nucleon of the incident CR.
#       * ------------------------------------------------------------------------------------------------------ *

def particle_cross_section(T_e,T_p):
    
    point=np.array([T_e,T_p])
    points=(particle_kinetic_energy,projectile_kinetic_energy)
    result=interpn(points,cross_section,point)
    return result




