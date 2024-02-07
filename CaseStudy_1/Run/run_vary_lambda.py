# import os

# os.system("sudo /home/user/Desktop/Molecular_simulation/Project/CaseStudy_1/Run/run")

import subprocess
import numpy as np

# working_directory - where you have run file
working_directory = '/home/user/Documents/GitHub/Thermodynamic_Integration/CaseStudy_1/Run'
# the path of file 'run' 
run_path = "/home/user/Documents/GitHub/Thermodynamic_Integration/CaseStudy_1/Run/run"

# Fortran output file path
out_path = '/home/user/Documents/GitHub/Thermodynamic_Integration/CaseStudy_1/Run/out'
# Python output file path
data_path = '/home/user/Documents/GitHub/Thermodynamic_Integration/'

#---------------- Thermodynamic Integration ----------------------------------------

def change_lambda(file_path, lambd: str or float):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    rho = '{rho}'
    lines[13] = f'  200   2.0  ${rho} {lambd}\n'

    with open(file_path, 'w') as file:
        file.writelines(lines)

step = 0.01
for i in np.arange(0.1, 1 + step , step):
    change_lambda(run_path, i)
    subprocess.run(['sudo', run_path], cwd=working_directory)
