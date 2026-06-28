# GridEdge Energy — Network Migration Project

A production-pattern network automation project simulating an SDH/PDH to MPLS-TP migration at a fictional electricity utility. Built to demonstrate a complete, end-to-end automation pipeline using Python, Netmiko, Ansible, and Terraform.

## What This Project Does

1. **Pre-migration audit** — connects to every device in the inventory, captures full device state, saves timestamped audit files
2. **NMS infrastructure** — provisions a monitoring server on AWS using Terraform
3. **Config migration** — pushes MPLS-TP config to each device using Ansible and Jinja2 templates
4. **CI/CD pipeline** — GitHub Actions validates and runs the pipeline automatically on every push

## Scaling to Production

This project is designed to scale to any fleet size without code changes:

| To do this | Change this |
|---|---|
| Add a device | Add one row to `inventory/devices.csv` |
| Add a device-specific config | Add one file to `ansible/host_vars/` |
| Add an audit command | Add one line to `AUDIT_COMMANDS` in `netmiko/pre_migration_audit.py` |
| Add a new site | Add a new group to `ansible/hosts.ini` |

No script, playbook, or template changes required.

---

## Project Structure
gridedge-migration/

├── inventory/

│   ├── devices.csv          # Device inventory — one row per device

│   └── README.md            # Inventory column reference

├── audit/                   # Timestamped audit output files

├── netmiko/

│   └── pre_migration_audit.py   # Pre-migration state capture

├── ansible/

│   ├── hosts.ini            # Ansible inventory

│   ├── host_vars/           # Per-device variables

│   │   └── GRIDEDGE-CORE-01.yml

│   ├── templates/

│   │   └── mpls_tp_migration.j2  # Jinja2 config template

│   ├── migration_push.yml   # Migration playbook

│   └── rollback.yml         # Rollback playbook

└── terraform/

├── main.tf              # NMS server infrastructure

├── variables.tf

└── outputs.tf

---

## Tool Stack

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.12 | Scripting and automation |
| Netmiko | 4.7.0 | SSH device automation |
| Ansible | 14.0.0 | Config management |
| Terraform | 1.15.7 | AWS infrastructure |
| Cisco IOS-XE | 17.15.4c | Target platform |
| AWS | ap-southeast-2 | NMS server hosting |

---

## CI/CD Pipeline

GitHub Actions runs automatically on every push to `main` that touches `gridedge-migration/`:
Push to main

│

▼

┌─────────────┐

│  Validate   │  Ansible syntax check + inventory validation

└──────┬──────┘

│

▼

┌─────────────┐

│    Audit    │  Pre-migration audit against live devices

└──────┬──────┘

│

▼

┌─────────────┐

│  Artifacts  │  Audit files uploaded and retained 30 days

└─────────────┘

Credentials are stored as GitHub Actions secrets — never in code.

---

## Running Locally

**Prerequisites:**
```bash
pip install netmiko ansible
brew install terraform
```

**Pre-migration audit:**
```bash
cd gridedge-migration
DEVICE_PASSWORD=your_password python3 netmiko/pre_migration_audit.py
```

**Migration playbook:**
```bash
cd gridedge-migration/ansible
ansible-playbook -i hosts.ini migration_push.yml
```

**Rollback:**
```bash
ansible-playbook -i hosts.ini rollback.yml
```

**NMS server (Terraform):**
```bash
cd gridedge-migration/terraform
terraform init
terraform apply
terraform destroy  # always destroy after lab use
```

---

## Lab Environment

Tested against Cisco DevNet Cat8kv AlwaysOn Sandbox — free, no reservation required.
Hostname : devnetsandboxiosxec8k.cisco.com

Platform : Cisco Catalyst 8000V (IOS-XE 17.15.4c)

Access   : developer.cisco.com/sandbox

For production use — replace sandbox credentials in `inventory/devices.csv` with real device details and update GitHub Actions secrets accordingly.

---

## Background

Built as part of a network automation learning portfolio by a senior network engineer (CCNP, CCNA, AWS) with 13+ years of infrastructure experience, specialising in Cisco routing/switching, MPLS, SD-WAN, and enterprise network migrations.