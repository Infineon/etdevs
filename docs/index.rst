etdevs Documentation
====================

etdevs is a small Python package and CLI for embedded test device management.
It covers three core tasks:

- find devices by serial/USB identity
- load known devices from YAML
- power-cycle switchable USB ports through ``uhubctl``

.. warning::

   This is version 0.1.0 (Beta). The API and documentation may evolve.

Quick Start
-----------

.. code-block:: bash

   pip install .
   etdevs-query address

Project Structure
-----------------

.. code-block:: text

   etdevs/
   ├── src/etdevs/
   │   ├── devs.py          # Main data models and device discovery helpers
   │   ├── devs_query.py    # CLI entry point for etdevs-query
   │   └── uhubctl.py       # Wrapper around the uhubctl system tool
   ├── scripts/
   │   └── install_uhubctl.sh
   ├── tests/
   │   ├── devs.yml         # Example device list used by tests
   │   └── test_*.py
   └── docs/

.. toctree::
   :maxdepth: 1
   :caption: Overview

   motivation
   requirements
   installation

.. toctree::
   :maxdepth: 1
   :caption: Usage

   cli-etdevs-query
   python-library

.. toctree::
   :maxdepth: 1
   :caption: Reference

   device-yaml
   enabling-switches
