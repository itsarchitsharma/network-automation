hostname = "RTR-EDGE-01"
loopback_ip = "10.255.0.1"
loopback_mask = "255.255.255.255"
bgp_as = "65001"

print(f"hostname {hostname}")
print(f"!")
print(f"interface Loopback0")
print(f" ip address {loopback_ip} {loopback_mask}")
print(f"!")
print(f"router bgp {bgp_as}")
print(f" bgp router-id {loopback_ip}")

hostname = "RTR-EDGE-02"
loopback_ip = "10.255.0.2"
loopback_mask = "255.255.255.255"
bgp_as = "65001"

print(f"hostname {hostname}")
print(f"!")
print(f"interface Loopback0")
print(f" ip address {loopback_ip} {loopback_mask}")
print(f"!")
print(f"router bgp {bgp_as}")
print(f" bgp router-id {loopback_ip}")

hostname = "RTR-EDGE-03"
loopback_ip = "10.255.0.3"
loopback_mask = "255.255.255.255"
bgp_as = "65001"

print(f"hostname {hostname}")
print(f"!")
print(f"interface Loopback0")
print(f" ip address {loopback_ip} {loopback_mask}")
print(f"!")
print(f"router bgp {bgp_as}")
print(f" bgp router-id {loopback_ip}")