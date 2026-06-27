import csv
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

COMMANDS = [
    "show ip interface brief",
    "show ip route",
]

results = {
    "success": [],
    "failed": [],
}

with open("inventory.csv") as f:
    reader = csv.DictReader(f)
    for device in reader:
        print(f"Connecting to {device['hostname']}...")

        try:
            connection = ConnectHandler(
                device_type=device["device_type"],
                host=device["host"],
                port=device["port"],
                username=device["username"],
                password=device["password"],
            )

            output_lines = []
            for command in COMMANDS:
                output_lines.append(f"{'='*50}")
                output_lines.append(f"Command: {command}")
                output_lines.append(f"{'='*50}")
                output_lines.append(connection.send_command(command))
                output_lines.append("")

            connection.disconnect()

            filename = f"audit/{device['hostname']}.txt"
            with open(filename, "w") as audit_file:
                audit_file.write("\n".join(output_lines))

            print(f"Success: {device['hostname']} — saved to {filename}")
            results["success"].append(device["hostname"])

        except NetmikoTimeoutException:
            print(f"FAILED: {device['hostname']} — device unreachable")
            results["failed"].append({
                "hostname": device["hostname"],
                "reason": "Device unreachable"
            })

        except NetmikoAuthenticationException:
            print(f"FAILED: {device['hostname']} — authentication failed")
            results["failed"].append({
                "hostname": device["hostname"],
                "reason": "Authentication failed"
            })

        except Exception as e:
            print(f"FAILED: {device['hostname']} — unexpected error: {str(e)}")
            results["failed"].append({
                "hostname": device["hostname"],
                "reason": str(e)
            })

print(f"\n{'='*50}")
print(f"SUMMARY")
print(f"{'='*50}")
print(f"Successful: {len(results['success'])}")
for hostname in results["success"]:
    print(f"  ✓ {hostname}")

print(f"Failed: {len(results['failed'])}")
for item in results["failed"]:
    print(f"  ✗ {item['hostname']} — {item['reason']}")