deren_production_list = []

# Assuming only one sigma value
sigma_value = 0.25

with open('/home/user/Documents/GitHub/Thermodynamic_Integration/total_der_energies', 'r') as file:
    lines = file.readlines()
    temp_list = []
    for i, line in enumerate(lines):
        if i % 2 == 1:
            temp_list.append(line)
        
    deren_production_list.append(temp_list)

for elem_index, elem in enumerate(deren_production_list):
    deren_production_list[elem_index] = [line for line in elem if '*' not in line]
    
    print(sigma_value)
    print(len(elem), '\n')
    print(deren_production_list[elem_index])
    
    with open('/home/user/Documents/GitHub/Thermodynamic_Integration/total_der_energies_cleaned', 'w') as file:
        file.writelines(deren_production_list[elem_index])
