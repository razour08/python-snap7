Frequently Asked Questions
==========================


How do I find my PLC's IP address?
-----------------------------------

Your PLC's IP address is configured in the PLC project (e.g., in TIA Portal or
STEP 7). You can also find it by:

1. Checking the PLC's display (if it has one)
2. Scanning your network with tools like ``nmap``
3. Checking your project configuration in the engineering software


What are rack and slot numbers?
-------------------------------

- **Rack**: The physical rack where your PLC is mounted (usually ``0``)
- **Slot**: The position of the CPU in the rack (usually ``0`` for S7-1200/1500,
  ``2`` for S7-300/400)

Common configurations:

.. list-table::
   :header-rows: 1

   * - PLC Series
     - Rack
     - Slot
   * - S7-1200
     - 0
     - 0
   * - S7-1500
     - 0
     - 0
   * - S7-300
     - 0
     - 2
   * - S7-400
     - 0
     - 2 or 3


Can I connect to multiple PLCs simultaneously?
-----------------------------------------------

Yes! Create multiple ``Client`` instances:

.. code-block:: python

    import snap7

    client1 = snap7.Client()
    client1.connect("192.168.0.1", 0, 0)

    client2 = snap7.Client()
    client2.connect("192.168.0.2", 0, 0)


Does python-snap7 support S7-1200 and S7-1500?
-------------------------------------------------

Yes, but you need to enable **PUT/GET** communication on the PLC:

1. Open TIA Portal
2. Go to your CPU's properties
3. Navigate to **Protection & Security** → **Connection mechanisms**
4. Check **Permit access with PUT/GET communication**


What data types are supported?
------------------------------

python-snap7 supports reading and writing:

- **Bool** — Single bits
- **Byte/Int/DInt/Real** — Numeric types
- **Word/DWord** — Unsigned integers
- **String** — Character strings
- **Date/Time/DateTime** — Temporal types
- **S5Time/Time** — PLC time formats


Is python-snap7 thread-safe?
-----------------------------

Each ``Client`` instance should be used from a single thread. For multi-threaded
applications, create one ``Client`` per thread or use thread synchronization.


What is the maximum data size I can read/write?
-------------------------------------------------

The maximum data size depends on the PDU size negotiated with the PLC:

- **S7-300**: up to 240 bytes per PDU
- **S7-400/1200**: up to 480 bytes per PDU  
- **S7-1500**: up to 960 bytes per PDU

For larger data, use ``read_multi_vars()`` or split into multiple reads.
