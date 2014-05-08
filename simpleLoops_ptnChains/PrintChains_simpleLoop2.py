#!/usr/bin/env python

#####
# Author: Dale Housler
# Creaton Date: 08-05-2014
# PROGRAM: ProteinChians_simpleLoop.py
#####

#####
# This program prints all chains
# provides an example of a simple while loop with user input
#####

chain_number = int(input("How many chains are there? "))

## Loops through user input ##
i = 1
while i <= chain_number:
    print(i)
    i+= 1
## end ##
    
input("Press any key to exit.")
