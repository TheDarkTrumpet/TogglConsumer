#!/bin/sh

pyenv virtualenv 3.7.4 togglconsumer

source "$HOME/.pyenv/versions/togglconsumer/bin/activate"

pip install -r requirements.txt

echo "Run pyenv activate togglconsumer to run this"
