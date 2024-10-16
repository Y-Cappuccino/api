#!/usr/bin/env bash

python -m venv .venv
. .venv/bin/activate
pip install pyb
source .venv/bin/activate
pip install pyb
pyb publish