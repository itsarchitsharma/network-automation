from netmiko import ConnectHandler

device = {
    "device_type": "cisco_xe",
    "host": "devnetsandboxiosxec8k.cisco.com",
    "username": "architsharma08",
    "password": "6G-5W7Z_hsna",
}

config_commands = [
    "interface Loopback200",
    "description NETMIKO-TEST",
    "ip address 10.200.0.1 255.255.255.255",
]

rollback_commands = [
    "no interface Loopback200",
]

print("Connecting...")
connection = ConnectHandler(**device)
print("Connected\n")

# Step 1 - capture state before change
print("=== BEFORE ===")
before = connection.send_command("show ip interface brief")
print(before)

# Step 2 - push the config
print("=== PUSHING CONFIG ===")
output = connection.send_config_set(config_commands)
print(output)

# Step 3 - verify the change landed
print("=== AFTER ===")
after = connection.send_command("show ip interface brief")
print(after)

# Step 4 - rollback
print("=== ROLLING BACK ===")
rollback = connection.send_config_set(rollback_commands)
print(rollback)

# Step 5 - verify rollback
print("=== AFTER ROLLBACK ===")
final = connection.send_command("show ip interface brief")
print(final)

connection.disconnect()
print("Disconnected")