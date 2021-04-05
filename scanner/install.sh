#!/bin/bash

# clean install
rm -rf /usr/local/findsshbeacon


# make folder in /usr/local/
mkdir /usr/local/findsshbeacon
mkdir /usr/local/findsshbeacon/venv

# copy the exec into bin so its in path
cp findsshbeacon /usr/local/bin

# create virtual env in the install directory
python3 -m venv /usr/local/findsshbeacon/venv

source /usr/local/findsshbeacon/venv/bin/activate
pip install networkscan ifaddr

# copy files to install directory

cp scanner.py /usr/local/findsshbeacon/scanner.py