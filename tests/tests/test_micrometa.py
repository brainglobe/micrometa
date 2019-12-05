import pytest

from pathlib import Path
from math import isclose

import micrometa.micrometa as meta

data_dir = Path("tests", "data")
metadata_dir = data_dir / "metadata"

cellfinder_metadata = metadata_dir / "cellfinder_metadata.ini"
baking_tray_metadata = metadata_dir / "BakingTray_recipe.yml"
mesoSPIM_metadata = metadata_dir / "mesoSPIM.raw_meta.txt"
unsupported_metadata = metadata_dir / "unsupported_metadata.txt"
missing_metadata = metadata_dir / "cellfinder_metadata_missing.ini"

VOX_DIM_TOLERANCE = 0.1


def test_cellfinder_meta():
    metadata = meta.get_acqusition_metadata(cellfinder_metadata)
    assert isclose(2, metadata.x_pixel_um, abs_tol=VOX_DIM_TOLERANCE)
    assert isclose(2, metadata.y_pixel_um, abs_tol=VOX_DIM_TOLERANCE)
    assert isclose(5, metadata.z_pixel_um, abs_tol=VOX_DIM_TOLERANCE)

    assert metadata.num_planes == 1500


def test_baking_tray_meta():
    metadata = meta.get_acqusition_metadata(baking_tray_metadata)
    assert isclose(2.19, metadata.x_pixel_um, abs_tol=VOX_DIM_TOLERANCE)
    assert isclose(2.14, metadata.y_pixel_um, abs_tol=VOX_DIM_TOLERANCE)
    assert isclose(5, metadata.z_pixel_um, abs_tol=VOX_DIM_TOLERANCE)

    assert metadata.num_planes == 2000


def test_mesospim_meta():
    metadata = meta.get_acqusition_metadata(mesoSPIM_metadata)
    assert isclose(8.23, metadata.x_pixel_um, abs_tol=VOX_DIM_TOLERANCE)
    assert isclose(8.23, metadata.y_pixel_um, abs_tol=VOX_DIM_TOLERANCE)
    assert isclose(10, metadata.z_pixel_um, abs_tol=VOX_DIM_TOLERANCE)

    assert metadata.num_planes == 852


def test_unsupported_meta():
    with pytest.raises(NotImplementedError):
        assert meta.get_acqusition_metadata(unsupported_metadata)


class Args:
    def __init__(self):
        self.x_pixel_um = self.y_pixel_um = self.z_pixel_um = None
        self.metadata = None

    def set_all_pixel_sizes(self):
        self.x_pixel_um = 1
        self.y_pixel_um = 2
        self.z_pixel_um = 3

    def set_some_pixel_sizes_w_meta_baking_tray(self):
        self.x_pixel_um = 10
        self.y_pixel_um = None
        self.z_pixel_um = 40

        self.metadata = baking_tray_metadata

    def set_some_pixel_sizes_w_meta_mesospim(self):
        self.x_pixel_um = 100
        self.y_pixel_um = None
        self.z_pixel_um = None

        self.metadata = mesoSPIM_metadata

    def set_some_pixel_sizes_w_meta_cellfinder(self):
        self.x_pixel_um = None
        self.y_pixel_um = 0.2
        self.z_pixel_um = 40

        self.metadata = cellfinder_metadata

    def set_some_pixel_sizes_no_meta(self):
        self.x_pixel_um = None
        self.y_pixel_um = 100
        self.z_pixel_um = 3
        self.metadata = None

    def set_some_pixel_sizes_unsupported_meta(self):
        self.x_pixel_um = None
        self.y_pixel_um = 100
        self.z_pixel_um = 3
        self.metadata = unsupported_metadata

    def set_some_pixel_sizes_missing_meta(self):
        self.x_pixel_um = None
        self.y_pixel_um = 100
        self.z_pixel_um = 3
        self.metadata = missing_metadata
