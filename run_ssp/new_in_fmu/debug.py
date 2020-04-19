import os
import numpy as np
import matplotlib.pyplot as pl
#os.chdir('run_ssp/new_in_fmu')
os.getcwd()
from fmpy import *
from fmpy import read_model_description, extract
model_description  = read_model_description('in.fmu')

start_time = 0
stop_time = 86400
step_size = 60
idf_steps_per_hour = 60
seconds_in_hour = 60*60
ncp = int(stop_time/(seconds_in_hour/idf_steps_per_hour))

#util.change_fmu('in.fmu', start_values={'ElectricDesignLevel': '1000'})
#util.change_fmu('in.fmu', start_values={'ZoneTempSetpoint': '40'})

t = np.linspace(0.0, stop_time, ncp, dtype=int)
ZoneTempSetpoint = np.empty(len(t))
ZoneTempSetpoint.fill(40.0)
ElectricDesignLevel = np.empty(len(t))
ElectricDesignLevel.fill(1000.0)
Q = np.empty(len(t))
Q.fill(0.0)

#dtype = np.dtype([('time', np.int), ('ElectricDesignLevel', np.float64),
#                  ('Q', np.float64), ('ZoneTempSetpoint', np.float64)])

dtype = np.dtype([('ElectricDesignLevel', np.float64),
                  ('Q', np.float64), ('ZoneTempSetpoint', np.float64)])

#input_object = np.array([t, ElectricDesignLevel, Q, ZoneTempSetpoint], dtype=dtype)
#input_values = np.transpose(np.vstack((t, ElectricDesignLevel, Q, ZoneTempSetpoint)))
#input_object = (['time', 'ElectricDesignLevel', 'Q', 'ZoneTempSetpoint'],input_values)
input_object = list(zip(ElectricDesignLevel, Q, ZoneTempSetpoint))
input_object = np.array(input_object, dtype=dtype)

simulate_fmu('./in.fmu', start_time=0, stop_time=86400, step_size=60, output_interval=60, input=input_object)
