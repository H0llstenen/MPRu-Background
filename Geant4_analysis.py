# Analysis for the Geant4 codes, included weighted energy histogram
import csv
import matplotlib.pyplot as plt

file_path = "C:\\Users\\Elina\\mpru-analysis\\testrun.txt"

# create lists
kE = [] # kinenergy, every index correspond to that spec particle in the other lists
px = [] # momentum lists
py = []
pz = []
weight = [] # weighted lists, tell where the charged particle was created
pdg = [] # tell type of spec charged partcile


with open(file_path, "r") as file:

    read_file = csv.DictReader(file, delimiter='\t') # reads in header as identifier with tab as the seperator

    # read_file has attribute fieldnames,
    read_file.fieldnames = [header_name.strip() for header_name in read_file.fieldnames] # take each header and take away blank sapces around them

    for row in read_file: # append from each row whilst file obj is till unclosed
        kE.append(float(row['kE'])) # append corresponding number to the header title
        px.append(float(row['px']))
        py.append(float(row['py']))
        pz.append(float(row['pz']))
        weight.append(float(row['weight']))
        pdg.append(int(row['pdg']))


# create energy histogram of all charged particles!

plt.hist(kE, weights=weight, bins= 40, label = f'Tot counts {len(kE)}', color='indianred', edgecolor = 'black')
plt.title('Energy histogram, all particles')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.ylabel('weighted #charged particles')
plt.show()


# create lists for only protons!

index_p = [] # saves index for other particles than protons 
for i in range(len(pdg)):
    if pdg[i] != 2212: # identifier for protons
        # print(pdg[i]) # investigate comp.
        index_p.append(i) # i is the index we are currently on

# mostly deutrons, some Fe ions, few Cr ions
# print(len(index_noprotons)) # total of other charged particles instead of ions in the current run


# remove all inputs with non-protons
for ind in reversed(index_p):
    del kE[ind]
    del px[ind]
    del py[ind]
    del pz[ind]
    del weight[ind]
# the lists are updated with only protons!

# create energy histogram for only protons!

plt.hist(kE, weights=weight, bins= 40, label = f'Tot counts {len(kE)}', color='indianred', edgecolor = 'black')
plt.title('Energy histogram, only p')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.ylabel('weighted #protons')
plt.show()



# Create histogram to show the px,pz,py distribution for all protons

#px
plt.hist(px, weights=weight, bins= 40, label = f'Tot counts {len(px)}', color='indianred', edgecolor = 'black')
plt.title('Momentum histogram, only p')
plt.xlabel('Momentum px, x-direction []')
plt.legend()
plt.ylabel('Weighted #protons')
plt.show()

#py
plt.hist(py, weights=weight, bins= 40, label = f'Tot counts {len(py)}', color='indianred', edgecolor = 'black')
plt.title('Momentum histogram, only p')
plt.xlabel('Momentum py, y-direction []')
plt.legend()
plt.ylabel('Weighted #protons')
plt.show()

#pz
plt.hist(pz, weights=weight, bins= 40, label = f'Tot counts {len(pz)}', color='indianred', edgecolor = 'black')
plt.title('Momentum histogram, only p')
plt.xlabel('Momentum pz, z-direction []')
plt.legend()
plt.ylabel('Weighted #protons')
plt.show()




index_ppaint = [] # index for protons not created in paint
sum_check = 0
for i in range(len(weight)):
    if weight[i] != 0.00817061:
        sum_check += 1
        index_ppaint.append(i)

print(f'Counts of protons not created in paint: {sum_check}') # number of protons created somewhere else than in the paint
# index of the one not created in paint 0.991829

# create copies with all generated protons! Can be used later in analysis
kE_p = kE.copy()
px_p = px.copy()
py_p = py.copy()
pz_p = pz.copy()
weight_p = weight.copy()


# ONLY protons created in paint
for ind in reversed(index_ppaint):
    del kE[ind]
    del px[ind]
    del py[ind]
    del pz[ind]
    del weight[ind]

# create energy histogram for only protons created in paint!

plt.hist(kE, weights=weight, bins= 40, label = f'Tot counts {len(kE)}', color='indianred', edgecolor = 'black')
plt.title('Energy histogram, p from paint')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.ylabel('weighted #protons')
plt.show()




# choose only protons with a pz component that is ___ and bigger! (pass the collimator)

pz_limit = 0.9940

# PAINT PRODUCED PROTONS
index_pz = [] # index for the particles that scatter too much for collimator
sum_pz = 0
for i in range(len(pz)):
    if pz[i] <= pz_limit: # the outputs that should be deleted
        sum_pz +=1
        index_pz.append(i)

# ALL PROTONS
index_pzp = [] # index for the particles that scatter too much for collimator, ALL PROTONS
sum_pzp = 0
for i in range(len(pz_p)):
    if pz_p[i] <= pz_limit: # the outputs that should be deleted,  ALL PROTONS
        sum_pzp +=1
        index_pzp.append(i)

print(f'#protons from paint with too low pz: {sum_pz}')
print(f'#protons with too low pz: {sum_pzp}')


# ONLY protons created in paint and with sufficiently high pz component
for ind in reversed(index_pz): # to avoid index shifts in loop
    del kE[ind]
    del px[ind]
    del py[ind]
    del pz[ind]
    del weight[ind]

# protons with sufficiently high pz component
for ind in reversed(index_pzp):
    del kE_p[ind]
    del px_p[ind]
    del py_p[ind]
    del pz_p[ind]
    del weight_p[ind]



# create energy histogram for protons! with pz above set limit

plt.hist(kE_p, weights=weight_p, bins= 40, label = f'Tot counts {len(kE_p)}', color='indianred', edgecolor = 'black')
plt.title('Energy histogram for p that pass collimator')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.ylabel('weighted #protons')
plt.show()

# create energy histogram for only protons created in paint! with pz above set limit

plt.hist(kE, weights=weight, bins= 40, label = f'Tot counts {len(kE)}', color='indianred', edgecolor = 'black')
plt.title('Energy histogram, p from PAINT that pass collimator')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.ylabel('weighted #protons')
plt.show()




