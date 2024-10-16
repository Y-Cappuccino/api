#!/usr/bin/env bash

python -m venv .venv
. .venv/bin/activate
pip install pybuilder
pip install twine

pyb publish

twine upload  target/dist/api*/dist/api*.whl