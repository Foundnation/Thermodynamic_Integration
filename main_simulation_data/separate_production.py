deren_production_list = []
sigma_values = [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5]

for s in sigma_values:
    with open('/home/user/Documents/GitHub/Thermodynamic_Integration/main_simulation_data/der_energies_' + str(s), 'r') as file:
        lines = file.readlines()
        temp_list = []
        for i, line in enumerate(lines):
            if i % 2 == 1:
                temp_list.append(line)
        
    deren_production_list.append(temp_list)


for elem_index, elem in enumerate(deren_production_list):
    deren_production_list[elem_index] = [line for line in elem if '*' not in line]
    
    print(sigma_values[elem_index])
    print(len(elem), '\n')
    print(deren_production_list[elem_index])
    
    with open('/home/user/Documents/GitHub/Thermodynamic_Integration/main_simulation_data/der_energies_cleaned_' + str(sigma_values[elem_index]), 'w') as file:
        file.writelines(deren_production_list[elem_index])


        
# for elem_index, elem in enumerate(deren_production_list):
#     new_elem = []
#     i = 0
#     while i < len(elem):
#         if '***' in elem[i]:
#             if i > 0 and i < len(elem) - 1 and not ('***' in elem[i - 1]) and not ('***' in elem[i + 1]):
#                 if elem[i - 1].strip().replace('*', '').replace('\n', '').replace(' ', '') != '':  # Check if convertible
#                     new_elem.append(str(0.5 * (float(elem[i - 1]) + float(elem[i + 1]))))
#                 i += 1  # Skip the next element as it's already processed
#             elif i < len(elem) - 2 and not ('***' in elem[i - 1]):
#                 if elem[i - 1].strip().replace('*', '').replace('\n', '').replace(' ', '') != '' and \
#                    elem[i + 2].strip().replace('*', '').replace('\n', '').replace(' ', '') != '':  # Check if convertible
#                     new_elem.append(str(0.5 * (float(elem[i - 1]) + float(elem[i + 2]))))
#                 i += 2  # Skip the next two elements as they're already processed
#             else:
#                 i += 1  # Move to the next element without adding anything to new_elem
#         else:
#             new_elem.append(elem[i])
#             i += 1
    
#     deren_production_list[elem_index] = new_elem
    
#     print(sigma_values[elem_index])
#     print(len(elem), '\n')
#     print(new_elem, '\n')
#     with open('/home/user/Documents/GitHub/Thermodynamic_Integration/main_simulation_data/der_energies_cleaned_' + str(s), 'w') as file:
#         file.writelines(new_elem)



        
