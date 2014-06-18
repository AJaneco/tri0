#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classy_continuity import Reaction

T = 298.
N = 2.688e19
ne = 5.e14
ppod = 100
#tm = 1.e-1

reactions=[
  Reaction('O+H+M=OH+M', 4.36e-32), 
  Reaction('CH3+O=CH2O+H', 1.3e-10), 
  Reaction('CH2O+H=CHO+H2', 8.71e-12, -1510.), 
  Reaction('CH2O+O=CHO+OH', 3.e-11, -1550.), 
  Reaction('CH2O+OH=CHO+H2O', 4.74e-12, 225.), 
  Reaction('CHO+H=CO+H2', 2.e-10), 
  Reaction('CHO+O=CO+OH', 5.e-11), 
  Reaction('CHO+OH=CO+H2O', 5.e-11), 
  Reaction('CHO+CHO=CH2O+CO', 3e-11), 
  Reaction('CH3+CHO=CH4+CO', 2.e-10), 
  Reaction('CO+O+M=CO2+M', 1.7e-23, -1510.), 
  Reaction('CO+OH=CO2+H', 2.4e-13), 
  Reaction('H+H+M=H2+M', 9.11e-33), 
  Reaction('OH+H=O+H2', 6.86e-14, -1950.), 
  Reaction('CH4+H=CH3+H2', 9.87e-13, -4406.), 
  Reaction('OH+H2=H+H2O', 2.51e-14, -4384.), 
  Reaction('C+O+M=CO+M', 2.8e-33), 
  Reaction('CO2+H=CO+OH', 2.5e-10, -13300.), 
  Reaction('CH4+O=CH3+OH', 8.75e-12, -4330.),
  Reaction('CO2+e=CO+O+e', 2.e-13), 
  Reaction('CH4+e=CH3+H+e', 4.5e-13), 
  Reaction('CO+e=C+O+e', 1.e-17), 
  Reaction('H2+e=H+H+e', 1.e-16)
  ]

conc_i = {
  'CH4': 0.2,
  'CO2': 0.8,
  'e': ne/N
  }
dens_i={}
for g in conc_i.keys():
  dens_i[g] = conc_i[g]*N