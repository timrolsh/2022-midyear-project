#define parameters
INTERPRETERNAME="python3"
VENV_NAME="venv"

#create a virtual environment in the directory to run our program if one does not already exist on the computer
if [ ! -d "${VENV_NAME}" ]; then
    ${INTERPRETERNAME} -m venv ${VENV_NAME}
    #activate virtual envriornment
    source ${VENV_NAME}/Scrips/activate
    #install pygame (from requirements.txt) into the virtual enviornment
    ${INTERPRETERNAME} -m pip install -r requirements.txt
fi

# run game launcher
${INTERPRETERNAME} Game.py
