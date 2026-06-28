#!/usr/bin/env python3
"""
GridEdge Energy — Pre-Migration Audit
======================================
Captures full device state before migration begins.

SCALING TO PRODUCTION:
- Add rows to inventory/devices.csv to onboard additional devices
- This script connects to every device in the CSV automatically
- No code changes required — only the CSV changes

TESTED AGAINST:
- Cisco DevNet Cat8kv AlwaysOn Sandbox (IOS-XE 17.15.4c)
- Compatible with any Netmiko-supported Cisco IOS/IOS-XE device

ADDING NEW AUDIT COMMANDS:
- Add commands to AUDIT_COMMANDS list below
- All commands run against every device in the inventory
"""

import csv
import os
from datetime import datetime
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

# ── AUDIT COMMANDS ──────────────────────────────────────────
# Add or remove commands here to customise the audit scope.
# All commands run against every device in the inventory.
AUDIT_COMMANDS = [
    "show version",
    "show ip interface brief",
    "show ip route",
    "show processes cpu sorted",
    "show memory statistics",
    "show logging last 20",
]

INVENTORY_FILE = "inventory/devices.csv"
AUDIT_DIR = "audit"
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

results = {"success": [], "failed": []}


def run_audit(device, connection):
    """Run all audit commands against a connected device."""
    output_lines = []
    output_lines.append(f"GridEdge Energy — Pre-Migration Audit")
    output_lines.append(f"Device: {device['hostname']}")
    output_lines.append(f"Role: {device['role']}")
    output_lines.append(f"Site: {device['site']}")
    output_lines.append(f"Legacy Platform: {device['legacy_platform']}")
    output_lines.append(f"New Platform: {device['new_platform']}")
    output_lines.append(f"Timestamp: {TIMESTAMP}")
    output_lines.append(f"{'='*60}\n")

    for command in AUDIT_COMMANDS:
        output_lines.append(f"{'='*60}")
        output_lines.append(f"Command: {command}")
        output_lines.append(f"{'='*60}")
        output = connection.send_command(command)
        output_lines.append(output)
        output_lines.append("")

    return "\n".join(output_lines)


def save_audit(hostname, content):
    """Save audit output to a timestamped file."""
    os.makedirs(AUDIT_DIR, exist_ok=True)
    filename = f"{AUDIT_DIR}/{hostname}_pre_migration_{TIMESTAMP}.txt"
    with open(filename, "w") as f:
        f.write(content)
    return filename


def main():
    print(f"\nGridEdge Energy — Pre-Migration Audit")
    print(f"Timestamp: {TIMESTAMP}")
    print(f"{'='*60}\n")

    with open(INVENTORY_FILE) as f:
        reader = csv.DictReader(f)
        devices = list(reader)

    print(f"Devices in inventory: {len(devices)}")
    print(f"Adding devices to inventory/devices.csv scales this automatically\n")

    for device in devices:
        print(f"Connecting to {device['hostname']} ({device['host']})...")

        try:
            # Password resolved from environment variable if set
            # Set DEVICE_PASSWORD env var in GitHub Actions secrets
            # For local runs password is read directly from CSV
            password = os.environ.get("DEVICE_PASSWORD") or device["password"]

            connection = ConnectHandler(
                device_type=device["device_type"],
                host=device["host"],
                port=int(device["port"]),
                username=device["username"],
                password=password,
            )

            print(f"  Connected — running audit commands...")
            audit_content = run_audit(device, connection)
            connection.disconnect()

            filename = save_audit(device["hostname"], audit_content)
            print(f"  Audit saved: {filename}")
            results["success"].append(device["hostname"])

        except NetmikoTimeoutException:
            print(f"  FAILED: {device['hostname']} — unreachable")
            results["failed"].append({
                "hostname": device["hostname"],
                "reason": "Device unreachable"
            })

        except NetmikoAuthenticationException:
            print(f"  FAILED: {device['hostname']} — authentication failed")
            results["failed"].append({
                "hostname": device["hostname"],
                "reason": "Authentication failed"
            })

        except Exception as e:
            print(f"  FAILED: {device['hostname']} — {str(e)}")
            results["failed"].append({
                "hostname": device["hostname"],
                "reason": str(e)
            })

    print(f"\n{'='*60}")
    print(f"AUDIT SUMMARY")
    print(f"{'='*60}")
    print(f"Successful: {len(results['success'])}")
    for h in results["success"]:
        print(f"  ✓ {h}")
    print(f"Failed: {len(results['failed'])}")
    for item in results["failed"]:
        print(f"  ✗ {item['hostname']} — {item['reason']}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()