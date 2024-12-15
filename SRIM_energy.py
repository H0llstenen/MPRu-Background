import matplotlib.pyplot as plt
import numpy as np

file_14 = 'transmit14.txt'
file_19 = 'transmit19.txt'
file_24 = 'transmit24.txt'

def read_txtfile(file_path):
    Ek=[]
    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith('T'): # check that this is transmitted
                symbols = line.split() # split if a space or similar as seperator
                
                energies = symbols[2].replace(',', '.') # SRIM uses comma, python interpret . change! The kinetic energy! Python can understand E07 etc..
                energy_values = float(energies) # make it a number

                # Append the energy value to the list
                Ek.append(energy_values)
    return Ek


mean_energy_14 = np.mean(read_txtfile(file_14))
incident_E14 = 14000000 # 14MeV

print(f'Mean energy of transmitted ions: {round(mean_energy_14*10**(-6), 2)} MeV')
print(f'Mean energy lost: {round((incident_E14-mean_energy_14)*10**(-6), 2)} MeV')

percentage_14 = (incident_E14-mean_energy_14)/incident_E14



mean_energy_24 = np.mean(read_txtfile(file_24))
incident_E24 = 24000000 # 24MeV

print(f'Mean energy of transmitted ions: {round(mean_energy_24*10**(-6), 2)} MeV')
print(f'Mean energy lost: {round((incident_E24-mean_energy_24)*10**(-6), 2)} MeV')

percentage_24 = (incident_E24-mean_energy_24)/incident_E24



mean_energy_19 = np.mean(read_txtfile(file_19))
incident_E19 = 19000000 # 19MeV

print(f'Mean energy of transmitted ions: {round(mean_energy_19*10**(-6), 2)} MeV')
print(f'Mean energy lost: {round((incident_E19-mean_energy_19)*10**(-6), 2)} MeV')

percentage_19 = (incident_E19-mean_energy_19)/incident_E19


incident_lst = [incident_E14*10**(-6), incident_E19*10**(-6), incident_E24*10**(-6)]
perc_lst = [percentage_14, percentage_19, percentage_24] 

plt.bar(incident_lst, perc_lst, color = 'indianred')
plt.title('Percentage of Energy Loss')
plt.ylabel('Percentage energy loss [%]')
plt.xlabel('Incident proton energy [MeV]')
plt.show()




