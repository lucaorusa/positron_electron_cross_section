# positron_electron_cross_section
New determination of the production cross section for secondary positrons and electrons in the Galaxy
Luca Orusa, Mattia Di Mauro, Fiorenza Donato, Michael Korsmeier
arXiv:2203.13143 

In this repository are contained the tables with the energy differential cross section d\sigma_{ij}/dT of positrons and electrons for cosmic-ray (CR) 
component i and interstellar medium (ISM) component j. Here j are protons (Z=1,A=1) and Helium (Z=2,A=4). The first column of each file contains the 
kinetic energy per nucleon of the incident CR T_{projectile} and the second column the kinetic energy of the positron or electron T_{e}, both in GeV. 
The following columns contain the energy differential cross  sections of various possible CR isotopes in units of mb/GeV.  
These are total cross section, i.e. including all the possible contributions.
In 'supplementary_table_positrons_best_fit.dat' are contained the energy differential cross section of positrons, in 
'supplementary_table_positrons_upper_band.dat' is contained the upper 1-sigma uncertainty band, and in 'supplementary_table_positrons_lower_band.dat' is
contained the lower 1-sigma uncertainty band. The same rules apply for electrons. To read all these tables is sufficient to use the python script 'script_supplementary.py'. Details of its usage are reported in the script.
If you use these tables or the script, please cite the paper.
