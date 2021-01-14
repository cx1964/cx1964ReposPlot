rem filename: 100_install_libs_cx1964ReposPlot.cmd
rem functie:  install libraries tbv plot in windows

python3 -m venv env_python3_plot

rem activate python env
.\activate_python_env.cmd

rem upgrade pip
python -m pip install -U pip

rem importeer alle benodigde libraries
rem pip install ..

rem specifiek mbt matplotlib
pip uninstall matplotlib
python3 -m pip install matplotlib

rem toon geinstalleerde python libraries
pip list