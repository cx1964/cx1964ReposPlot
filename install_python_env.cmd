rem File: install_python_env.cmd
rem Functie: installatie tbv opzetten van een python3 omgeving
rem opmerking: Uitgangspunt python3 software is al geinstalleerd onder Windows10

rem maak virtuele python environment voor python libraries
python3 -m venv env_python3_plot

.\env_python3_plot\Scripts\activate.bat

