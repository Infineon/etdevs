Python Library Usage
====================

The Python API is centered on three classes:

- ``Device``: high-level object loaded from YAML
- ``DevAccessSerial``: serial device discovery and address lookup
- ``DevSwitch``: USB power control through ``uhubctl``

Quick Start
-----------

.. code-block:: python

   from etdevs.devs import Device, DevAccessSerial, DevSwitch

   # Scan serial devices
   devices = DevAccessSerial.scan()
   for dev in devices:
       print(dev.address, dev.serial_number)

   # Load from YAML
   devices = Device.load_device_list_from_yml("devices.yml")

   # Control USB power
   sw = DevSwitch.create_from_uid("1106035A012D2400")
   if sw:
       sw.on()
       print(sw.status())

DevAccessSerial
---------------

Most useful calls:

.. code-block:: python

   DevAccessSerial.scan(attr_name=None, attr_value=None)
   DevAccessSerial.create_from_uid(uid: str)
   .get_address() -> str
   .get_serial_number() -> str

Example:

.. code-block:: python

   from etdevs.devs import DevAccessSerial

   devices = DevAccessSerial.scan()
   for dev in devices:
       print(f"{dev.address}: {dev.serial_number}")

DevSwitch
---------

Requires ``uhubctl``. Most useful calls:

.. code-block:: python

   DevSwitch.scan()
   DevSwitch.create_from_uid(uid: str)
   DevSwitch.reset_all()
   .on() -> None
   .off() -> None
   .reset() -> None
   .status() -> str

Example:

.. code-block:: python

   from etdevs.devs import DevSwitch

   sw = DevSwitch.create_from_uid("1106035A012D2400")
   if sw:
       sw.reset()
       print(sw.status())

Device
------

Use ``Device`` when you want named devices from YAML:

.. code-block:: python

   Device.load_device_list_from_yml(yml_file: str)

Example:

.. code-block:: python

   from etdevs.devs import Device

   devices = Device.load_device_list_from_yml("tests/devs.yml")
   for dev in devices:
       print(dev.name)
       if dev.access:
           print(dev.access.address)
       if dev.switch:
           print(dev.switch.status())
