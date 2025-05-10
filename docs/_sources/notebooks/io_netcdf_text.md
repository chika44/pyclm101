
# NetCDF: Method Overview

This page describes various approaches to reading NetCDF climate data using `xarray`. It explains different use cases, strengths, and limitations of each method.

---

## 📂 Example Datasets

| File Name                        | Description                                  |
|----------------------------------|----------------------------------------------|
| `slp.ncep.194801-202504.nc`      | Monthly sea level pressure (multi-decade, single file) |
| `hgt_ncep_daily.2018.nc`         | Daily geopotential height (2018)             |
| `hgt_ncep_daily.2019.nc`         | Daily geopotential height (2019)             |
| `hgt_ncep_daily.2020.nc`         | Daily geopotential height (2020)             |
| `sst.oisst_high.198109-202504.nc`| Monthly high-resolution SST                    |

---
## 📘 Approach 1: Reading a Single NetCDF File

Use xr.open_dataset() when the dataset is already consolidated into a single file with all variables and time steps. This is ideal for simple, complete datasets.

```python
    import xarray as xr

    ds_slp = xr.open_dataset("../data/slp.ncep.194801-202504.nc")
    ds_slp.slp.isel(time=0).plot()
```

---

## 📘 Approach 2: Reading Multiple Files with a Wildcard

Use xr.open_mfdataset() to automatically combine many files (e.g., one per year) that follow a naming pattern. This is common for reanalysis or observational archives.

```python
    ds_hgt = xr.open_mfdataset("../data/hgt_ncep_daily.20*.nc", combine="by_coords")
    ds_hgt.hgt.sel(level=500).isel(time=0).plot()
```

Make sure the files are consistent in structure and metadata.

---

## 📘 Approach 3: Reading NCEP Files by Year Range

If you want explicit control over which files to include, use a year range to construct filenames like hgt_ncep_daily.YYYY.nc. This is useful when skipping specific years or handling missing files.

```python
    years = list(range(2018, 2021))
    file_list = [file_template.replace("YYYY", str(y)) for y in years]
    ds = xr.open_mfdataset(file_list, combine="by_coords")
```

---

## 📘 Approach 4: Downsampling High-Resolution SST

High-resolution datasets (e.g., 0.25° daily SST) can be downsampled for faster analysis. There are two main methods for reducing spatial resolution: **subsampling** using `isel()` and **block averaging** using `coarsen()`.

---

### 🔹 Option A: Subsampling using `isel()`

This method selects every N-th grid point along latitude and longitude. It's fast but does not preserve averages.

```python
    ds_lowres = ds_full.isel(
        lat=slice(None, None, coarsen_factor),
        lon=slice(None, None, coarsen_factor)
    )
```

- ✅ Fast and simple
- ⚠️ May miss finer-scale structure
- 🔄 Use when quick preview or approximate results are sufficient

---

### 🔹 Option B: Block averaging using `coarsen()`

This method divides the grid into blocks (e.g., 4×4) and computes the mean in each block. It better preserves physical meaning.

```python
    dataL = data.coarsen(
        latitude=coarsen_factor,
        longitude=coarsen_factor,
        boundary='trim'
    ).mean()
```

- ✅ Preserves spatial means
- ⚠️ Slightly slower, but more accurate
- 🔄 Use for climate analysis, long-term statistics, or model comparisons

---

Both methods can be combined with `.resample(time="1MS").mean()` if the input is daily and monthly aggregation is desired.



---



## 🔗 See Also

👉 View the companion notebook: [read_data_code.ipynb](read_data_code.ipynb)


