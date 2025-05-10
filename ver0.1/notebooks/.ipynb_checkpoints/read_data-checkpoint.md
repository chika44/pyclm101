# Reading NetCDF Datasets in Python

This page introduces four approaches for reading and managing climate datasets in NetCDF format using `xarray`. These methods are tailored to suit different data formats, file organizations, and resolution needs.

The examples below use files stored in the `data/` directory.

---

## 📂 Example Datasets

| File Name                        | Description                                  |
|----------------------------------|----------------------------------------------|
| `slp.ncep.194801-202504.nc`      | Sea-level pressure (multi-decade, single file) |
| `hgt_ncep_daily.2018.nc`         | Daily geopotential height (2018)             |
| `hgt_ncep_daily.2019.nc`         | Daily geopotential height (2019)             |
| `hgt_ncep_daily.2020.nc`         | Daily geopotential height (2020)             |
| `sst.oisst_high.198109-202504.nc`| Daily high-resolution SST                    |

---

## 📘 Approach 1: Reading a Single NetCDF File

Use `xr.open_dataset()` when the dataset is already consolidated into a single file.

```python
import xarray as xr

ds_slp = xr.open_dataset("../data/slp.ncep.194801-202504.nc")
ds_slp.slp.isel(time=0).plot()
```

---

## 📘 Approach 2: Reading Multiple Files with a Wildcard

Use `xr.open_mfdataset()` to automatically combine many files (e.g., one per year).

```python
ds_hgt = xr.open_mfdataset("../data/hgt_ncep_daily.20*.nc", combine="by_coords")
ds_hgt.hgt.sel(level=500).isel(time=0).plot()
```

---

## 📘 Approach 3: Looping Over Years and Building a List

Sometimes, especially with forecast model output, file names follow a strict pattern. You can loop through the years and manually load available files:

```python
import os
import xarray as xr

sst_list = []
dummy_shape = None
dummy_coords = None

for year in range(2010, 2021):  # example range
    month_str = "01"
    yyyymm = f"{year}{month_str}"
    filename = f"sst.i{yyyymm}.nc"
    file_path = os.path.join("path/to/dataset", "MODEL_NAME", filename)

    if os.path.isfile(file_path):
        try:
            ds = xr.open_dataset(file_path)
            if "sst" in ds:
                sst = ds["sst"].expand_dims(init=[year])
                sst_list.append(sst)

                if dummy_shape is None:
                    dummy_shape = sst.shape[1:]  # exclude 'init'
                    dummy_coords = {k: v for k, v in sst.coords.items() if k != "init"}
            else:
                print(f"[WARNING] 'sst' not found in {filename}")
                sst_list.append(make_nan_sst(year, dummy_shape, dummy_coords))
        except Exception as e:
            print(f"[ERROR] Failed to open {filename}: {e}")
            sst_list.append(make_nan_sst(year, dummy_shape, dummy_coords))
    else:
        print(f"[MISSING] {filename} not found")
        sst_list.append(make_nan_sst(year, dummy_shape, dummy_coords))
```

This method gives you full control over missing files and error handling.

---

## 📘 Approach 4: Downsampling High-Resolution Data

When working with high-resolution global datasets, it is often helpful to reduce resolution before analysis for faster computation.

```python
ds_sst = xr.open_dataset("../data/sst.oisst_high.198109-202504.nc")

# Downsample spatially by taking every 4th grid point (e.g., from 0.25° to ~1°)
ds_sst_lowres = ds_sst.isel(lat=slice(None, None, 4), lon=slice(None, None, 4))

# Optional: resample monthly mean if daily data
ds_sst_monthly = ds_sst_lowres.resample(time="1MS").mean()

# Quick look
ds_sst_monthly.sst.isel(time=0).plot()
```

This approach significantly improves performance during exploratory analysis or plotting.

---

## 🔗 See Also

👉 View the companion notebook: [read_data.ipynb](read_data.ipynb)


