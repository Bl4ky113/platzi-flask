#!/usr/bin/bash

if ! [ -d "venv" ]; then
    python -m venv venv
fi

source venv/bin/activate

if [ -e "requirements.txt" ]; then
    if ! [ "`cat requirements.txt`" = "`pip3 freeze`" ]; then
        pip3 install -r requirements.txt
    fi
else
    pip3 freeze > requirements.txt
fi

if [ -e "main.py" ]; then
    export FLASK_APP=main.py
else
    echo "No main.py file"
fi

export FLASK_DEBUG=1
export FLASK_ENV=development

read -n 1 -p "Start Flask Server? y/n " start_server

if [ "$start_server" = "y" ]; then
    flask run
fi
