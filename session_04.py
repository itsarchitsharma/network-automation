import csv
import os

def generate_config(router):
    config = f"""hostname {router['hostname']}
!
interface Loopback0
 ip address {router['loopback_ip']} {router['loopback_mask']}
!
router bgp {router['bgp_as']}
 bgp router-id {router['loopback_ip']}
!
"""
    return config


def write_config(router, output_dir="configs"):
    os.makedirs(output_dir, exist_ok=True)
    config = generate_config(router)
    filename = f"{output_dir}/{router['hostname']}.txt"
    with open(filename, "w") as f:
        f.write(config)
    print(f"Written: {filename}")


with open("inventory.csv") as f:
    reader = csv.DictReader(f)
    for router in reader:
        write_config(router)