Docker
======

python-snap7 provides Docker support for running an S7 server emulator
and for development purposes.


Docker Build
------------

Build the Docker image::

    $ docker build -t python-snap7 .

Run the container::

    $ docker run -p 102:102 python-snap7 snap7-server

This will start the S7 server emulator listening on port 102, which is the
standard S7 communication port.


Docker Compose
--------------

A ``docker-compose.yml`` file is provided with two services:

**snap7-server** — S7 Server Emulator
    Starts the built-in snap7 server emulator for testing PLC communication.
    Exposes port 102 for S7 client connections.

**snap7-dev** — Development Environment
    Mounts the source code into the container for live development and testing.
    Activated with the ``dev`` profile.

Start the server emulator::

    $ docker-compose up

Start in background::

    $ docker-compose up -d

Stop and remove containers::

    $ docker-compose down

Start the development environment::

    $ docker-compose --profile dev run snap7-dev

Open a shell in the development container::

    $ docker-compose --profile dev run snap7-dev bash


Connecting to the Emulator
--------------------------

Once the server is running, you can connect from your host machine:

.. code-block:: python

    import snap7

    client = snap7.Client()
    client.connect("127.0.0.1", 0, 0, 102)

    # Check connection
    print(f"Connected: {client.get_connected()}")

    # Read CPU info
    cpu_info = client.get_cpu_info()
    print(f"CPU: {cpu_info}")

    client.disconnect()


Dockerfile Reference
--------------------

The provided ``Dockerfile`` is based on Ubuntu 24.04 and:

1. Installs the snap7 native library from the PPA
2. Creates a Python virtual environment
3. Installs python-snap7 into the virtual environment

The ``snap7-server`` CLI command is available after build, which starts
a basic S7 server emulator.
