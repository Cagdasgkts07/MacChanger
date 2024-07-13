# MAC Address Changer

This Python script allows you to change the MAC address of a network interface on your machine. It provides options to specify a new MAC address or generate a random one.

## Features

- Change MAC address for a specified network interface.
- Validate the provided MAC address format.
- Option to generate a random MAC address.

## Usage

### Command Line Options

- `-i`, `--interface`: Interface to change the MAC address (required).
- `-m`, `--mac`: New MAC address (optional if `--random` is used).
- `-r`, `--random`: Generate a random MAC address.

### Examples

1. Change MAC address to a specific address:
   ```sh
   python mac_changer.py -i eth0 -m 00:11:22:33:44:55

2. Generate a random MAC address:
   ```sh
   python mac_changer.py -i eth0 -r
   

