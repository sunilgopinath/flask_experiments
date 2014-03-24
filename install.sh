#!/bin/bash
# expects python is installed with OS distribution
 
# single line command for execution
# wget -O - <RAW_URL> | bash
 
# determine environment
if hash apt-get 2>/dev/null; then
    echo "Bootstrapping UBUNTU"
    UBUNTU=true
    # update apt-get and install a C compiler
    sudo apt-get -y update && sudo apt-get -y upgrade
    sudo apt-get -y install gcc
else
    echo "Bootstrapping OSX"
    # on OSX we use brew as the application repo
    ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"
    brew doctor
    OSX=true
fi

# setup pip and virtualenv
if [ ! -f /usr/local/bin/pip ]; then
   sudo easy_install pip
fi
if [! -f /usr/bin/virtualenv ]; then
    sudo apt-get install python-virtualenv
fi

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# ignore the venv, build and .pyc files
touch .gitignore
echo venv/ >> .gitignore
echo build/ >> .gitignore
echo *.pyc >> .gitignore
