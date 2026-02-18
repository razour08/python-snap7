Troubleshooting
===============


snap7 library not found
------------------------

**Error**: ``can't find snap7 shared library``

**Cause**: The snap7 native library is not installed or not in the system path.

**Solution**:

1. Install via pip (recommended)::

      $ pip install python-snap7

2. Or install the native library manually:

   - **Ubuntu**: ``sudo apt install libsnap7-1``
   - **macOS**: ``brew install snap7``
   - **Windows**: Download from SourceForge and place ``snap7.dll`` in system PATH


Connection refused
------------------

**Error**: ``errIsoConnect`` or connection timeout

**Possible Causes**:

1. Wrong IP address, rack, or slot number
2. PLC is not reachable on the network
3. PUT/GET communication not enabled (S7-1200/1500)
4. Firewall blocking port 102

**Solutions**:

1. Verify the PLC IP address: ``ping 192.168.0.1``
2. Check rack/slot (see FAQ)
3. Enable PUT/GET in TIA Portal (see FAQ)
4. Open port 102 in your firewall


PDU size error
--------------

**Error**: ``errCliSizeOverPDU``

**Cause**: Trying to read/write more data than the PDU allows.

**Solution**: Split large reads into smaller chunks:

.. code-block:: python

    # Instead of reading 1000 bytes at once:
    # data = client.db_read(1, 0, 1000)  # May fail!

    # Read in chunks:
    chunk_size = 200
    data = bytearray()
    for offset in range(0, 1000, chunk_size):
        size = min(chunk_size, 1000 - offset)
        data += client.db_read(1, offset, size)


Permission denied
-----------------

**Error**: ``errCliNeedPassword`` or ``errCliFunctionRefused``

**Cause**: The PLC requires a password or the function is restricted.

**Solution**:

1. Set the PLC password:

   .. code-block:: python

       client.set_session_password("your_password")

2. Check PLC protection level in TIA Portal


Invalid address
---------------

**Error**: ``errCliAddressOutOfRange``

**Cause**: The DB number, start address, or size is invalid.

**Solution**:

1. Verify the DB exists on the PLC
2. Check the DB size in your PLC project
3. Ensure ``start + size`` doesn't exceed the DB length


Server binding error
--------------------

**Error**: ``errSrvCannotStart`` when starting the S7 server

**Cause**: Port 102 is already in use or requires elevated privileges.

**Solutions**:

1. Run with administrator/root privileges
2. Stop any existing snap7 server instances
3. Check if another process is using port 102::

      # Linux/macOS
      $ lsof -i :102

      # Windows
      > netstat -ano | findstr :102
