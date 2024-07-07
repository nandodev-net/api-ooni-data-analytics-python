"""Init Test."""

import sys

import django


def test_python_version():
    """Test version."""
    print("Python version:", sys.version)
    print("Django version:", django.get_version())
    assert True
