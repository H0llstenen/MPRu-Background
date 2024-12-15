import pickle
import matplotlib.pyplot as plt
import numpy as np

f = open('spec_components_104522.pickle', 'rb')
c = pickle.load(f)

def function_tot(x, maximum):
    if x <= maximum:
        # 1st Gaussian (centered peak, broader width)
        return 3500000000 * np.exp(-(x - maximum) ** 2 / 900)
    else:
        # 2nd Gaussian (centered peack, sharper width)
        return 3500000000 * np.exp(-(x - maximum) ** 2 / 200) 

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


# plot containing 
plt.plot(energy_axis, thermic_fit, color = 'b', linestyle = 'dashed', label = 'TH') # thermic bulk plasma
plt.plot(energy_axis, beam_fit, linestyle = 'dashdot', color = 'g', label = 'BT') # thermic beam injection 
plt.plot(energy_axis, total_fit, color = 'r', label = 'total')
plt.plot(energy_axis, tot_background, color='black', linestyle='dotted', label='Fitted Background')
plt.legend()
plt.xlabel('En [keV]')
plt.ylabel('dN/dE')
plt.title('Neutron data, Two Gaussians')
plt.show()


np.savez('twogaussians.npz', En=energy_axis, spec=tot_background)
