routers = [
    {
        "hostname": "RTR-EDGE-01",
        "loopback_ip": "10.255.0.1",
        "loopback_mask": "255.255.255.255",
        "bgp_as": "65001"
    },
    {
        "hostname": "RTR-EDGE-02",
        "loopback_ip": "10.255.0.2",
        "loopback_mask": "255.255.255.255",
        "bgp_as": "65001"
    },
    {
        "hostname": "RTR-EDGE-03",
        "loopback_ip": "10.255.0.3",
        "loopback_mask": "255.255.255.255",
        "bgp_as": "65001"
    },
    {
          "hostname": "RTR-EDGE-04",
        "loopback_ip": "10.255.0.4",
        "loopback_mask": "255.255.255.255",
        "bgp_as": "65001"
    }
]

for router in routers:
    print(f"hostname {router['hostname']}")
    print(f"!")
    print(f"interface Loopback0")
    print(f" ip address {router['loopback_ip']} {router['loopback_mask']}")
    print(f"!")
    print(f"router bgp {router['bgp_as']}")
    print(f" bgp router-id {router['loopback_ip']}")
    print(f"!")
    print()