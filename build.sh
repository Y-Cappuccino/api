#!/usr/bin/env bash

python -m venv .venv
. .venv/bin/activate
pip install pybuilder
pyb publish