[![Travis](https://img.shields.io/travis/com/adamltyson/micrometa?label=Travis%20CI)](
    https://travis-ci.com/adamltyson/micrometa)
[![Coverage Status](https://coveralls.io/repos/github/adamltyson/micrometa/badge.svg?branch=master)](https://coveralls.io/github/adamltyson/micrometa?branch=master)
    
# micrometa
Reading of microscopy metadata

### About
micrometa reads metadata from various whole-organ microscopes for use with 
[cellfinder](https://github.com/SainsburyWellcomeCentre/cellfinder) and
[amap](https://github.com/SainsburyWellcomeCentre/amap-python).

This is a work in progress, and currently the only metadata files supported 
are:
* [BakingTray](https://github.com/SainsburyWellcomeCentre/BakingTray) 
recipe files 
* [mesoSPIM](https://github.com/mesoSPIM/mesoSPIM-control) 
 metadata files
 * [amap custom metadata files](https://raw.githubusercontent.com/adamltyson/micrometa/master/tests/data/metadata/amap_metadata.ini)
* [cellfinder custom metadata files](https://raw.githubusercontent.com/adamltyson/micrometa/master/tests/data/metadata/cellfinder_metadata.ini)

Parameters currently supported are:
* Number of planes in the axial direction
* Pixel sizes in x, y & z


### To install
```bash
pip install micrometa
```

### To use
```python
from micrometa.micrometa import get_acquisition_metadata
metadata = get_acquisition_metadata("cellfinder_metadata.ini")
print(metadata.x_pixel_um)
print(metadata.y_pixel_um)
print(metadata.z_pixel_um)
print(metadata.num_planes)
```