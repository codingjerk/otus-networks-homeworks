#!/usr/bin/env python


for name, ipv4, gw in [
    ("VPC30", "193.1.5.200", "193.1.5.100"),
    ("VPC31", "193.1.5.210", "193.1.5.101"),
    ("VPC1",  "193.1.6.200", "193.1.6.102"),
    ("VPC7",  "193.1.6.210", "193.1.6.112"),
    ("VPC",   "193.1.7.200", "193.1.7.112"),
    ("VPC8",  "193.1.7.210", "193.1.7.102"),
]:
    print(f"# {name}")
    print(f"""\
<details>
  <summary>{name}</summary>

  ```
  ip {ipv4} {gw} 24
  ip auto
  ```
</details>
""")
