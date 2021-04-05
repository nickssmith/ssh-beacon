# ssh-beacon

A systemd service and connection script to find a system on a network as a known SSH target

## requirements

nmap and python on client system

## Service

systemd service that listens on port `2222` 

## Connector

script that uses nmap and python to ping all on port `2222` with a passphrase
if the passphrase is what the beacon is looking for, then the beacon will return a true value

## Config

change in python code the passphrase, default is `thisu`

passphrase allows for multiple beacons on the same network, since connector will return address of 1st good beacon reply
