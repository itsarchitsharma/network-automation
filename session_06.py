import csv
import os
from netmiko import ConnectHandler

COMMANDS = [
    "show ip interface brief",
    "show ip route",
    "show version",
]

os.makedirs("audit", exist_ok=True)

with open("inventory.csv") as f:
    reader = csv.DictReader(f)
    for device in reader:
        print(f"Connecting to {device['hostname']}...")

        connection = ConnectHandler(
            device_type=device["device_type"],
            host=device["host"],
            port=device["port"],
            username=device["username"],
            password=device["password"],
        )

        print(f"Connected to {device['hostname']}")

        output_lines = []
        for command in COMMANDS:
            output_lines.append(f"{'='*50}")
            output_lines.append(f"Command: {command}")
            output_lines.append(f"{'='*50}")
            output_lines.append(connection.send_command(command))
            output_lines.append("")

        connection.disconnect()
        print(f"Disconnected from {device['hostname']}")

        filename = f"audit/{device['hostname']}.txt"
        with open(filename, "w") as audit_file:
            audit_file.write("\n".join(output_lines))

        print(f"Audit saved: {filename}\n")