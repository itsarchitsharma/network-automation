# Network Automation Portfolio

A structured learning portfolio documenting my progression from Python fundamentals to production-grade network automation tools. Built as a practising senior network engineer (CCNP, CCNA, AWS) adding automation skills to 13+ years of infrastructure expertise.

## What This Repo Demonstrates

- Python scripting for network engineering tasks
- SSH-based device automation using Netmiko
- Configuration management at scale using Ansible
- Cloud infrastructure as code using Terraform
- Real Cisco IOS-XE device interaction throughout (Cisco DevNet Sandbox)
- Git-based version control from day one

---

## Stack

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.12 | Scripting and automation |
| Netmiko | 4.7.0 | SSH device automation |
| Ansible | 14.0.0 | Config management |
| Terraform | 1.15.7 | Infrastructure as code |
| Cisco IOS-XE | 17.15.4c | Target platform (Cat8000V) |
| AWS | ap-southeast-2 | Cloud networking target |

---

## Repository Structure

---

## Python Foundations (Sessions 1–4)

Covers the Python constructs directly relevant to network automation — no fluff, no web frameworks, no data science.

**Session 1** — Variables, strings, f-strings. Generates Cisco config blocks programmatically.

**Session 2** — Lists, dictionaries, loops. Replaces repetitive code with a single loop across a device inventory.

**Session 3** — CSV file I/O. Reads a device inventory from a CSV file and writes per-device config files to disk.

**Session 4** — Functions. Refactors the config generator into `generate_config()` and `write_config()` — separation of concerns.

---

## Netmiko — SSH Device Automation (Sessions 5–8)

Live SSH automation against a Cisco Catalyst 8000V running IOS-XE 17.15.4c via Cisco DevNet Sandbox.

**Session 5** — First live device connection. `ConnectHandler`, `send_command()`, show command capture.

**Session 6** — Multi-device audit tool. Loops through CSV inventory, SSHs into each device, saves output to per-device files.

**Session 7** — Config push with `send_config_set()`. Before/after state capture and rollback pattern.

**Session 8** — Production-grade error handling. `try/except` blocks catch timeouts and auth failures gracefully. Script keeps running against remaining inventory when one device fails.

---

## Ansible for Networks (Sessions 9–13)

Agentless configuration management targeting Cisco IOS-XE via `cisco.ios` collection.

**Session 9** — Inventory, ping module, first playbook, `ios_command`.

**Session 10** — `ios_config`, idempotency demonstrated, config push and rollback.

**Session 11** — Jinja2 templates and vars files. Config structure separated from data.

**Session 12** — Ansible roles. Reusable, self-contained automation packages with variable overrides.

**Session 13** — Migration-style playbook. `host_vars` per device, pre/post state capture, audit files written to disk.

---

## Terraform — AWS Infrastructure as Code (Sessions 14–17)

Modular AWS network infrastructure targeting ap-southeast-2.

**Session 14** — HCL basics, AWS provider, VPC and subnet. Plan/apply/destroy workflow.

**Session 15** — Variables, outputs, tfvars. Environment-driven deployments from a single codebase.

**Session 16** — Modules. Reusable VPC and subnet modules called with variable overrides.

**Session 17** — Complete AWS network baseline. VPC, public/private subnets, Internet Gateway, route tables, security group — all modular.

---

## Background

Senior Network & Infrastructure Engineer with 13+ years experience. Certifications: CCNP, CCNA, AWS. Core expertise: Cisco routing/switching, MPLS, SD-WAN, SASE, OT/SCADA, enterprise network migrations. Currently managing an SDH/PDH to MPLS-TP migration programme at an electricity utility.

This portfolio documents the automation layer being added on top of that infrastructure expertise.

---

## Contact

GitHub:[itsarchitsharma](https://github.com/itsarchitsharma)