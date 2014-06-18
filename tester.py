#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classy_continuity import Reaction

N0 = 1.e19 # cm-3
ne0 = 1.e10 #  cm-3

T0 = None #K
ppod = None
tm= None # s
ti= None # s


reactions = [
  #Reaction('AB+/e>B/A', 2.e-13), # test_A
  #Reaction('CH4/e>CH4+/e/e', 'Ionis4'), # test_B
  #Reaction('CH4+/e>CH4', 2.e-9), # test_B
  Reaction('He/e>He+/e/e', 'Ionizati'), # test_C
  Reaction('He+/e/M>He/M', 1.e-25), # test_C
  ]

dens_i = {
  #'AB+': 0.5*N0, # test_A
  #'e': 0.5*N0, # test_A
  #'CH4': N0, # test_B
  #'e': ne0 # test_B
  'He': N0, # test_C
  'e': 1. # test_C
  }

def fieldt (t):
  """
  Da/devolve o campo reduzido num dado instante
  """
  return 75.