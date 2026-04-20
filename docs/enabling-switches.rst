Enabling Switchable USB Devices
===============================

If your hub supports per-port power switching, etdevs can use ``uhubctl`` to
turn ports on, off, or cycle them. If you are using a different infrastructure, 
you can also create the appropriate wrapper program to control the hub ports.

Requirements
------------

1. ``uhubctl`` installed and in ``PATH``
2. a supported hub
3. suitable permissions on Linux

Installation
~~~~~~~~~~~~

.. tabs::

   .. tab:: Debian/Ubuntu

      .. code-block:: bash

         sudo apt update
         sudo apt install uhubctl

   .. tab:: Fedora/RHEL

      .. code-block:: bash

         sudo dnf install uhubctl

   .. tab:: macOS

      .. code-block:: bash

         brew install uhubctl

   .. tab:: Build from Source

      .. code-block:: bash

         git clone https://github.com/mvp/uhubctl.git
         cd uhubctl
         make
         sudo make install

Verify
~~~~~~

.. code-block:: bash

   uhubctl

If no hubs are found, you will usually see:

.. code-block:: text

   No compatible devices detected!

Examples
--------

Direct ``uhubctl`` usage:

.. code-block:: bash

   uhubctl -l 1-1 -p 2 -a off
   uhubctl -l 1-1 -p 2 -a on
   uhubctl -l 1-1 -p 2 -a cycle
   uhubctl -s 1106035A012D2400

Python usage through ``DevSwitch``:

.. code-block:: python

   from etdevs.devs import DevSwitch

   sw = DevSwitch.create_from_uid("1106035A012D2400")
   if sw:
       sw.reset()
       print(sw.status())

Troubleshooting
---------------

- ``command not found``: install ``uhubctl`` first
- ``permission denied``: run with ``sudo`` or configure udev rules
- device not found: verify the serial number with ``etdevs-query serial_number``
