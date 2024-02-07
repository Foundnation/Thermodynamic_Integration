

out_path = '/home/user/Documents/GitHub/Thermodynamic_Integration/CaseStudy_1/Run/out'
data_path = '/home/user/Documents/GitHub/Thermodynamic_Integration/total_energies'
data_path_der = '/home/user/Documents/GitHub/Thermodynamic_Integration/total_der_energies'
data_path_avg = '/home/user/Documents/GitHub/Thermodynamic_Integration/avg_der_energies'

total_energies = []
total_der_energies = []
avg_der_energies = []
with open(out_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if 'Total energy end of simulation' in line:
            total_energies.append(line.split()[6])
        elif 'Total derivative of energy derEn' in line:
            total_der_energies.append(line.split()[6])
        # elif 'Ensemble average of derEn' in line:
        #     avg_der_energies.append(line.split()[5])

with open(data_path, 'w') as file:
    for energy in total_energies:
        file.write(energy + '\n')
        
with open(data_path_der, 'w') as file:
    for der_energy in total_der_energies:
        file.write(der_energy + '\n')
             
# with open(data_path_avg, 'w') as file:
#     for avg_der_energy in avg_der_energies:
#         file.write(avg_der_energy + '\n')
