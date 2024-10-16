#!/usr/bin/env bash

python -m venv .venv
. .venv/bin/activate
pip install pybuilder
pip install twine

pyb publish
if [ -z "$1" ]
then
    echo "No username supplied"
    exit 0
fi
if [ -z "$2" ]
then
    echo "No password supplied"
    exit 0
fi
mv target/dist/api*/dist/api*.whl target/dist/api*/dist/ycappuccino_api*.whl
twine upload  target/dist/api*/dist/api*.whl --repository-url https://nexus.ycappuccino.fr/ -u$1 -p$2