# Authors: The MNE-Python contributors.
# License: BSD-3-Clause
# Copyright the MNE-Python contributors.

import warnings

import pytest


def has_pyvista():
    """Check that PyVista is installed."""
    try:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            import pyvista  # noqa: F401
        return True
    except ImportError:
        return False


def has_pyvistaqt():
    """Check that PyVistaQt is installed."""
    try:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            import pyvistaqt  # noqa: F401
        return True
    except ImportError:
        return False


def has_imageio_ffmpeg():
    """Check if imageio-ffmpeg is installed."""
    try:
        import imageio_ffmpeg  # noqa: F401

        return True
    except ImportError:
        return False


skips_if_not_pyvistaqt = pytest.mark.skipif(
    not has_pyvistaqt(), reason="requires pyvistaqt"
)
