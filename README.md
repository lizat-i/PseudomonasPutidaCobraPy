# genome-scale metabolic modelling of Pseudomonas putida using the cobra Toolbox


## General description

In this project PHA production using the Pseudonomas Putida Model iJN1462 is modelled. 

## Requirements

This verion of the code is based on the [MATLAB](- https://de.mathworks.com/products/matlab.html) version of the COBRA Toolbox, so MATLAB is required

The COnstraint-Based Reconstruction and Analysis Toolbox [COBRA](https://opencobra.github.io/cobratoolbox/stable/) utility is necesary.
 
For certain application [ibmCplexOptimizer](https://www.ibm.com/de-de/analytics/cplex-optimizer) is necesarry. if not available, comment out lines where the standard solver is set as ibm_cplex(main script)

## Project structure

 The `files` folder contains modells used [iJN1463](http://bigg.ucsd.edu/models/iJN1463) and [iJN1462](https://sfamjournals.onlinelibrary.wiley.com/doi/full/10.1111/1462-2920.14843)

 The `funcitons` folder contains some selfwritten subroutines in order to make certain operations redundant, they are application-specific writte.

 The `MatlabStart.sh` is a shell script to initialize the necesarry environent variables to connect the Cobra toolbox and Matlab to the CPLEX toolbox

 The `main.m` is  where the case Setup happens.

## References

[iJN1462Modell](https://sfamjournals.onlinelibrary.wiley.com/action/showCitFormats?doi=10.1111%2F1462-2920.14843) : 

Nogales, J., Mueller, J., Gudmundsson, S., Canalejo, F.J., Duque, E., Monk, J., Feist, A.M., Ramos, J.L., Niu, W. and Palsson, B.O. (2020), High-quality genome-scale metabolic modelling of Pseudomonas putida highlights its broad metabolic capabilities. Environ Microbiol, 22: 255-269. https://doi.org/10.1111/1462-2920.14843

[ibmCplexOptimizer](https://www.ibm.com/de-de/analytics/cplex-optimizer) :

Cplex, I. I. (2009). V12. 1: User’s Manual for CPLEX. International Business Machines Corporation, 46(53), 157.

[COBRA TOOLBOX](https://opencobra.github.io/cobratoolbox/stable/index.html) :

Laurent Heirendt & Sylvain Arreckx, Thomas Pfau, Sebastian N. Mendoza, Anne Richelle, Almut Heinken, Hulda S. Haraldsdottir, Jacek Wachowiak, Sarah M. Keating, Vanja Vlasov, Stefania Magnusdottir, Chiam Yu Ng, German Preciat, Alise Zagare, Siu H.J. Chan, Maike K. Aurich, Catherine M. Clancy, Jennifer Modamio, John T. Sauls, Alberto Noronha, Aarash Bordbar, Benjamin Cousins, Diana C. El Assal, Luis V. Valcarcel, Inigo Apaolaza, Susan Ghaderi, Masoud Ahookhosh, Marouen Ben Guebila, Andrejs Kostromins, Nicolas Sompairac, Hoai M. Le, Ding Ma, Yuekai Sun, Lin Wang, James T. Yurkovich, Miguel A.P. Oliveira, Phan T. Vuong, Lemmer P. El Assal, Inna Kuperstein, Andrei Zinovyev, H. Scott Hinton, William A. Bryant, Francisco J. Aragon Artacho, Francisco J. Planes, Egils Stalidzans, Alejandro Maass, Santosh Vempala, Michael Hucka, Michael A. Saunders, Costas D. Maranas, Nathan E. Lewis, Thomas Sauter, Bernhard Ø. Palsson, Ines Thiele, Ronan M.T. Fleming, Creation and analysis of biochemical constraint-based models: the COBRA Toolbox v3.0, Nature Protocols, volume 14, pages 639–702, 2019 doi.org/10.1038/s41596-018-0098-2.

[MATLAB](- https://de.mathworks.com/products/matlab.html) :

MATLAB, 2021. version: 9.10.0.1739362 (R2021a) Update 5, Natick, Massachusetts: The MathWorks In
