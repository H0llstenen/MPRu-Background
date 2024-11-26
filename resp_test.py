import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import statistics as st
import pandas as pd
import json
import seaborn as sns

def neutron_distr(x):
    return np.exp((-(x-1000)**2)/20000)

# Load response function
drf_file = 'MPRu_response.json'

drf_file = open(drf_file, 'r') # read in json
drf = json.load(drf_file)
drf_file.close()

En = np.array(drf['x']) # list to array
Xpos = np.array(drf['y'])
matrix = np.array(drf['matrix'])
ch = np.arange(len(Xpos)) # just get channels

plt.pcolor(En,ch,matrix.T)
plt.ylabel('[channel]')
plt.xlabel('[En (keV)]')

plt.figure()
i = 1000
plt.plot(ch, matrix[i])
plt.title(f'En = {En[i]}')
plt.xlabel('channel')
plt.show()

# Resp.func for neutron spectra with mean value of En = 15 MeV to position
plt.figure()
plt.plot(Xpos, matrix[i])
plt.title(f'En = {En[i]}')
plt.xlabel('Xpos')
plt.show()


# take peak maxima for array of energies and then get corresponding channels, diff channel number corr energy
# FOr each neutron energy, find the hodoscope channel with most counts, ch_max = f(En).
# response function, how the neutron energy is mapped to proton recoil energy spectra


channels_maxima = [] # when proton peak occurs
energy_list = [] # neutron energy
for i in range(500, 1500):
    protonEmax_index = list(matrix[i]).index(np.max(matrix[i])) # matrix(i) is the spec neutron energy corresponding to a proton answer of energies
    channels_maxima.append(ch[protonEmax_index])
    energy_list.append(En[i]) # NOT CORRECT


# close neutron energy will appear in same channel due to resolution of the channels (better res in middle, less wide scintillators)
plt.scatter(energy_list, channels_maxima)
plt.title('Channel maxima')
plt.xlabel('Indcident neutron E [keV]')
plt.ylabel('Channel maxima in proton repsonse')
plt.show()

index_ch5 = list(channels_maxima).index(8)
n_E5 = En[index_ch5]
index_ch16 = list(channels_maxima).index(19)
n_E16 = En[index_ch16]
print(f"{n_E16-n_E5} keV") # energy difference between channel 5 and 16, comparison to shot 104335



# Neutron Spectra creation 

neutron_spectr = []
for i in range(0,len(En)): 
    neutron_spectr.append(neutron_distr(i))

# print(len(En)) # 2000 points!!!

plt.figure()
plt.plot(En, neutron_spectr)
plt.xlabel('En [keV]')
plt.ylabel('dN/dE')
plt.title('Neutron Spectra')
plt.show()

# neutron_spectr is now a vector with weights of how much different responsefunctions should be in the ''real'' result
# each En respond to a different response function

# something like matrix[i]*weight[i] for all energies
# total = np.matmul(matrix, neutron_spectr)
# neutron_spectr requires a dimension as a matrix (not a flat list), it can be doen with reshape

neutron_spectr = np.reshape(neutron_spectr, (2000, 1)) # give dimension
matrix_trans = np.transpose(matrix) # match shapes

total_pmatrix = np.dot(matrix_trans, neutron_spectr)

# print(np.shape(total_pmatrix))

plt.figure()
plt.plot(ch, total_pmatrix)
plt.xlabel('channels')
plt.ylabel('counts (p)')
plt.title('Protons')
plt.show()



