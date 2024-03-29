ips = {
    "R22": {
        "e0/0": ("193.1.1.0", "2001:1::0"),
        "e0/1": ("193.1.1.1", "2001:1::1"),
        "e0/2": ("193.1.1.2", "2001:1::2"),
    },
    "R21": {
        "e0/0": ("193.1.2.0", "2001:2::0"),
        "e0/1": ("193.1.2.1", "2001:2::1"),
        "e0/2": ("193.1.2.2", "2001:2::2"),
    },
    "R23": {
        "e0/0": ("193.1.3.0", "2001:3::0"),
        "e0/1": ("193.1.3.1", "2001:3::1"),
        "e0/2": ("193.1.3.2", "2001:3::2"),
    },
    "R24": {
        "e0/0": ("193.1.3.10", "2001:3::1:0"),
        "e0/1": ("193.1.3.11", "2001:3::1:1"),
        "e0/2": ("193.1.3.12", "2001:3::1:2"),
        "e0/3": ("193.1.3.13", "2001:3::1:3"),
    },
    "R25": {
        "e0/0": ("193.1.3.20", "2001:3::2:0"),
        "e0/1": ("193.1.3.21", "2001:3::2:1"),
        "e0/2": ("193.1.3.22", "2001:3::2:2"),
        "e0/3": ("193.1.3.23", "2001:3::2:3"),
    },
    "R26": {
        "e0/0": ("193.1.3.30", "2001:3::3:0"),
        "e0/1": ("193.1.3.31", "2001:3::3:1"),
        "e0/2": ("193.1.3.32", "2001:3::3:2"),
        "e0/3": ("193.1.3.33", "2001:3::3:3"),
    },
    "R27": {
        "e0/0": ("193.1.4.0", "2001:4::0"),
    },
    "R28": {
        "e0/0": ("193.1.5.0", "2001:5::0"),
        "e0/1": ("193.1.5.1", "2001:5::1"),
        "e0/2": ("193.1.5.2", "2001:5::2"),
    },
    "R12": {
        "e0/0": ("193.1.6.0", "2001:6::0"),
        "e0/1": ("193.1.6.1", "2001:6::1"),
        "e0/2": ("193.1.6.2", "2001:6::2"),
        "e0/3": ("193.1.6.3", "2001:6::3"),
    },
    "R13": {
        "e0/0": ("193.1.6.10", "2001:6::1:0"),
        "e0/1": ("193.1.6.11", "2001:6::1:1"),
        "e0/2": ("193.1.6.12", "2001:6::1:2"),
        "e0/3": ("193.1.6.13", "2001:6::1:3"),
    },
    "R14": {
        "e0/0": ("193.1.6.20", "2001:6::2:0"),
        "e0/1": ("193.1.6.21", "2001:6::2:1"),
        "e0/2": ("193.1.6.22", "2001:6::2:2"),
        "e0/3": ("193.1.6.23", "2001:6::2:3"),
    },
    "R15": {
        "e0/0": ("193.1.6.30", "2001:6::3:0"),
        "e0/1": ("193.1.6.31", "2001:6::3:1"),
        "e0/2": ("193.1.6.32", "2001:6::3:2"),
        "e0/3": ("193.1.6.33", "2001:6::3:3"),
    },
    "R19": {
        "e0/0": ("193.1.6.40", "2001:6::4:0"),
    },
    "R20": {
        "e0/0": ("193.1.6.50", "2001:6::5:0"),
    },
    "R16": {
        "e0/0": ("193.1.7.0", "2001:7::0"),
        "e0/1": ("193.1.7.1", "2001:7::1"),
        "e0/2": ("193.1.7.2", "2001:7::2"),
        "e0/3": ("193.1.7.3", "2001:7::3"),
    },
    "R17": {
        "e0/0": ("193.1.7.10", "2001:7::1:0"),
        "e0/1": ("193.1.7.11", "2001:7::1:1"),
        "e0/2": ("193.1.7.12", "2001:7::1:2"),
    },
    "R18": {
        "e0/0": ("193.1.7.20", "2001:7::2:0"),
        "e0/1": ("193.1.7.21", "2001:7::2:1"),
        "e0/2": ("193.1.7.22", "2001:7::2:2"),
        "e0/3": ("193.1.7.23", "2001:7::2:3"),
    },
    "R32": {
        "e0/0": ("193.1.7.30", "2001:7::3:0"),
    },
}


for sw, is_ in ips.items():
    print(f"\n# {sw}")

    for i, (ipv4, ipv6) in is_.items():
        print(f"interface Ethernet{i[1:]}")
        print(" no shutdown")
        print(f" ip address {ipv4} 255.255.255.0")
        print(f" ipv6 address {ipv6}")
        print(f" ipv6 address FE80::{sw[1:]} link-local")
        print("!")
