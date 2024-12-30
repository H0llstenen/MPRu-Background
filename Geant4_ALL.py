import csv
import matplotlib.pyplot as plt
import numpy as np

file_path_250 = 'C:\\Users\\Elina\\mpru-analysis\\MPRuGdSimulation_250tot.txt'
file_path_500 = 'C:\\Users\\Elina\\mpru-analysis\\MPRuGdSimulation_500tot.txt'
file_path_1000 = 'C:\\Users\\Elina\\mpru-analysis\\MPRuGdSimulation_1000tot.txt'

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

lst_250 = read_file(file_path_250) # read out dictionary

kE_250 = np.array(lst_250['kE']) # call the lists from within dictionary!
px_250 = np.array(lst_250['px']) # create np arrays to use numpy operators 
py_250 = np.array(lst_250['py'])
pz_250 = np.array(lst_250['pz'])
weight_250 = np.array(lst_250['weight'])
pdg_250 = np.array(lst_250['pdg'])


lst_500 = read_file(file_path_500) # read out dictionary

kE_500 = np.array(lst_500['kE']) # call the lists from within dictionary!
px_500 = np.array(lst_500['px']) # create np arrays to use numpy operators 
py_500 = np.array(lst_500['py'])
pz_500 = np.array(lst_500['pz'])
weight_500 = np.array(lst_500['weight'])
pdg_500 = np.array(lst_500['pdg'])

lst_1000 = read_file(file_path_1000) # read out dictionary

kE_1000 = np.array(lst_1000['kE']) # call the lists from within dictionary!
px_1000 = np.array(lst_1000['px']) # create np arrays to use numpy operators 
py_1000 = np.array(lst_1000['py'])
pz_1000 = np.array(lst_1000['pz'])
weight_1000 = np.array(lst_1000['weight'])
pdg_1000 = np.array(lst_1000['pdg'])


''' # all particles
# plot the histogram
plt.hist(kE_500, weights=weight_500, bins=bin_count, label=f'500 µm', color='indianred')
plt.title('Energy Histogram, all particles')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.ylabel('Weighted #charged particles')
plt.show()
'''

# ----------------  ONLY PROTONS
#create boolean list:
onlyP_filter500 = (pdg_500 == 2212) # return false or true 
onlyP_filter250 = (pdg_250 == 2212)
onlyP_filter1000 = (pdg_1000 == 2212)

kE_500 = kE_500[onlyP_filter500] # from now on only protons in kE_250 and so on...
px_500 = px_500[onlyP_filter500]
py_500 = py_500[onlyP_filter500]
pz_500 = pz_500[onlyP_filter500]
weight_500 = weight_500[onlyP_filter500]
pdg_500 = pdg_500[onlyP_filter500]

kE_250 = kE_250[onlyP_filter250] # from now on only protons in kE_250 and so on...
px_250 = px_250[onlyP_filter250]
py_250 = py_250[onlyP_filter250]
pz_250 = pz_250[onlyP_filter250]
weight_250 = weight_250[onlyP_filter250]
pdg_250 = pdg_250[onlyP_filter250]

kE_1000 = kE_1000[onlyP_filter1000] # from now on only protons in kE_250 and so on...
px_1000 = px_1000[onlyP_filter1000]
py_1000 = py_1000[onlyP_filter1000]
pz_1000 = pz_1000[onlyP_filter1000]
weight_1000 = weight_1000[onlyP_filter1000]
pdg_1000 = pdg_1000[onlyP_filter1000]



counts250, bin_edges250, patches250 = plt.hist(kE_250, weights=weight_250, bins=bin_count, alpha=0, label=None) # unpack histogram for information retrieval
bincenters250 = (bin_edges250[:-1] + bin_edges250[1:] )/ 2 # mean value of bins, with offset of lists to each other div by 2

counts500, bin_edges500, patches500 =plt.hist(kE_500, weights=weight_500, bins=bin_count, alpha=0, label=None)
bincenters500 = (bin_edges500[:-1] + bin_edges500[1:] )/ 2 

counts1000, bin_edges1000, patches1000 =plt.hist(kE_1000, weights=weight_1000, bins=bin_count, alpha=0, label=None)
bincenters1000 = (bin_edges1000[:-1] + bin_edges1000[1:] )/ 2 

# plot the outlines, only protons 

plt.plot(bincenters250, counts250, linewidth = 1.5,  label='250µm', color='forestgreen') # plot contour of histogram
plt.plot(bincenters500, counts500, linewidth = 1.5, label='500µm', color='indianred') # plot contour of histogram
plt.plot(bincenters1000, counts1000, linewidth = 1.5, label='1000µm', color='royalblue') # plot contour of histogram
plt.title('Contour of Energy Histogram for Protons after Foil')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.ylabel('Weighted #protons')
plt.show()


#  ----------------  MOMENTUM   

#250
Xcounts250, Xbin_edges250, Xpatches250 = plt.hist(px_250, weights=weight_250, bins=bin_count, alpha=0, label=None) # unpack histogram for information retrieval
Xbincenters250 = (Xbin_edges250[:-1] + Xbin_edges250[1:] )/ 2 # mean value of bins, with offset of lists to each other div by 2

Ycounts250, Ybin_edges250, Ypatches250 = plt.hist(py_250, weights=weight_250, bins=bin_count, alpha=0, label=None) # unpack histogram for information retrieval
Ybincenters250 = (Ybin_edges250[:-1] + Ybin_edges250[1:] )/ 2 # mean value of bins, with offset of lists to each other div by 2

Zcounts250, Zbin_edges250, Zpatches250 = plt.hist(pz_250, weights=weight_250, bins=bin_count, alpha=0, label=None) # unpack histogram for information retrieval
Zbincenters250 = (Zbin_edges250[:-1] + Zbin_edges250[1:] )/ 2 # mean value of bins, with offset of lists to each other div by 2

#500
Xcounts500, Xbin_edges500, Xpatches500 =plt.hist(px_500, weights=weight_500, bins=bin_count, alpha=0, label=None)
Xbincenters500 = (Xbin_edges500[:-1] + Xbin_edges500[1:] )/ 2 

Ycounts500, Ybin_edges500, Ypatches500 =plt.hist(py_500, weights=weight_500, bins=bin_count, alpha=0, label=None)
Ybincenters500 = (Ybin_edges500[:-1] + Ybin_edges500[1:] )/ 2 

Zcounts500, Zbin_edges500, Zpatches500 =plt.hist(pz_500, weights=weight_500, bins=bin_count, alpha=0, label=None)
Zbincenters500 = (Zbin_edges500[:-1] + Zbin_edges500[1:] )/ 2 

#1000

Xcounts1000, Xbin_edges1000, Xpatches1000 =plt.hist(px_1000, weights=weight_1000, bins=bin_count, alpha=0, label=None)
Xbincenters1000 = (Xbin_edges1000[:-1] + Xbin_edges1000[1:] )/ 2 

Ycounts1000, Ybin_edges1000, Ypatches1000 =plt.hist(py_1000, weights=weight_1000, bins=bin_count, alpha=0, label=None)
Ybincenters1000 = (Ybin_edges1000[:-1] + Ybin_edges1000[1:] )/ 2 

Zcounts1000, Zbin_edges1000, Zpatches1000 =plt.hist(pz_1000, weights=weight_1000, bins=bin_count, alpha=0, label=None)
Zbincenters1000 = (Zbin_edges1000[:-1] + Zbin_edges1000[1:] )/ 2 



fig, axs = plt.subplots(1, 3, figsize=(15, 4))

axs[0].plot(Xbincenters250, Xcounts250, label='250 µm', color='forestgreen')
axs[0].plot(Xbincenters500, Xcounts500, label='500 µm', color='indianred')
axs[0].plot(Xbincenters1000, Xcounts1000, label='1000 µm', color='royalblue')
axs[0].set_xlabel('Unit Momentum Vector in X')
axs[0].set_ylabel('Weighted #protons')
axs[0].legend()

axs[1].plot(Ybincenters250, Ycounts250, label='250 µm', color='forestgreen')
axs[1].plot(Ybincenters500, Ycounts500, label='500 µm', color='indianred')
axs[1].plot(Ybincenters1000, Ycounts1000, label='1000 µm', color='royalblue')
axs[1].set_xlabel('Unit Momentum Vector in Y')
axs[1].legend()

axs[2].plot(Zbincenters250, Zcounts250, label='250 µm', color='forestgreen')
axs[2].plot(Zbincenters500, Zcounts500, label='500 µm', color='indianred')
axs[2].plot(Zbincenters1000, Zcounts1000, label='1000 µm', color='royalblue')
axs[2].set_xlabel('Unit Momentum Vector in Z')
axs[2].legend()

fig.suptitle('Contour of Unit Momentum Vector')
fig.tight_layout()
plt.show()



# ------------- ONLY protons created in paint

onlyPpaint_filter250 = (weight_250 == 0.00409369) & (pdg_250 == 2212) # only protons and only in paint, (pdg_250 == 2212) req to get sum correct
onlyPpaint_filter500 = (weight_500 == 0.00817061) & (pdg_500 == 2212)
onlyPpaint_filter1000 = (weight_1000 == 0.0162745) & (pdg_1000 == 2212) # different weights!

# filter the lists
kE_250ppaint = kE_250[onlyPpaint_filter250]
weight_250ppaint = weight_250[onlyPpaint_filter250]

kE_500ppaint = kE_500[onlyPpaint_filter500]
weight_500ppaint = weight_500[onlyPpaint_filter500]

kE_1000ppaint = kE_1000[onlyPpaint_filter1000]
weight_1000ppaint = weight_1000[onlyPpaint_filter1000]


counts250, bin_edges250, patches250 = plt.hist(kE_250ppaint, weights=weight_250ppaint, bins=bin_count, alpha=0, label=None) # unpack histogram for information retrieval
bincenters250 = (bin_edges250[:-1] + bin_edges250[1:] )/ 2 # mean value of bins, with offset of lists to each other div by 2

counts500, bin_edges500, patches500 =plt.hist(kE_500ppaint, weights=weight_500ppaint, bins=bin_count, alpha=0, label=None)
bincenters500 = (bin_edges500[:-1] + bin_edges500[1:] )/ 2 

counts1000, bin_edges1000, patches1000 =plt.hist(kE_1000ppaint, weights=weight_1000ppaint, bins=bin_count, alpha=0, label=None)
bincenters1000 = (bin_edges1000[:-1] + bin_edges1000[1:] )/ 2


plt.plot(bincenters250, counts250, linewidth = 1.5,  label='250µm', color='forestgreen') # plot contour of histogram
plt.plot(bincenters500, counts500, linewidth = 1.5, label='500µm', color='indianred') # plot contour of histogram
plt.plot(bincenters1000, counts1000, linewidth = 1.5, label='1000µm', color='royalblue') # plot contour of histogram
plt.title('Contour of Energy Histogram for Protons w\ Origin in Paint')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.ylabel('Weighted #protons')
plt.show()



# ---------------- ONLY protons created in foil/window

onlyPfoil_filter250 = (weight_250 != 0.00409369) & (pdg_250 == 2212) # only protons and only in paint, (pdg_250 == 2212) req to get sum correct
onlyPfoil_filter500 = (weight_500 != 0.00817061) & (pdg_500 == 2212)
onlyPfoil_filter1000 = (weight_1000 != 0.0162745) & (pdg_1000 == 2212) # different weights!


kE_250pfoil = kE_250[onlyPfoil_filter250]
weight_250pfoil = weight_250[onlyPfoil_filter250]

kE_500pfoil = kE_500[onlyPfoil_filter500]
weight_500pfoil = weight_500[onlyPfoil_filter500]

kE_1000pfoil = kE_1000[onlyPfoil_filter1000]
weight_1000pfoil = weight_1000[onlyPfoil_filter1000]

counts250, bin_edges250, patches250 = plt.hist(kE_250pfoil, weights=weight_250pfoil, bins=bin_count, alpha=0, label=None) # unpack histogram for information retrieval
bincenters250 = (bin_edges250[:-1] + bin_edges250[1:] )/ 2 # mean value of bins, with offset of lists to each other div by 2

counts500, bin_edges500, patches500 =plt.hist(kE_500pfoil, weights=weight_500pfoil, bins=bin_count, alpha=0, label=None)
bincenters500 = (bin_edges500[:-1] + bin_edges500[1:] )/ 2 

counts1000, bin_edges1000, patches1000 =plt.hist(kE_1000pfoil, weights=weight_1000pfoil, bins=bin_count, alpha=0, label=None)
bincenters1000 = (bin_edges1000[:-1] + bin_edges1000[1:] )/ 2

plt.plot(bincenters250, counts250, linewidth = 1.5,  label='250µm', color='forestgreen') # plot contour of histogram
plt.plot(bincenters500, counts500, linewidth = 1.5, label='500µm', color='indianred') # plot contour of histogram
plt.plot(bincenters1000, counts1000, linewidth = 1.5, label='1000µm', color='royalblue') # plot contour of histogram
plt.title('Contour of Energy Histogram for Protons w\ Origin in Foil/Window')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.ylabel('Weighted #protons')
plt.show()



# ---------------- Create plots with higher than ___ given pz
pz_limit = 0.9945



# all proton w\ pz

onlyPpz250 = (pdg_250 == 2212) & (pz_250 >= pz_limit)
onlyPpz500 = (pdg_500 == 2212) & (pz_500 >= pz_limit)
onlyPpz1000 = (pdg_1000 == 2212) & (pz_1000 >= pz_limit)

kE_250ppz = kE_250[onlyPpz250]
weight_250ppz = weight_250[onlyPpz250]

kE_500ppz = kE_500[onlyPpz500]
weight_500ppz = weight_500[onlyPpz500]

kE_1000ppz = kE_1000[onlyPpz1000]
weight_1000ppz = weight_1000[onlyPpz1000]

counts250, bin_edges250, patches250 = plt.hist(kE_250ppz, weights=weight_250ppz, bins=bin_count, alpha=0, label=None) # unpack histogram for information retrieval
bincenters250 = (bin_edges250[:-1] + bin_edges250[1:] )/ 2 # mean value of bins, with offset of lists to each other div by 2

counts500, bin_edges500, patches500 =plt.hist(kE_500ppz, weights=weight_500ppz, bins=bin_count, alpha=0, label=None)
bincenters500 = (bin_edges500[:-1] + bin_edges500[1:] )/ 2 

counts1000, bin_edges1000, patches1000 =plt.hist(kE_1000ppz, weights=weight_1000ppz, bins=bin_count, alpha=0, label=None)
bincenters1000 = (bin_edges1000[:-1] + bin_edges1000[1:] )/ 2


plt.plot(bincenters250, counts250, linewidth = 1.5,  label='250µm', color='forestgreen') # plot contour of histogram
plt.plot(bincenters500, counts500, linewidth = 1.5, label='500µm', color='indianred') # plot contour of histogram
plt.plot(bincenters1000, counts1000, linewidth = 1.5, label='1000µm', color='royalblue') # plot contour of histogram
plt.title(f'Contour of Energy Histogram for Protons, pz>{pz_limit}')
plt.xlabel('Energy [MeV]')
plt.ylabel('Weighted #protons')
plt.legend()
plt.show()


# protons in paint w\ pz 


onlyPpzpaint250 = (weight_250 == 0.00409369) & (pdg_250 == 2212) & (pz_250 >= pz_limit) 
onlyPpzpaint500 = (weight_500 == 0.00817061) & (pdg_500 == 2212) & (pz_500 >= pz_limit)
onlyPpzpaint1000 = (weight_1000 == 0.0162745) & (pdg_1000 == 2212) & (pz_1000 >= pz_limit)


kE_250ppzPaint = kE_250[onlyPpzpaint250]
weight_250ppzPaint = weight_250[onlyPpzpaint250]

kE_500ppzPaint = kE_500[onlyPpzpaint500]
weight_500ppzPaint = weight_500[onlyPpzpaint500]

kE_1000ppzPaint = kE_1000[onlyPpzpaint1000]
weight_1000ppzPaint = weight_1000[onlyPpzpaint1000]

counts250, bin_edges250, patches250 = plt.hist(kE_250ppzPaint, weights=weight_250ppzPaint, bins=bin_count, alpha=0, label=None) # unpack histogram for information retrieval
bincenters250 = (bin_edges250[:-1] + bin_edges250[1:] )/ 2 # mean value of bins, with offset of lists to each other div by 2

counts500, bin_edges500, patches500 =plt.hist(kE_500ppzPaint, weights=weight_500ppzPaint, bins=bin_count, alpha=0, label=None)
bincenters500 = (bin_edges500[:-1] + bin_edges500[1:] )/ 2 

counts1000, bin_edges1000, patches1000 =plt.hist(kE_1000ppzPaint, weights=weight_1000ppzPaint, bins=bin_count, alpha=0, label=None)
bincenters1000 = (bin_edges1000[:-1] + bin_edges1000[1:] )/ 2

plt.plot(bincenters250, counts250, linewidth = 1.5,  label='250µm', color='forestgreen') # plot contour of histogram
plt.plot(bincenters500, counts500, linewidth = 1.5, label='500µm', color='indianred') # plot contour of histogram
plt.plot(bincenters1000, counts1000, linewidth = 1.5, label='1000µm', color='royalblue') # plot contour of histogram
plt.title(f'Contour of Energy Histogram for Protons w\ Origin in Paint, pz>{pz_limit}')
plt.xlabel('Energy [MeV]')
plt.ylabel('Weighted #protons')
plt.legend()
plt.show()


# ---- protons NOT in paint w\ pz  

onlyPpzfoil250 = (weight_250 != 0.00409369) & (pdg_250 == 2212) & (pz_250 >= pz_limit) 
onlyPpzfoil500 = (weight_500 != 0.00817061) & (pdg_500 == 2212) & (pz_500 >= pz_limit)
onlyPpzfoil1000 = (weight_1000 != 0.0162745) & (pdg_1000 == 2212) & (pz_1000 >= pz_limit)

kE_250ppzfoil = kE_250[onlyPpzfoil250]
weight_250ppzfoil = weight_250[onlyPpzfoil250]

kE_500ppzfoil = kE_500[onlyPpzfoil500]
weight_500ppzfoil = weight_500[onlyPpzfoil500]

kE_1000ppzfoil = kE_1000[onlyPpzfoil1000]
weight_1000ppzfoil = weight_1000[onlyPpzfoil1000]

counts250, bin_edges250, patches250 = plt.hist(kE_250ppzfoil, weights=weight_250ppzfoil, bins=bin_count, alpha=0, label=None) # unpack histogram for information retrieval
bincenters250 = (bin_edges250[:-1] + bin_edges250[1:] )/ 2 # mean value of bins, with offset of lists to each other div by 2

counts500, bin_edges500, patches500 =plt.hist(kE_500ppzfoil, weights=weight_500ppzfoil, bins=bin_count, alpha=0, label=None)
bincenters500 = (bin_edges500[:-1] + bin_edges500[1:] )/ 2 

counts1000, bin_edges1000, patches1000 =plt.hist(kE_1000ppzfoil, weights=weight_1000ppzfoil, bins=bin_count, alpha=0, label=None)
bincenters1000 = (bin_edges1000[:-1] + bin_edges1000[1:] )/ 2

plt.plot(bincenters250, counts250, linewidth = 1.5,  label='250µm', color='forestgreen') # plot contour of histogram
plt.plot(bincenters500, counts500, linewidth = 1.5, label='500µm', color='indianred') # plot contour of histogram
plt.plot(bincenters1000, counts1000, linewidth = 1.5, label='1000µm', color='royalblue') # plot contour of histogram
plt.title(f'Contour of Energy Histogram for p w\ Origin in Foil/Window, pz>{pz_limit}')
plt.xlabel('Energy [MeV]')
plt.ylabel('Weighted #protons')
plt.legend()
plt.show()


