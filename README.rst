About
=====

.. image:: https://img.shields.io/pypi/v/python-snap7.svg
   :target: https://pypi.python.org/pypi/python-snap7/

.. image:: https://img.shields.io/pypi/pyversions/python-snap7.svg
   :target: https://pypi.python.org/pypi/python-snap7/

.. image:: https://img.shields.io/github/license/gijzelaerr/python-snap7.svg
   :target: https://github.com/gijzelaerr/python-snap7/blob/master/LICENSE

.. image:: https://img.shields.io/github/actions/workflow/status/gijzelaerr/python-snap7/testing.yml?label=tests
   :target: https://github.com/gijzelaerr/python-snap7/actions

.. raw:: html

   <p align="center">
     <strong>🌍 Language / اللغة:</strong>&nbsp;&nbsp;
     <a href="README.rst"><strong>English</strong></a> |
     <a href="README_AR.rst">العربية</a>
   </p>

This is a Python wrapper for `Snap7 <https://snap7.sourceforge.net>`_, an open-source, 32/64 bit, multi-platform Ethernet
communication suite for interfacing natively with Siemens S7 PLCs.

Python-snap7 is tested with Python 3.10+, on Windows, Linux and OS X.

The full documentation is available on `Read The Docs <https://python-snap7.readthedocs.io/en/latest/>`_.


Key Features
============

* 📡 **PLC Communication** — Read/write data blocks, inputs, outputs, and memory areas
* 🔄 **PLC Control** — Start, stop, and cold/hot restart PLCs remotely
* 📊 **Diagnostics** — Read CPU info, status, and order code
* 🖥️ **S7 Server** — Built-in S7 server emulator for testing
* 🤝 **Partner** — Peer-to-peer communication between PLCs
* 🏗️ **Logo Support** — Siemens Logo PLC communication
* 🛠️ **Utilities** — Data conversion helpers for industrial data types


Installation
============

If you are running Windows (amd64), Mac OS X (amd64/aarch64), GNU/Linux (amd64/arm64) or a compatible platform you can install the binary wheel using::

   $ pip install python-snap7

To use the CLI interface for running an emulator::

   $ pip install "python-snap7[cli]"

Otherwise, please follow the `online installation instructions <https://python-snap7.readthedocs.io/en/latest/installation.html>`_ to install python-snap7 from source.


Quick Start
===========

.. code-block:: python

    import snap7

    # Connect to a PLC
    client = snap7.Client()
    client.connect("192.168.0.1", 0, 0)

    # Read data block
    data = client.db_read(1, 0, 10)
    print(f"Data: {data}")

    # Disconnect
    client.disconnect()


Docker
======

Run with Docker::

   $ docker build -t python-snap7 .

Or use Docker Compose::

   $ docker-compose up

See the `Docker documentation <doc/docker.rst>`_ for more details.


Contributing
============

We welcome contributions! Please see the `Development Guide <https://python-snap7.readthedocs.io/en/latest/development.html>`_ for details.


License
=======

This project is licensed under the `MIT License <LICENSE>`_.
