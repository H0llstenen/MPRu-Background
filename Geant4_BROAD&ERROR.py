import csv
import matplotlib.pyplot as plt
import numpy as np

bin_size = 60

pz_limit = 0.9945

file_path_500 = 'C:\\Users\\Elina\\mpru-analysis\\MPRuGdSimulation_500.txt'

def gaussian(E_axis, bin_center, sigma):
    G = 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(E_axis-bin_center)**2/(2*sigma**2))
    dE = E_axis[1] - E_axis[0]
    G = G * dE
    return G

def read_file(file_path):
    dict_lst = {'kE': [], 'px': [], 'py': [], 'pz': [], 'weight': [],  'pdg': [] } # dictonary containing all lists, lists created here!

    with open(file_path, "r") as file:
        read_file = csv.DictReader(file, delimiter='\t')
        read_file.fieldnames = [header_name.strip() for header_name in read_file.fieldnames]

        for row in read_file:
            dict_lst['kE'].append(float(row['kE'])) # call the list
            dict_lst['px'].append(float(row['px']))
            dict_lst['py'].append(float(row['py']))
            dict_lst['pz'].append(float(row['pz']))
            dict_lst['weight'].append(float(row['weight']))
            dict_lst['pdg'].append(int(row['pdg']))
    return dict_lst

# read in files and lists


lst_500 = read_file(file_path_500) # read out dictionary

kE_500 = np.array(lst_500['kE']) # call the lists from within dictionary!
px_500 = np.array(lst_500['px']) # create np arrays to use numpy operators 
py_500 = np.array(lst_500['py'])
pz_500 = np.array(lst_500['pz'])
weight_500 = np.array(lst_500['weight'])
pdg_500 = np.array(lst_500['pdg'])



# ----------------  ONLY PROTONS with pz limit straight away!!!



onlyPpz_filter = (pdg_500 == 2212) & (pz_500 >= pz_limit) # protons and pz direction (forward)
kE_500 = kE_500[onlyPpz_filter]
px_500 = px_500[onlyPpz_filter]
py_500 = py_500[onlyPpz_filter]
pz_500 = pz_500[onlyPpz_filter]
weight_500 = weight_500[onlyPpz_filter]
pdg_500 = pdg_500[onlyPpz_filter]


counts, bin_edges, patches =plt.hist(kE_500, weights=weight_500, bins=bin_size, alpha=0, label=None)
bincenters = (bin_edges[:-1]+bin_edges[1:])/2

bincenters = np.array(bincenters)
bincenters = bincenters *10**3


# plot the histogram, only protons pz
plt.hist(kE_500, weights=weight_500, bins=bin_size, label=f'500 µm', color='indianred') # add \nTot count sum... back into every plot!!
plt.title('Energy Histogram for Protons after Foil')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.ylabel('Weighted #protons')
plt.show()


# find the amount of counts in each bin for paint vs. not paint


onlyPpaintpz_filter = (weight_500 == 0.00817061) & (pdg_500 == 2212) & (pz_500 >= pz_limit)  # only paint, pz
countspaintpz, _, _ = plt.hist(kE_500[onlyPpaintpz_filter], bins=bin_size, alpha=0, label=None)

onlyPfoilpz_filter = (weight_500 != 0.00817061) & (pdg_500 == 2212) & (pz_500 >= pz_limit)  # only foil window, pz
countsfoilpz, _, _ = plt.hist(kE_500[onlyPfoilpz_filter], bins=bin_size, alpha=0, label=None)
# no weight used for counts for errors!!!

# saved in two lists the corresponding counts in each bin (no broadening yet!)

#calculate each sigma_i in all bins, with two different weights
sigma_bins = []

w1 = 0.00817061 # weight in paint
w2 = 0.991829 # weight in foil/window
for i in range(len(bincenters)):
    sigma_bins.append(np.sqrt(w1**2*countspaintpz[i] + w2**2*countsfoilpz[i]))


#OBSERVE: sigma_bins countain all respective bins errors now!!

# --------------------- NOW APPLY BROADENING

# standard deviation of broadening Gaussian
T = 15 # keV, ion temps
gaussian_sigma = np.sqrt(2*1/5*14000)*np.sqrt(T)
print(gaussian_sigma)
#75.2*np.sqrt(15)




counts_broad = np.zeros_like(counts)
sigma_broad = np.zeros_like(counts)

for i in range(len(bincenters)):
    bin = bincenters[i]
    x = counts[i]
    sigma_x = sigma_bins[i]
    A = gaussian(bincenters, bin, gaussian_sigma)
    u = A*x
    counts_broad = counts_broad + u

    #CHANGED TEST!!!
    if i == 59:
        print(np.sum(u))
        print(x)
    #END TEST!!!

    sigma_u = A*sigma_x
    sigma_broad = sigma_broad + sigma_u     # double check this! Not uncorrelated events



# plot broadened error and compare w\ original
plt.figure()
plt.errorbar(bincenters, counts, yerr=sigma_bins, label='original')
plt.errorbar(bincenters, counts_broad, yerr=sigma_broad, label='broad')
plt.legend()
plt.show()



# plot original error for each bin
plt.figure()
plt.bar(bincenters, counts, width=(bincenters[1]-bincenters[0]), align='center', color='indianred', edgecolor='maroon', label='500 µm')
plt.errorbar(bincenters, counts, yerr=sigma_bins, fmt='o', color='black', markersize = 1, label='Error Bars')
plt.title(f'Broadened Energy Histogram for Protons, pz>{pz_limit}')
plt.ylabel('Weighted #protons')
plt.xlabel('Energy [keV]')
plt.legend()
plt.show()






# -------------------------- ONLY WINDOW/FOIL CREATED PROTONS; BROADENING, pz forward

onlyPfoil_filter = (weight_500 != 0.00817061) & (pdg_500 == 2212) & (pz_500 >= pz_limit) # protons but created elsewhere than paint, mostly in foil

kE_500pfoil = kE_500[onlyPfoil_filter]
weight_500pfoil = weight_500[onlyPfoil_filter]


counts, bin_edges, patches =plt.hist(kE_500pfoil, weights=weight_500pfoil, bins=bin_size, alpha=0, label=None)

bin_edges = bin_edges*10**3 # REMEMBER!!!

bincenters = (bin_edges[:-1]+bin_edges[1:])/2

bincenters_diff = bincenters[1]-bincenters[0] # take out the difference between bins
for _ in range(10): # append 10 more bins, to plot further when broadening occurs! Extend list
    bincenters = np.append(bincenters, bincenters[-1]+bincenters_diff)
    counts = np.append(counts, 0)

total_spectrafoil = np.zeros_like(bincenters, dtype=np.float64)

for count_i, bin_i in zip(counts, bincenters): # zip create [(,)] tuple in each entry, which can be used in the for loop
    total_spectrafoil += (count_i * gaussian(bincenters, bin_i, gaussian_sigma)) # all values in keV!

plt.plot(bincenters, total_spectrafoil)
plt.title('p created in foil/window, Gaussian')
plt.xlabel('Energy [keV]')
plt.show()

# -------------------------- ONLY PAINT CREATED PROTONS; BROADENING, pz forward

onlyPpaint_filter = (weight_500 == 0.00817061) & (pdg_500 == 2212) & (pz_500 >= pz_limit)# protons but created elsewhere than paint, mostly in foil

kE_500ppaint = kE_500[onlyPpaint_filter]
weight_500ppaint = weight_500[onlyPpaint_filter]


counts, bin_edges, patches =plt.hist(kE_500ppaint, weights=weight_500ppaint, bins=bin_size, alpha=0, label=None)


bin_edges = bin_edges*10**3 # REMEMBER!!!

bincenters = (bin_edges[:-1]+bin_edges[1:])/2


for _ in range(10): # append 10 more bins, to plot further when broadening occurs! Extend list
    bincenters = np.append(bincenters, bincenters[-1]+bincenters_diff)
    counts = np.append(counts, 0)


total_spectrapaint = np.zeros_like(bincenters, dtype=np.float64)

for count_i, bin_i in zip(counts, bincenters): # zip create [(,)] tuple in each entry, which can be used in the for loop
    total_spectrapaint += (count_i * gaussian(bincenters, bin_i, gaussian_sigma)) # all values in keV!

plt.plot(bincenters, total_spectrapaint)
plt.title('p created in foil/window, Gaussian')
plt.xlabel('Energy [keV]')
plt.show()






#-------------TOTAL BROADENED SPECTRUM WITH BOTH PAINT AND FOIL COMPONENT
plt.figure()
plt.plot(bincenters,total_spectrapaint, color = 'fuchsia', label = 'Paint')
plt.plot(bincenters,total_spectrafoil, color = 'black', linestyle = 'dashdot', label='Window/Foil')
plt.title('Broadened Energy Histogram w\ Paint and Window/Foil Components')
plt.xlabel('Energy [keV]')
plt.ylabel('Weighted #protons')
plt.legend()
plt.show()




# ---------TRY TO IMPLEMENT LONGER ENERGY-AXIS!!!!!!!!







