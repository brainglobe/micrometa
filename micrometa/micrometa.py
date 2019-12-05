"""
micrometa
===============

Functions to read image acqusition metadata files.

"""

import configparser
import yaml

from . import tools

SUPPORTED_METADATA_TYPES = ["Cellfinder", "BakingTray", "mesoSPIM"]

CELLFINDER_STR = "cellfinder_meta"
CELLFINDER_SUFFIX = ".ini"

BAKING_TRAY_STR = "recipe"
BAKING_TRAY_SUFFIX = ".yml"

MESOSPIM_STR = "raw_meta"
MESOSPIM_SUFFIX = ".txt"


def get_acqusition_metadata(metadata_path):
    """
    Parses metadata files. Will guess what kind of metadata it is.
    :param metadata_path: Pathlib object referencing the metadata file
    :return: Object with potentially useful metadata attributes
    """
    if (BAKING_TRAY_STR in metadata_path.name) and (
        metadata_path.suffix == BAKING_TRAY_SUFFIX
    ):
        metadata = get_baking_tray_metadata(metadata_path)

    elif (MESOSPIM_STR in metadata_path.name) and (
        metadata_path.suffix == MESOSPIM_SUFFIX
    ):
        metadata = get_mesospim_metadata(metadata_path)

    elif CELLFINDER_STR in metadata_path.name and (
        metadata_path.suffix == CELLFINDER_SUFFIX
    ):
        metadata = get_cellfinder_metadata(metadata_path)

    else:
        raise NotImplementedError(
            "The metadata type of file: '{}' is not yet supported. Please "
            "supply of one of: '{}' or enter metadata manually.".format(
                metadata_path.name, SUPPORTED_METADATA_TYPES
            )
        )

    return metadata


class CellfinderMetadata:
    """
    Class to deal with cellfinder custom metadata files
    """

    def __init__(self, metadata_path):
        self._metadata_path = metadata_path
        self._metadata = read_ini(metadata_path)

    @property
    def x_pixel_um(self):
        pixel_um = self._metadata["voxels"].getfloat("x")
        tools.check_positive_float(pixel_um, none_allowed=False)
        return pixel_um

    @property
    def y_pixel_um(self):
        pixel_um = self._metadata["voxels"].getfloat("y")
        tools.check_positive_float(pixel_um, none_allowed=False)
        return pixel_um

    @property
    def z_pixel_um(self):
        pixel_um = self._metadata["voxels"].getfloat("z")
        tools.check_positive_float(pixel_um, none_allowed=False)
        return pixel_um

    @property
    def num_planes(self):
        num_planes = self._metadata["planes"].getint("num_planes")
        tools.check_positive_int(num_planes, none_allowed=False)
        return num_planes


class BakingTrayMetadata:
    """
    Class to deal with BakingTray
    (https://github.com/SainsburyWellcomeCentre/BakingTray) recipe files:
    """

    def __init__(self, metadata_path):
        self._metadata_path = metadata_path
        self._metadata = read_yaml(metadata_path)

    @property
    def x_pixel_um(self):
        pixel_um = float(
            self._metadata["StitchingParameters"]["VoxelSize"]["X"]
        )
        tools.check_positive_float(pixel_um, none_allowed=False)
        return pixel_um

    @property
    def y_pixel_um(self):
        pixel_um = float(
            self._metadata["StitchingParameters"]["VoxelSize"]["Y"]
        )
        tools.check_positive_float(pixel_um, none_allowed=False)
        return pixel_um

    @property
    def z_pixel_um(self):
        slice_thickness = float(self._metadata["mosaic"]["sliceThickness"])
        num_optical_planes = float(
            self._metadata["mosaic"]["numOpticalPlanes"]
        )
        pixel_um = 1000 * slice_thickness / num_optical_planes
        tools.check_positive_float(pixel_um, none_allowed=False)
        return pixel_um

    @property
    def num_planes(self):
        num_physical_sections = float(self._metadata["mosaic"]["numSections"])
        num_optical_planes = float(
            self._metadata["mosaic"]["numOpticalPlanes"]
        )
        num_planes = num_physical_sections * num_optical_planes
        tools.check_positive_int(num_planes, none_allowed=False)
        return num_planes


class MesoSpimMetadata:
    """
    Class to deal with mesoSPIM (https://github.com/mesoSPIM/mesoSPIM-control)
    metadata files:
    """

    def __init__(self, metadata_path):
        self._metadata_path = metadata_path
        self._metadata = tools.get_text_lines(metadata_path)

    @property
    def x_pixel_um(self):
        line = [
            item
            for item in self._metadata
            if item.startswith("[Pixelsize in um]")
        ][0]
        pixel_um = float(line.split()[-1])
        tools.check_positive_float(pixel_um, none_allowed=False)
        return pixel_um

    @property
    def y_pixel_um(self):
        line = [
            item
            for item in self._metadata
            if item.startswith("[Pixelsize in um]")
        ][0]
        pixel_um = float(line.split()[-1])
        tools.check_positive_float(pixel_um, none_allowed=False)
        return pixel_um

    @property
    def z_pixel_um(self):
        line = [
            item for item in self._metadata if item.startswith("[z_stepsize]")
        ][0]
        pixel_um = float(line.split()[-1])
        tools.check_positive_float(pixel_um, none_allowed=False)
        return pixel_um

    @property
    def num_planes(self):
        line = [
            item for item in self._metadata if item.startswith("[z_planes]")
        ][0]
        num_planes = int(line.split()[-1])
        tools.check_positive_int(num_planes, none_allowed=False)
        return num_planes


def get_cellfinder_metadata(metadata_path):
    """
    Parses cellfinder custom metadata files.
    :param metadata_path: Pathlib object referencing the metadata file
    :return: Object with potentially useful metadata attributes
    """

    return CellfinderMetadata(metadata_path)


def get_baking_tray_metadata(metadata_path):
    """
    Parses BakingTray (https://github.com/SainsburyWellcomeCentre/BakingTray)
    recipe files.
    :param metadata_path: Pathlib object referencing the metadata file
    :return: Object with potentially useful metadata attributes
    """

    return BakingTrayMetadata(metadata_path)


def get_mesospim_metadata(metadata_path):
    """
    Parses mesoSPIM (https://github.com/mesoSPIM/mesoSPIM-control)
    metadata files.
    :param metadata_path: Pathlib object referencing the metadata file
    :return: Object with potentially useful metadata attributes
    """

    return MesoSpimMetadata(metadata_path)


def read_ini(ini_path):
    """
    Returns a configparser object to be parsed.
    :param ini_path: Path to ini file
    :return: configparser object to be parsed.
    """

    config = configparser.ConfigParser()
    config.read(ini_path)
    return config


def read_yaml(yaml_path):
    """
    Returns a yaml object to be parsed.
    :param yaml_path: Path to yaml file
    :return: yaml object to be parsed.
    """

    with open(yaml_path, "r") as stream:
        return yaml.safe_load(stream)
