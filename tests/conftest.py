"""Shared pytest fixtures and deterministic random seed configuration."""

import random

import numpy as np
import pytest


@pytest.fixture(autouse=True)
def deterministic_seed() -> None:
    """Seed standard library and NumPy RNGs before every test."""
    random.seed(42)
    np.random.seed(42)
