#!/usr/bin/env bash

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

echo Run cheat.sh to generate the code needed for a perfect score