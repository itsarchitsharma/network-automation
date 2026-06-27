# Device Inventory

## Format
hostname, host, port, username, password, device_type, role, site, legacy_platform, new_platform

## Design Decision
One row = one device. To onboard a new device add a single row to devices.csv.
No code changes required anywhere — all scripts, playbooks, and templates
scale automatically from this file.

## Columns
| Column | Description |
|---|---|
| hostname | Device name used in reports and output files |
| host | IP address or FQDN |
| port | SSH port (default 22) |
| username | SSH username |
| password | SSH password |
| device_type | Netmiko device type |
| role | core / edge / distribution |
| site | Physical site name |
| legacy_platform | Platform being replaced |
| new_platform | Target platform post-migration |