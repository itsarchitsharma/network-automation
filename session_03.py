import csv
import os

os.makedirs("configs", exist_ok=True)

with open("inventory.csv") as f:
    reader = csv.DictReader(f)
    for router in reader:
        config = f"""hostname {router['hostname']}
!
interface Loopback0
 ip address {router['loopback_ip']} {router['loopback_mask']}
!
router bgp {router['bgp_as']}
 bgp router-id {router['loopback_ip']}
!
"""
        filename = f"configs/{router['hostname']}.txt"
        with open(filename, "w") as config_file:
            config_file.write(config)
        print(f"Written: {filename}")