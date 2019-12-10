import pytest

from pathlib import Path
from math import isclose

import micrometa.micrometa as meta

data_dir = Path("tests", "data")
metadata_dir = data_dir / "metadata"

cellfinder_metadata = metadata_dir / "cellfinder_metadata.ini"
amap_metadata = metadata_dir / "amap_metadata.ini"
baking_tray_metadata = metadata_dir / "BakingTray_recipe.yml"
mesoSPIM_metadata = metadata_dir / "mesoSPIM.raw_meta.txt"
unsupported_metadata = metadata_dir / "unsupported_metadata.txt"

VOX_DIM_TOLERANCE = 0.1


def test_cellfinder_meta():
    metadata = meta.get_acquisition_metadata(cellfinder_metadata)
    assert isclose(2, metadata.x_pixel_um, abs_tol=VOX_DIM_TOLERANCE)
    assert isclose(2, metadata.y_pixel_um, abs_tol=VOX_DIM_TOLERANCE)
    assert isclose(5, metadata.z_pixel_um, abs_tol=VOX_DIM_TOLERANCE)

    assert metadata.num_planes == 1500


def test_amap_meta():
    metadata = meta.get_acquisition_metadata(amap_metadata)
    assert isclose(8, metadata.x_pixel_um, abs_tol=VOX_DIM_TOLERANCE)
    assert isclose(8, metadata.y_pixel_um, abs_tol=VOX_DIM_TOLERANCE)
    assert isclose(20, metadata.z_pixel_um, abs_tol=VOX_DIM_TOLERANCE)

    assert metadata.num_planes == 100


def test_baking_tray_meta():
    metadata = meta.get_acquisition_metadata(baking_tray_metadata)
    assert isclose(2.19, metadata.x_pixel_um, abs_tol=VOX_DIM_TOLERANCE)
    assert isclose(2.14, metadata.y_pixel_um, abs_tol=VOX_DIM_TOLERANCE)
    assert isclose(5, metadata.z_pixel_um, abs_tol=VOX_DIM_TOLERANCE)

    assert metadata.num_planes == 2000


def test_mesospim_meta():
    metadata = meta.get_acquisition_metadata(mesoSPIM_metadata)
    assert isclose(8.23, metadata.x_pixel_um, abs_tol=VOX_DIM_TOLERANCE)
    assert isclose(8.23, metadata.y_pixel_um, abs_tol=VOX_DIM_TOLERANCE)
    assert isclose(10, metadata.z_pixel_um, abs_tol=VOX_DIM_TOLERANCE)

    assert metadata.num_planes == 852


def test_unsupported_meta():
    with pytest.raises(NotImplementedError):
        assert meta.get_acquisition_metadata(unsupported_metadata)
