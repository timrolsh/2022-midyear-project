# define parameters
$INTERPRETERNAME = "python"
$VENV_NAME = "venv"

#create a virtual environment in the directory to run our program if one does not already exist on the computer
if (!(Test-Path -Path ${VENV_NAME})) {
    Invoke-Expression "${INTERPRETERNAME} -m venv ${VENV_NAME}"
    # activate virtual envriornment
    Invoke-Expression ".\${VENV_NAME}\Scripts\activate.ps1"
    # install pygame (from requirements.txt) into the virtual enviornment
    Invoke-Expression "${INTERPRETERNAME} -m pip install -r requirements.txt"
}

# activate virtual envriornment
Invoke-Expression ".\${VENV_NAME}\Scripts\activate.ps1"
# run game launcher
Invoke-Expression "${INTERPRETERNAME} Game.py"