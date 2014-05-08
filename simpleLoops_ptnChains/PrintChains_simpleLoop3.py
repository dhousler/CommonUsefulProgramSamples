#!/usr/bin/env python

#####
# Author: Dale Housler
# Creaton Date: 08-05-2014
# PROGRAM: ProteinChians_simpleLoop.py
#####

#####
# This program prints all chains
# provides an example of a simple while loop from user input
# and prints pre-defined chains dependent on number of chains input by user
#####

chain_number = int(input("How many chains are there? "))
Chains = ['0','A','B','C','D','E','F','G','H','I','J',
          'K','L','M','N','O','P','Q','R','S','T',
          'U','V','W','X','Y','Z']

## loops through user defined number of chains ##
i = 1
while i <= chain_number:
    print(Chains[i])
    i+= 1
## end ##
    
input("Press any key to exit.")
