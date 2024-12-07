import pickle
import matplotlib.pyplot as plt
import numpy as np

f = open('spec_components_104522.pickle', 'rb')
c = pickle.load(f)

def function_tot(x, maximum): # two Gaussian meeting at maximum point
    if x <= maximum:
        # 1st Gaussian
        return 3500000000 * np.exp(-(x - maximum) ** 2 / 900) 
    else:
        # 2nd Gaussian
        return 3500000000 * np.exp(-(x - maximum) ** 2 / 400) 
# Parameters for nonsteep and midsteep: 900, 200 (denominator in Gaussian exponent)
# ...and for steep: 900, 400

energy_axis = c['En']
thermic_fit = c['th']
beam_fit = c['bt']
total_fit = thermic_fit + beam_fit # component-wise

"""
print(len(energy_axis))
print(len(thermic_fit))
print(len(beam_fit))
# OK all same length!
"""

maximum = 252 # CAN CHANGE MAXIMUM HERE!!!
#gives approx. 1400 kev between half right side of the peaks


tot_background = []
for i in range(0,len(energy_axis)): # creates first part of list
    tot_background.append(function_tot(i, maximum))

scaling_list = [] # array used to scale the Gaussians for steep 
for i in range(0, len(energy_axis)):
    if i <= 260: 
        scaling_list.append(1)
    elif i <=267: 
        scaling_list.append(0.97)
    else:
        scaling_list.append(0) 


scaling_list_mid = [] # array used to scale the Gaussians for midsteep
for i in range(0, len(energy_axis)):
    if i <= 260:
        scaling_list_mid.append(1)
    elif i <= 265:
        scaling_list_mid.append(1.1)
    elif i <= 267:
        scaling_list_mid.append(1.2)
    elif i <= 269:
        scaling_list_mid.append(1.3)
    elif i <= 278:
        scaling_list_mid.append(1.4)
    else:
        scaling_list_mid.append(0)


tot_background = np.array(tot_background) 

#steep
scaling_list = np.array(scaling_list) 
tot_spec = tot_background * scaling_list # for elementwise multiplication, only works for numpy arrays

#mid
scaling_list_mid = np.array(scaling_list_mid) 
tot_spec_mid = tot_background * scaling_list_mid

# plots
plt.plot(energy_axis, thermic_fit, color = 'b', linestyle = 'dashed', label = 'TH') # thermic bulk plasma
plt.plot(energy_axis, beam_fit, linestyle = 'dashdot', color = 'g', label = 'BT') # thermic beam injection 
plt.plot(energy_axis, total_fit, color = 'r', label = 'total')
plt.plot(energy_axis, tot_spec_mid, color='black', linestyle='dotted', label='Fitted Background') #tot_background, tot_spec, tot_spec_mid all OK choices of background
plt.legend()
plt.xlabel('En [keV]')
plt.ylabel('dN/dE')
plt.title('Neutron data, Background Models (nonsteep, midsteep, steep)')
plt.show()

np.savez('twoGaussians_model.npz', En=energy_axis, spec=tot_spec) 

