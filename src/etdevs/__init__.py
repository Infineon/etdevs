"""
Embedded Test Devices (etdevs) - Python package for embedded test device management.

This package provides utilities for managing embedded test devices for on-target 
functional testing, including USB hub control and serial device management.
"""

__version__ = "0.1.0"
__author__ = "Infineon Technologies"
__email__ = "opensource@infineon.com"

# Import main classes for easier access
from .devs import Device, DevAccessSerial, DevSwitch
from .uhubctl import Uhubctl

__all__ = [
    "Device",
    "DevAccessSerial", 
    "DevSwitch",
    "Uhubctl",
    "__version__",
    "__author__",
    "__email__",
]
