Requirements
============

Runtime
-------

- Python ``>=3.9``
- ``pyserial>=3.5``
- ``PyYAML>=6.0``

System
------

- serial devices exposed by the host OS, such as ``/dev/ttyACM*`` or
	``/dev/ttyUSB*`` on Linux
- access permission to those device nodes

(Optional) For power switching
----------------------------

- ``uhubctl`` installed in ``PATH``
- a hub supported by `uhubctl <https://github.com/mvp/uhubctl>`_
- suitable Linux permissions or udev rules
