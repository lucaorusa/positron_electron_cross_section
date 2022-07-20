# positron_electron_cross_section
New determination of the production cross section for secondary positrons and electrons in the Galaxy
Luca Orusa, Mattia Di Mauro, Fiorenza Donato, Michael Korsmeier
arXiv:            2203.13143 [astro-ph.HE]    
Published in: Phys. Rev. D 105, 123021    

IF YOU USE THIS TABLE, PLEASE CITE THE ABOVE PAPER.    
Please acknowledge the use of these tables by citing the paper: Phys. Rev. D 105, 123021(2203.13143)
If you want to add these tables to a public code,  please add the readme file available at this link(https://github.com/lucaorusa/positron_electron_cross_section) to the folder where the tables are located.    

In this repository are contained the tables with the energy differential cross section d\sigma_{ij}/dT of positrons and electrons for cosmic-ray (CR) 
component i and interstellar medium (ISM) component j. Here j are protons (Z=1,A=1) and Helium (Z=2,A=4). The first column of each file contains the 
kinetic energy per nucleon of the incident CR T_{projectile} and the second column the kinetic energy of the positron or electron T_{e}, both in GeV. 
The following columns contain the energy differential cross  sections of various possible CR isotopes in units of mb/GeV. The tables can be used to find the source term only up to 10 TeV for the positron/electron energies.
These are total cross section, i.e. including all the possible contributions.
In 'supplementary_table_positrons_best_fit.dat' are contained the energy differential cross section of positrons, in 
'supplementary_table_positrons_upper_band.dat' is contained the upper 1-sigma uncertainty band, and in 'supplementary_table_positrons_lower_band.dat' is
contained the lower 1-sigma uncertainty band. The same rules apply for electrons. To read all these tables is sufficient to use the python script 'script_supplementary.py'. Details of its usage are reported in the script.
