import subprocess
import optparse
import re
from random import randint


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="Interface to change")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="New MAC address")
    parse_object.add_option("-r", "--random", action="store_true", dest="random", help="Generate a random MAC address")
    return parse_object.parse_args()


def validate_mac_address(mac):
    mac_regex = re.compile(r'^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$')
    return mac_regex.match(mac)


def generate_random_mac():
    return ":".join(f"{randint(0, 255):02x}" for _ in range(6))


def change_mac_address(interface, mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])


def main():
    (user_input, arguments) = get_user_input()
    interface = user_input.interface
    mac_address = user_input.mac_address
    random_mac = user_input.random

    if not interface:
        print("Interface is required. Use --help for more information.")
        return

    if random_mac:
        mac_address = generate_random_mac()
        print(f"Generated random MAC address: {mac_address}")
    elif not mac_address:
        print("MAC address is required. Use --help for more information.")
        return
    elif not validate_mac_address(mac_address):
        print("Invalid MAC address format. Please use the format XX:XX:XX:XX:XX:XX.")
        return

    print("MacChanger Started!")
    change_mac_address(interface, mac_address)
    print(f"MAC address for {interface} changed to {mac_address}")


if __name__ == "__main__":
    main()
