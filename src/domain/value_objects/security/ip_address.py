# src/domain/value_objects/security/ip_address.py

import ipaddress
from dataclasses import dataclass


@dataclass(frozen=True)
class IPAddress:
    value: str

    def __post_init__(self):
        ipaddress.ip_address(self.value)