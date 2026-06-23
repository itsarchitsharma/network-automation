from netmiko import ConnectHandler

device = {
    "device_type": "cisco_xe",
    "host": "devnetsandboxiosxec8k.cisco.com",
    "username": "architsharma08",
    "password": "LEX248tLlTLxyQ--",
}

commands = [
    "show ip interface brief",
    "show version",
    "show ip route",
]

print("Connecting...")
connection = ConnectHandler(**device)
print("Connected successfully\n")

for command in commands:
    print(f"{'='*50}")
    print(f"Command: {command}")
    print(f"{'='*50}")
    output = connection.send_command(command)
    print(output)
    print()

connection.disconnect()
print("Disconnected")