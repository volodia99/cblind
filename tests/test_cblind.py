import matplotlib as mpl
import cblind

import pytest

def test_cmap_registration():
    import cblind # noqa
    for name in cblind.cblind.PALETTES_FULL:
        assert name in mpl.colormaps


def test_cbmap_deprecation():
    with pytest.deprecated_call():
        cblind.cbmap("cb.extreme_rainbow")

