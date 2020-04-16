#"python3 #{lib_dir}/mo/run_ssp3.py #{ssp_file} #{run_dir} #{fmu_start_time} #{fmu_stop_time} #{fmu_time_step}"
import os
import sys
import shutil

print("sys.argv:", sys.argv)
print("os.getcwd():", os.getcwd())
print("os.environ:", os.environ)
import matplotlib
import matplotlib.pyplot as pl
matplotlib.use('Agg')

from fmpy.ssp.simulation import simulate_ssp
from fmpy.util import plot_result

from pathlib import Path

#model_name = "HelloWorld"
#mo_file = "/var/oscli/clones/openstudio-workflow/lib/openstudio/workflow/jobs/HelloWorld.mo"
ssp_filename = Path(sys.argv[1])
#run_dir = sys.argv[2] + '/FMU'
run_dir = Path(sys.argv[2]) / "FMU"
fmu_start_time = int(sys.argv[3])
fmu_stop_time = int(sys.argv[4])
fmu_time_step = int(sys.argv[5])
#make run_dir
#shutil.rmtree(run_dir, ignore_errors=True)

Path(run_dir).mkdir(parents=True, exist_ok=True)
#copy ssp to run_dir
ssp_file = shutil.copy(ssp_filename, run_dir)
os.chdir(run_dir)
print("os.getcwd():", os.getcwd())
print("Simulating %s..." % ssp_filename)
result = simulate_ssp(ssp_file, start_time=fmu_start_time, stop_time=fmu_stop_time, step_size=fmu_time_step, run_dir=run_dir)

show_plot=True

if show_plot:
    dir, _ = os.path.split(run_dir)
    save_name = dir + '/ssp.png'
    save_name2 = dir + '/temp.png'
    print("Plotting results in directory:",save_name)
    print("run_dir:",run_dir)
    #plot_result(result, names=['space.electric_demand', 'space.district_heating', 'space.district_cooling'], window_title=ssp_filename, filename=save_name)
    #plot_result(result, names=['space.zone_temp'], window_title=ssp_filename, filename=dir + '/temp.png')
    fig1 = pl.figure()
    ax1 = fig1.add_subplot()
    ax1.plot(result['electric.y'], 'b--')
    ax1.plot(result['space.district_heating'], 'r')
    ax1.plot(result['space.district_cooling'], 'g')
    pl.savefig(save_name)

print('result: ', result)
print('Done.')
