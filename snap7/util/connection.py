"""
Connection management utilities for snap7.

أدوات إدارة الاتصال لـ snap7.

Provides enhanced connection management with auto-reconnect,
connection health monitoring, and timeout configuration.
"""

import logging
import time
from typing import Optional

from snap7.client import Client
from snap7.type import Parameter

logger = logging.getLogger(__name__)


class ConnectionConfig:
    """Configuration for PLC connection parameters.

    تكوين معاملات الاتصال بـ PLC.

    Args:
        address: IP address of the PLC.
        rack: Rack number (default: 0).
        slot: Slot number (default: 0).
        tcp_port: TCP port (default: 102).
        ping_timeout: Timeout for ping in milliseconds (default: 750).
        send_timeout: Timeout for send in milliseconds (default: 10000).
        recv_timeout: Timeout for receive in milliseconds (default: 3000).

    Example:
        >>> config = ConnectionConfig("192.168.0.1", rack=0, slot=0)
        >>> print(f"PLC at {config.address}")
    """

    def __init__(
        self,
        address: str,
        rack: int = 0,
        slot: int = 0,
        tcp_port: int = 102,
        ping_timeout: int = 750,
        send_timeout: int = 10000,
        recv_timeout: int = 3000,
    ) -> None:
        self.address = address
        self.rack = rack
        self.slot = slot
        self.tcp_port = tcp_port
        self.ping_timeout = ping_timeout
        self.send_timeout = send_timeout
        self.recv_timeout = recv_timeout


class ManagedClient:
    """A managed snap7 client with auto-reconnect and health monitoring.

    عميل snap7 مُدار مع إعادة اتصال تلقائية ومراقبة صحة الاتصال.

    Wraps the standard snap7 Client with:
    - Configurable timeouts
    - Auto-reconnect on connection loss
    - Connection health checking
    - Context manager support

    Args:
        config: Connection configuration.
        auto_reconnect: Enable auto-reconnect (default: True).
        max_reconnect_attempts: Maximum reconnection attempts (default: 3).
        reconnect_delay: Delay between reconnection attempts in seconds (default: 1.0).

    Example:
        >>> config = ConnectionConfig("192.168.0.1")
        >>> with ManagedClient(config) as client:
        ...     data = client.db_read(1, 0, 10)
        ...     print(data)
    """

    def __init__(
        self,
        config: ConnectionConfig,
        auto_reconnect: bool = True,
        max_reconnect_attempts: int = 3,
        reconnect_delay: float = 1.0,
    ) -> None:
        self._config = config
        self._auto_reconnect = auto_reconnect
        self._max_reconnect_attempts = max_reconnect_attempts
        self._reconnect_delay = reconnect_delay
        self._client: Optional[Client] = None
        self._connected = False

    @property
    def client(self) -> Client:
        """Get the underlying snap7 client, reconnecting if needed.

        Returns:
            The snap7 Client instance.

        Raises:
            RuntimeError: If not connected and auto-reconnect fails.
        """
        if self._client is None or not self.is_connected():
            if self._auto_reconnect:
                self._reconnect()
            else:
                raise RuntimeError("Not connected to PLC and auto-reconnect is disabled")
        assert self._client is not None
        return self._client

    def connect(self) -> "ManagedClient":
        """Connect to the PLC with configured timeouts.

        Returns:
            Self for method chaining.

        Raises:
            RuntimeError: If connection fails.
        """
        self._client = Client()

        # Apply timeout settings
        # تطبيق إعدادات المهلة
        self._client.set_param(Parameter.PingTimeout, self._config.ping_timeout)
        self._client.set_param(Parameter.SendTimeout, self._config.send_timeout)
        self._client.set_param(Parameter.RecvTimeout, self._config.recv_timeout)

        logger.info(
            f"Connecting to PLC at {self._config.address}:{self._config.tcp_port} "
            f"(rack={self._config.rack}, slot={self._config.slot})"
        )
        self._client.connect(
            self._config.address,
            self._config.rack,
            self._config.slot,
            self._config.tcp_port,
        )
        self._connected = True
        logger.info("Connected successfully")
        return self

    def disconnect(self) -> None:
        """Disconnect from the PLC."""
        if self._client is not None:
            try:
                self._client.disconnect()
            except Exception as e:
                logger.warning(f"Error during disconnect: {e}")
            finally:
                self._connected = False

    def is_connected(self) -> bool:
        """Check if the client is currently connected.

        Returns:
            True if connected, False otherwise.
        """
        if self._client is None:
            return False
        try:
            return bool(self._client.get_connected())
        except Exception:
            return False

    def _reconnect(self) -> None:
        """Attempt to reconnect to the PLC.

        Raises:
            RuntimeError: If all reconnection attempts fail.
        """
        last_error: Optional[Exception] = None

        for attempt in range(1, self._max_reconnect_attempts + 1):
            try:
                logger.info(f"Reconnection attempt {attempt}/{self._max_reconnect_attempts}")
                self.disconnect()
                self.connect()
                return
            except Exception as e:
                last_error = e
                logger.warning(f"Reconnection attempt {attempt} failed: {e}")
                if attempt < self._max_reconnect_attempts:
                    time.sleep(self._reconnect_delay)

        raise RuntimeError(
            f"Failed to reconnect after {self._max_reconnect_attempts} attempts: {last_error}"
        )

    def db_read(self, db_number: int, start: int, size: int) -> bytearray:
        """Read from a data block with auto-reconnect support.

        Args:
            db_number: DB number to read from.
            start: Start byte offset.
            size: Number of bytes to read.

        Returns:
            Data read from the PLC.
        """
        return self.client.db_read(db_number, start, size)

    def db_write(self, db_number: int, start: int, data: bytearray) -> None:
        """Write to a data block with auto-reconnect support.

        Args:
            db_number: DB number to write to.
            start: Start byte offset.
            data: Data to write.
        """
        self.client.db_write(db_number, start, data)

    def get_cpu_state(self) -> str:
        """Get CPU state with auto-reconnect support.

        Returns:
            CPU state string.
        """
        return self.client.get_cpu_state()

    def __enter__(self) -> "ManagedClient":
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, *args: object) -> None:
        """Context manager exit."""
        self.disconnect()

    def __repr__(self) -> str:
        status = "connected" if self._connected else "disconnected"
        return f"<ManagedClient {self._config.address}:{self._config.tcp_port} [{status}]>"
