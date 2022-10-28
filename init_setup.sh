echo [$(date)]: "START"
echo [$(date)]: "Creating conda environment with python 3.8"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "Activating conda environment" 
source activate ./env
echo [$(date)]: "Installing dev reqirements" 
pip install -r requirements_dev.txt 
echo [$(date)]: "END"
