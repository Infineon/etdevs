Device YAML Format
==================

Device files are simple YAML lists.

Schema
------

Each item supports:

.. code-block:: yaml

    - name: <string>
       uid: <string>
       features:
       - <string>
       - <string>

``name`` and ``uid`` are the main fields. ``features`` is optional and can be
used for your own filtering or grouping.

Example
-------

.. code-block:: yaml

   - name: CY8CKIT-062S2-AI
     uid: 1106035A012D2400
     features:
          - psoc6

   - name: XMC1100_BOOT_KIT
     uid: "000591128721"
       features:
          - xmc1100

Usage
-----

Load devices in your Python code:

.. code-block:: python

   from etdevs.devs import Device

   devices = Device.load_device_list_from_yml("path/to/devices.yml")
      print(devices[0].name)

From the CLI:

.. code-block:: bash

   etdevs-query name -y devices.yml
