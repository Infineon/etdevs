Motivation
==========

etdevs exists to keep embedded test setup simple.

Typical use cases:

- discover connected boards by serial number
- query predefined boards from a YAML list
- map a board to a switchable USB port
- cycle power with ``uhubctl`` during test or recovery flows

The project intentionally stays small and script-friendly. The main interfaces
are the ``etdevs-query`` CLI and three Python classes: ``Device``,
``DevAccessSerial``, and ``DevSwitch``.
