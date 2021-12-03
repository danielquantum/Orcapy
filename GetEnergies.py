# -*- coding: utf-8 -*-
"""
Get energies from trajectories - Orca 5.0.1
"""

###########################################
# Input and Output files
###########################################
item='Reactant_trj.xyz'
out='energies.csv'

file_in = open(item,'r')
file_out = open(out, 'w+')

file_in_lines = file_in.readlines()

###########################################
# Creating a dictionary of energies
###########################################
list_of_energies = []
for line in (file_in_lines):
    if 'Coordinates' in line:
        linesplit = line.split() 		# a list
        #print(linesplit)
        energy = linesplit[5]
        list_of_energies.append(energy)
    file_in.close()

###########################################
# Write to csv
###########################################    
#print(list_of_energies)
for i, line in enumerate(list_of_energies):
    file_out.write(str(i) + ',' + str(line))
    file_out.write('\n')
file_out.close()
    