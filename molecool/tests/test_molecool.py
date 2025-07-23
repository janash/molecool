"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import molecool


def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "molecool" in sys.modules
