from setuptools import setup
import tarfile
import os
import shutil
import distutils
import platform

# compile Qt UI and resources
try:
    from fmpy.gui import compile_resources
    compile_resources()
except Exception as e:
    print("Failed to compile resources. %s" % e)

# build CVode shared libraries
url = 'https://computing.llnl.gov/projects/sundials/download/cvode-4.1.0.tar.gz'
filename = 'cvode-4.1.0.tar.gz'
checksum = 'fe130b149dff00bdbe5cf04ea40f9209312d6f1e417831ec37238747c5322fff'

from fmpy.util import download_file
download_file(url, checksum)

print("Extracting %s" % filename)
with tarfile.open(filename, 'r:gz') as tar:
    tar.extractall()

print("Building CVode")
status = os.system('cmake -B cvode-4.1.0/build -DEXAMPLES_ENABLE_C=OFF -DBUILD_STATIC_LIBS=OFF EXAMPLES_INSTALL=OFF -DCMAKE_INSTALL_PREFIX=cvode-4.1.0/dist -DCMAKE_USER_MAKE_RULES_OVERRIDE:STRING=../OverrideMSVCFlags.cmake cvode-4.1.0')
status = os.system('cmake -B cvode-4.1.0/build -DEXAMPLES_ENABLE_C=OFF -DBUILD_STATIC_LIBS=OFF EXAMPLES_INSTALL=OFF -DCMAKE_INSTALL_PREFIX=cvode-4.1.0/dist -DCMAKE_USER_MAKE_RULES_OVERRIDE:STRING=../OverrideMSVCFlags.cmake cvode-4.1.0 && cmake --build cvode-4.1.0/build --target install --config Release')

from fmpy import sharedLibraryExtension

library_prefix = '' if platform.system() == 'Windows' else 'lib'

for shared_library in ['sundials_cvode', 'sundials_nvecserial', 'sundials_sunlinsoldense', 'sundials_sunmatrixdense']:
    shutil.copyfile(os.path.join('cvode-4.1.0', 'dist', 'lib', library_prefix + shared_library + sharedLibraryExtension),
                    os.path.join('fmpy', 'sundials', shared_library + sharedLibraryExtension))

long_description = """
FMPy
====

FMPy is a free Python library to simulate `Functional Mock-up Units (FMUs) <http://fmi-standard.org/>`_ that...

- supports FMI 1.0 and 2.0 for Co-Simulation and Model Exchange
- runs on Windows, Linux and macOS
- has a graphical user interface
- compiles C code FMUs and generates CMake projects for debugging 
"""

packages = ['fmpy', 'fmpy.cross_check', 'fmpy.examples', 'fmpy.gui', 'fmpy.gui.generated', 'fmpy.ssp',
            'fmpy.ssp.examples', 'fmpy.sundials']

package_data = {
    'fmpy': ['c-code/*.h',
             'c-code/CMakeLists.txt',
             'schema/fmi1/*.xsd',
             'schema/fmi2/*.xsd',
             'schema/fmi3/*.xsd',
             'sundials/sundials_*.dylib',
             'sundials/sundials_*.so',
             'sundials/sundials_*.dll'],
    'fmpy.gui': ['icons/app_icon.ico'],
    'fmpy.ssp': ['schema/*.xsd'],
}

install_requires = ['lark-parser', 'lxml', 'numpy', 'pathlib', 'pywin32;platform_system=="Windows"']

extras_require = {
    'examples': ['dask[bag]', 'requests'],
    'plot': ['matplotlib'],
    'gui': ['PyQt5', 'pyqtgraph']
}

extras_require['complete'] = sorted(set(sum(extras_require.values(), [])))

setup(name='FMPy',
      version='0.2.13',
      description="Simulate Functional Mock-up Units (FMUs) in Python",
      long_description=long_description,
      author="Torsten Sommer",
      author_email="torsten.sommer@3ds.com",
      url="https://github.com/CATIA-Systems/FMPy",
      license="Standard 3-clause BSD",
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      extras_require=extras_require,
      entry_points={'console_scripts': ['fmpy=fmpy.command_line:main']})

# see https://www.python.org/dev/peps/pep-0425/#python-tag
platform_tag = distutils.util.get_platform().replace('-', '_').replace('.', '_')

# add the platform tag to the wheel
for dirpath, _, filenames in os.walk('dist'):
    for filename in filenames:
        if filename.endswith('-any.whl'):
            shutil.move(os.path.join(dirpath, filename),
                        os.path.join(dirpath, filename).replace('-any.whl', '-' + platform_tag + '.whl'))
