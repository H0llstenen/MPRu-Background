import pickle
import matplotlib.pyplot as plt
import numpy as np

f = open('spec_components_104522.pickle', 'rb')
c = pickle.load(f)

# global set of variables handling the slopes of the lines:
k1 = 0.06E8
k2 = 0.01E8
k3 = 0.04E8
k4 = 0.02E8
k5 = -0.02E8
k6 = -0.001E8
k7 = -0.08E8
k8 = -0.2E8
k9 = -0.4E8
k10 = -0.65E8

m1 = 3.2E9 # start
m2 = None # calculated inside intervals
m3 = None
m4 = None
m5 = None
m6 = None
m7 = None
m8 = None
m9 = None
m10 = None

def intervals(x, l_points):  # l_points interval points
    global k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10 # create access
    if x <= l_points[0]:
        return k1 * x + m1
    elif x <= l_points[1]:
        m2 = k1*l_points[0] + m1 - k2*l_points[0] # for continuity last point in k1*x+m1 above! y1 = k2*x + m 
        return k2 * x + m2
    elif x <= l_points[2]:
        m3 = k2*l_points[1] + m2 - k3*l_points[1]
        return k3 * x + m3
    elif x <= l_points[3]:
        m4 = k3*l_points[2] + m3 - k4*l_points[2]
        return k4 * x + m4
    elif x <= l_points[4]:
        m5 = k4*l_points[3] + m4 - k5*l_points[3]
        return k5* x + m5
    elif x <= l_points[5]:
        m6 = k5*l_points[4] + m5 - k6*l_points[4]
        return k6* x + m6
    elif x <= l_points[6]:
        m7 = k6*l_points[5] + m6 - k7*l_points[5]
        return k7* x + m7
    elif x <= l_points[7]:
        m8 = k7*l_points[6] + m7 - k8*l_points[6]
        return k8* x + m8
    elif x <= l_points[8]:
        m9 = k8*l_points[7] + m8 - k9*l_points[7]
        return k9* x + m9
    elif x <= l_points[9]:
        m10 = k9*l_points[8] + m9 - k10*l_points[8]
        return k10* x + m10
    else:
        return 0



energy_axis = c['En']
thermic_fit = c['th']
beam_fit = c['bt']
total_fit = thermic_fit + beam_fit # component-wise

length = np.arange(0,len(energy_axis))
l_points = [20, 60, 90, 130, 160, 190, 210, 250, 280, 300] # the interval region changes

tot_background = []
for i in range(0,len(energy_axis)): # creates first part of list
    tot_background.append(intervals(i, l_points))


# dE = 1200 keV approx!!

# plot containing 
plt.plot(energy_axis, thermic_fit, color = 'b', linestyle = 'dashed', label = 'TH') # thermic bulk plasma
plt.plot(energy_axis, beam_fit, linestyle = 'dashdot', color = 'g', label = 'BT') # thermic beam injection 
plt.plot(energy_axis, total_fit, color = 'r', label = 'total')
plt.plot(energy_axis, tot_background, color='black', linestyle='dotted', label='Background')
plt.plot()
plt.legend()
plt.xlabel('En [keV]')
plt.ylabel('dN/dE')
plt.title('Neutron data, Linear')
plt.show()

np.savez('deltalinear.npz', En=energy_axis, spec=tot_background)


