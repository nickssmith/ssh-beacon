# ssh-beacon

A systemd service and connection script to find a system on a network as a known SSH target

Once installed on a client and server system, the command `findsshbeacon` can be used to print the IP address of the beacon.
Example usage:
```
ssh nick@$(findsshbeacon) -XY
```
could be used to find the beacon system on any network configuration.

Some use cases include:
 - laptop target that could have an IP over ethernet or wifi that would change
 - certain networks or configs could not support hostname resolution
 - cannot create a static IP for the target system 

## requirements

python3-venv


## Service

systemd service that listens on port `2222` 

To install and enable the service, run `install.sh` are root/with sudo from the `beacon` directory

## Scanner

To install the command `findsshbeacon` run `install.sh` as root/with sudo from the `scanner` directory

This will
 - create an install for it in `/usr/local/findsshbeacon`
 - create a python3 virtual environment and install requirements
 - move the `findsshbeacon` script to `/usr/bin`

When running `findsshbeacon` it will print out the IP of the beacon it finds. 
This can be used in a script to ssh to that IP


## Config

change in python code the passphrase, default is `thisu`

after change in code, run `install.sh` to update and make changes

passphrase allows for multiple beacons on the same network, since connector will return address of 1st good beacon reply
