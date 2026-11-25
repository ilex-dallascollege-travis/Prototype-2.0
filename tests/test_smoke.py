"""Smoke tests verifying package installation and deterministic test harness."""

import prototype2


def test_package_version_is_set() -> None:
    """Confirm the prototype2 package imports cleanly and exposes a version."""
    assert prototype2.__version__ == "0.1.0"
