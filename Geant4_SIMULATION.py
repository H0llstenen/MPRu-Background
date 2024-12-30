import csv
import matplotlib.pyplot as plt
import numpy as np

file_path_500 = 'C:\\Users\\Elina\\mpru-analysis\\MPRuGdSimulation_500tot.txt'

bin_count = 60

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


# all particles
# plot the histogram
plt.hist(kE_500, weights=weight_500, bins=bin_count, label=f'Tot count: {len(kE_500)}\n500 µm', color='indianred', edgecolor='maroon')
plt.title('Energy Histogram, All Charged Particles')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.ylabel('Weighted #charged particles')
plt.show()


# ----------------  ONLY PROTONS
#create boolean list:
onlyP_filter = (pdg_500 == 2212) # return false or true 

kE_500 = kE_500[onlyP_filter] # from now on only protons in kE_250 and so on...
px_500 = px_500[onlyP_filter]
py_500 = py_500[onlyP_filter]
pz_500 = pz_500[onlyP_filter]
weight_500 = weight_500[onlyP_filter]
pdg_500 = pdg_500[onlyP_filter]


sum_p = 0
for el in onlyP_filter:
    if el==True:
        sum_p += 1


# plot the histogram, only protons 
plt.hist(kE_500, weights=weight_500, bins=bin_count, label=f'Tot counts: {sum_p}\n500 µm', color='indianred', edgecolor='maroon') # add \nTot count sum... back into every plot!!
plt.title('Energy Histogram for Protons after Foil')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.ylabel('Weighted #protons')
plt.show()

# momentum
fig, axs = plt.subplots(1, 3, figsize=(15, 4))

axs[0].hist(px_500, weights=weight_500, bins= bin_count, label='px \n500 µm', color='indianred', edgecolor='maroon')
axs[0].set_xlabel('Unit Momentum Vector in X')
axs[0].set_ylabel('Weighted #protons')
axs[0].legend()
axs[1].hist(py_500, weights=weight_500, bins= bin_count, label='py \n500 µm', color='indianred', edgecolor='maroon')
axs[1].set_xlabel('Unit Momentum Vector in Y')
axs[1].legend()
axs[2].hist(pz_500, weights=weight_500, bins= bin_count, label='pz \n500 µm', color='indianred', edgecolor='maroon')
axs[2].set_xlabel('Unit Momentum Vector in Z')
axs[2].legend()

fig.suptitle('Unit Momentum Vector Histogram')
fig.tight_layout()
plt.show()

# ONLY protons created in paint
onlyPpaint_filter = (weight_500 == 0.00817061) & (pdg_500 == 2212) # only protons and only in paint, (pdg_250 == 2212) req to get sum correct

kE_500ppaint = kE_500[onlyPpaint_filter]
weight_500ppaint = weight_500[onlyPpaint_filter]

sum_ppaint = 0
for el in onlyPpaint_filter:
    if el == True:
        sum_ppaint+=1


print(f'\#protons created in paint: {sum_ppaint}')


plt.hist(kE_500ppaint, weights=weight_500ppaint, bins=bin_count, label=f'Tot counts: {sum_ppaint}\n500 µm', color='indianred', edgecolor='maroon')
plt.title('Energy Histogram for Protons w\ Origin in Paint')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.ylabel('Weighted #protons')
plt.show()

# protons created NOT in paint (vacuum window and foil)


sum_pfoil = sum_p-sum_ppaint
print(f'\#protons NOT created in paint: {sum_pfoil}')

onlyPfoil_filter = (weight_500 != 0.00817061) & (pdg_500 == 2212) # protons but created elsewhere than paint, mostly in foil

kE_500pfoil = kE_500[onlyPfoil_filter]
weight_500pfoil = weight_500[onlyPfoil_filter]

plt.hist(kE_500pfoil, weights=weight_500pfoil, bins=bin_count, label=f'Tot counts: {sum_pfoil}\n500 µm', color='indianred', edgecolor='maroon')
plt.title('Energy Histogram for Protons w\ Origin in Foil/Window')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.ylabel('Weighted #protons')
plt.show()



# Create plots with higher than ___ given pz
pz_limit = 0.9945

#0.954

#0.9945



# all proton w\ pz


onlyPpz = (pdg_500 == 2212) & (pz_500 >= pz_limit)

sum_Ppz = 0
for el in onlyPpz:
    if el == True:
        sum_Ppz+=1


kE_500ppz = kE_500[onlyPpz]
weight_500ppz = weight_500[onlyPpz]

plt.hist(kE_500ppz, weights=weight_500ppz, bins=bin_count, label=f'Tot counts: {sum_Ppz}\n500 µm', color='indianred', edgecolor='maroon')
plt.title(f'Energy Histogram for Protons, pz>{pz_limit}')
plt.xlabel('Energy [MeV]')
plt.ylabel('Weighted #protons')
plt.legend()
plt.show()


# protons in paint w\ pz 


onlyPpzpaint = (weight_500 == 0.00817061) & (pdg_500 == 2212) & (pz_500 >= pz_limit) 


sum_PpzPaint = 0
for el in onlyPpzpaint:
    if el == True:
        sum_PpzPaint +=1


kE_500ppzPaint = kE_500[onlyPpzpaint]
weight_500ppzPaint = weight_500[onlyPpzpaint]

plt.hist(kE_500ppzPaint, weights=weight_500ppzPaint, label=f'Tot counts: {sum_PpzPaint}\n500 µm', bins=bin_count, color='indianred', edgecolor='maroon')
plt.title(f'Energy Histogram for Protons w\ Origin in Paint, pz>{pz_limit}')
plt.xlabel('Energy [MeV]')
plt.ylabel('Weighted #protons')
plt.legend()
plt.show()


# protons NOT in paint w\ pz 

onlyPpzfoil = (weight_500 != 0.00817061) & (pdg_500 == 2212) & (pz_500 >= pz_limit) 

sum_PpzFoil = sum_Ppz - sum_PpzPaint

kE_500ppzfoil = kE_500[onlyPpzfoil]
weight_500ppzfoil = weight_500[onlyPpzfoil]

plt.hist(kE_500ppzfoil, weights=weight_500ppzfoil, label=f'Tot counts: {sum_PpzFoil}\n500µm', bins=bin_count, color='indianred', edgecolor='maroon')
plt.title(f'Energy Histogram for Protons w\ Origin in Foil/Window, pz>{pz_limit}')
plt.xlabel('Energy [MeV]')
plt.ylabel('Weighted #protons')
plt.legend()
plt.show()


