"""
Retry utility for snap7 connections.

أداة إعادة المحاولة لاتصالات snap7.

Provides a configurable retry mechanism for PLC communication,
handling transient connection failures gracefully.
"""

import logging
import time
from functools import wraps
from typing import Any, Callable, Optional, TypeVar, cast

logger = logging.getLogger(__name__)

F = TypeVar("F", bound=Callable[..., Any])


def retry(
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: tuple[type[Exception], ...] = (RuntimeError,),
    on_retry: Optional[Callable[[Exception, int], None]] = None,
) -> Callable[[F], F]:
    """Decorator that retries a function on failure.

    Useful for PLC operations that may fail due to transient
    network issues or temporary PLC unavailability.

    Args:
        max_attempts: Maximum number of attempts (default: 3).
        delay: Initial delay between retries in seconds (default: 1.0).
        backoff: Multiplier for delay after each retry (default: 2.0).
        exceptions: Tuple of exception types to catch and retry on.
        on_retry: Optional callback called on each retry with (exception, attempt_number).

    Returns:
        Decorated function with retry behavior.

    Example:
        >>> from snap7.util.retry import retry
        >>> @retry(max_attempts=3, delay=0.5)
        ... def read_data(client, db, start, size):
        ...     return client.db_read(db, start, size)
    """

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception: Optional[Exception] = None
            current_delay = delay

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts:
                        logger.warning(
                            f"Attempt {attempt}/{max_attempts} failed for {func.__name__}: {e}. "
                            f"Retrying in {current_delay:.1f}s..."
                        )
                        if on_retry:
                            on_retry(e, attempt)
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        logger.error(f"All {max_attempts} attempts failed for {func.__name__}: {e}")

            raise last_exception  # type: ignore[misc]

        return cast(F, wrapper)

    return decorator


class RetryConfig:
    """Configuration class for retry behavior.

    Provides a reusable configuration object for retry parameters.

    Args:
        max_attempts: Maximum number of attempts.
        delay: Initial delay between retries in seconds.
        backoff: Multiplier for delay after each retry.
        exceptions: Tuple of exception types to catch.

    Example:
        >>> from snap7.util.retry import RetryConfig
        >>> config = RetryConfig(max_attempts=5, delay=0.5)
        >>> @config.wrap
        ... def my_function():
        ...     pass
    """

    def __init__(
        self,
        max_attempts: int = 3,
        delay: float = 1.0,
        backoff: float = 2.0,
        exceptions: tuple[type[Exception], ...] = (RuntimeError,),
    ) -> None:
        self.max_attempts = max_attempts
        self.delay = delay
        self.backoff = backoff
        self.exceptions = exceptions

    def wrap(self, func: F) -> F:
        """Apply retry configuration as a decorator.

        Args:
            func: Function to wrap with retry behavior.

        Returns:
            Wrapped function.
        """
        return retry(
            max_attempts=self.max_attempts,
            delay=self.delay,
            backoff=self.backoff,
            exceptions=self.exceptions,
        )(func)
