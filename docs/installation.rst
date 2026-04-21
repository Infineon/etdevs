Installation
=============

Install package
---------------

.. code-block:: bash

   pip install etdevs

(Optional) Install ``uhubctl``
------------------------------

Currently, there is native support for using `uhubctl` to control the USB port.
The provided `scripts/install_uhubctl.sh` script should ease the installation of `uhubctl`.
See https://github.com/mvp/uhubctl for further information.

**Note** that this script requires sudo privileges to run, and you need to know the board's VID (Vendor ID) beforehand.

.. code-block:: bash

    ./install_uhubctl.sh <version> <idVendor>


