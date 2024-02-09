# import os

# os.system("sudo /home/user/Desktop/Molecular_simulation/Project/CaseStudy_1/Run/run")

import subprocess
import numpy as np

# working_directory - where you have run file
working_directory = '/home/user/Documents/GitHub/Thermodynamic_Integration/CaseStudy_1/Run'
# the path of file 'run' 
param_path = "/home/user/Documents/GitHub/Thermodynamic_Integration/CaseStudy_1/Run/lj.model"
# python runner path for thermodynamic integration
run_vary_lambda_path = '/home/user/Documents/GitHub/Thermodynamic_Integration/CaseStudy_1/Run/run_vary_lambda.py'
# parser extracts data relevant for therm. integration from 'out' file
parser_path = '/home/user/Documents/GitHub/Thermodynamic_Integration/CaseStudy_1/Run/parse_out.py'
# total energy derivatives output file path
der_energies_path = '/home/user/Documents/GitHub/Thermodynamic_Integration/total_der_energies'
# Fortran output file path
out_path = '/home/user/Documents/GitHub/Thermodynamic_Integration/CaseStudy_1/Run/out'
#
output_path = '/home/user/Documents/GitHub/Thermodynamic_Integration/main_simulation_data/'

#--------------------------------------------------------

def change_sigma(file_path, sigma: str or float):
    with open(out_path, 'w'):
        pass                 # this clears Fortran 'out'
                             # otherwise new data will be appended to old
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    lines[3] = f'1.  {sigma}   1.    5.0  \n'

    with open(file_path, 'w') as file:
        file.writelines(lines)

step = 0.25
sigma_values = np.arange(0.25, 2.5 + step , step)
for i in sigma_values:
    change_sigma(param_path, i)
    subprocess.run(["python", run_vary_lambda_path], cwd=working_directory)
    subprocess.run(["python", parser_path], cwd=working_directory)

    with open(der_energies_path, 'r') as file:
        lines = file.readlines()
        total_energies = lines
    
    with open(output_path + 'der_energies_' + str(i), 'w') as file:
        file.writelines(total_energies)
    
    if i == sigma_values[-2]:
        continue
    
    print(f'finished calculation for sigma = {i}')


