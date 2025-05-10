# Reading GRIB Files

GRIB (GRIdded Binary) is a highly compressed format used in operational weather forecasting. It's often used by agencies like ECMWF and NOAA.

To work with GRIB files in Python, you'll need the `cfgrib` engine, which is part of the `ecCodes` toolkit.

## ⚙️ Installation (One Time Setup)

```bash
conda install -c conda-forge cfgrib eccodes
```

## 📥 Reading GRIB Data with xarray

```python
import xarray as xr

ds = xr.open_dataset("../data/example.grib", engine="cfgrib")
print(ds)
```

## 🧠 Notes

- GRIB files may have multiple message levels or parameter types.
- Use `filter_by_keys` in `cfgrib` to narrow down dimensions (e.g., `shortName`, `typeOfLevel`, `level`).

> GRIB is not as flexible as NetCDF for self-describing metadata, but it is widely used in operational and real-time settings.


