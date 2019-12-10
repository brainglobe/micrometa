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
* [cellfinder custom metadata files](https://github.com/SainsburyWellcomeCentre/cellfinder/tree/master/doc_build/examples/cellfinder_metadata.ini)

Parameters currently supported are:
* Number of planes in the axial direction
* Pixel sizes in x, y & z


### To install
```bash
pip install micrometa
```

### To use
```python
from micrometa.micrometa import get_acqusition_metadata
metadata = get_acqusition_metadata("cellfinder_metadata.ini")
print(metadata.x_pixel_um)
print(metadata.y_pixel_um)
print(metadata.z_pixel_um)
print(metadata.num_planes)
```