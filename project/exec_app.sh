#!/bin/bash

if [ -z "$1" ] || [ "$1" = "help" ] || ! [[ ("$1" == "vulnerable") || ("$1" == "secure") || ("$1" == "enterprise") ]]
  then
    echo "Help:"
    echo "  ./exec_app.sh help         -> displays this message"
    echo "  ./exec_app.sh vulnerable   -> runs vulnerable app"
    echo "  ./exec_app.sh secure       -> runs secure app"
    echo "  ./exec_app.sh enterprise   -> runs enterprise app"
fi

if [ "$1" = "vulnerable" ]
  then
      cd ./vulnerable
      FLASK_APP=main.py FLASK_DEBUG=1 TEMPLATES_AUTO_RELOAD=1 flask run
fi

if [ "$1" = "secure" ]
  then
      cd ./secure
      echo "Not implemented yet!"
fi

if [ "$1" = "enterprise" ]
  then
      cd ./enterprise
      echo "Not implemented yet!"
fi
