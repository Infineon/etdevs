etdevs-query CLI Tool
=====================

``etdevs-query`` reads either currently connected serial devices or a YAML device list.

Basic Usage
-----------

.. code-block:: bash

   etdevs-query QUERY_ATTRIBUTE [options]

Common query attributes:

- ``address`` – serial port path (e.g., ``/dev/ttyACM0``)
- ``serial_number`` – USB serial number
- ``name`` – human-readable device name (from YAML)
- ``uid`` – unique identifier (from YAML)

Options
-------

.. code-block:: text

   -f, --filter FILTER          Filter results (format: key=value)
   -y, --devs-yml FILE         Load devices from YAML file
   --not-connected             Include disconnected devices (with --devs-yml)
   -h, --help                  Show help

Examples
--------

List serial device paths:

.. code-block:: bash

   etdevs-query address

Query YAML names:

.. code-block:: bash

   etdevs-query name -y tests/devs.yml

Filter by name:

.. code-block:: bash

   etdevs-query uid -y tests/devs.yml -f name=CY8CKIT-062S2-AI

Include disconnected entries from YAML:

.. code-block:: bash

   etdevs-query name --devs-yml tests/devs.yml --not-connected

Filters use ``key=value`` format. Multiple ``-f`` options are combined.
