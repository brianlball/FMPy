import os
import numpy as np
import matplotlib.pyplot as pl

os.chdir('run_ssp/new_in_fmu')
os.getcwd()
import pyfmi
from pyfmi import load_fmu
fmu_path = 'in.fmu'
start_time=0
final_time=86400
step_size=60
idf_steps_per_hour=60
model = load_fmu(fmu=fmu_path)
seconds_in_hour = 60*60
ncp = int(final_time/(seconds_in_hour/idf_steps_per_hour))
opts = model.simulate_options()
opts['ncp'] = ncp
step_size = seconds_in_hour // idf_steps_per_hour

t = np.linspace(0.0,final_time,ncp,dtype=int)
ZoneTempSetpoint = np.empty(len(t)); ZoneTempSetpoint.fill(40.0)
ElectricDesignLevel = np.empty(len(t)); ElectricDesignLevel.fill(1000.0)
Q = np.empty(len(t)); Q.fill(0.0)

input_values = np.transpose(np.vstack((t, ElectricDesignLevel, Q, ZoneTempSetpoint)))
input_object = (['ElectricDesignLevel', 'Q', 'ZoneTempSetpoint'],input_values)

model.set(['ElectricDesignLevel', 'Q', 'ZoneTempSetpoint'],[1000, 0, 40])

result = model.simulate(start_time=0, final_time=final_time, input = input_object, options=opts)

print(result.keys())
fig1 = pl.figure()
ax1 = fig1.add_subplot()
ax1.plot(result['Q'], 'b--')
ax1.plot(result['ElectricDesignLevel'], 'r')
ax1.plot(result['ZoneTempSetpoint'], 'g')