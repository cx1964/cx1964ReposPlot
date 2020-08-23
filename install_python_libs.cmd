rem activate python env
.\activate_python_env.cmd

rem upgrade pip
python -m pip install --upgrade pip

rem install bednodigde python libraries
pip install pyodbc
pip install pandas

python -m pip install -U pip
python -m pip install -U matplotlib

rem toon geinstalleerde python libraries
pip list