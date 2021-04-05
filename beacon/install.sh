#!/bin/bash

# clean install
rm -rf /usr/local/sshbeacon


# make folder in /usr/local/
mkdir /usr/local/sshbeacon

# copy serice.py into place
cp service.py /usr/local/sshbeacon/service.py

# copy unit file into place
cp sshbeacon.service /etc/systemd/system/sshbeacon.service

# start service
systemctl daemon-reload
systemctl start sshbeacon
systemctl enable sshbeacon