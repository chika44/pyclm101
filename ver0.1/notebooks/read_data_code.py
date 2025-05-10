#!/usr/bin/env python
# coding: utf-8

# # Read Data (Code)
# 
# This notebook demonstrates four ways to read NetCDF climate datasets using `xarray`:
# 
# 1. A single NetCDF file
# 2. Multiple files using wildcards
# 3. Manual file loading with a loop
# 4. Downsampling high-resolution data
# 
# The datasets are located in the `../data/` directory.
# 

# In[1]:


import xarray as xr
import matplotlib.pyplot as plt
import os

# === PARAMETERS ===
data_dir = "../data"
file_slp = "slp.ncep.194801-202504.nc"
file_hgt_all = "hgt_ncep_daily.*.nc"
file_hgt_year = "hgt_ncep_daily.YYYY.nc"
file_sst = "sst.oisst_high.198109-202504.nc"


# ## Approach 1: Reading a Single File with `open_dataset()`
# 

# In[2]:


# Define the start and end years
ystr, yend = 1991, 2020

# === Step 1: Construct full path and open dataset
path_slp = os.path.join(data_dir, file_slp)
ds1 = xr.open_dataset(path_slp)

# === Step 2: Select time range from ystr to yend
slp = ds1["slp"].sel(time=slice(f"{ystr}-01-01", f"{yend}-12-31"))

# === Step 3: Preview result
slp




# In[3]:


# Plot the first time slice
slp.isel(time=0).plot(cmap="coolwarm")
plt.title(f"Sea-Level Pressure on {str(slp.time.values[0])[:10]}")
plt.show()


# ## Approach 2: Reading Multiple Files with `open_mfdataset()`
# 
# This method is useful when data is split into multiple NetCDF files by year or month. Here, we combine geopotential height data from 2018–2020 using a wildcard pattern.
# 

# In[4]:


plev = 500

# === Step 1: Build full path pattern
hgt_path = os.path.join(data_dir, file_hgt_all)

# === Step 2: Open multiple files using wildcard
ds2 = xr.open_mfdataset(hgt_path, combine="by_coords", parallel=True)

# === Step 3: Select 500 hPa level
z500 = ds2["hgt"].sel(level=plev)

# === Step 4: Preview result
z500


# In[5]:


z500.isel(time=0).plot(cmap="viridis")
plt.title("500 hPa Geopotential Height – First Time Step")
plt.show()


# ## Approach 3: Reading Multiple NCEP Files by Year Range
# 
# This method loads daily geopotential height (`hgt`) data from multiple yearly NCEP files using a specified range of years. It uses `xarray.open_mfdataset` to combine the data into a single dataset for easy analysis.
# 

# In[6]:


# === PARAMETERS ===
ystr, yend = 2018, 2020
plev = 250

years = list(range(ystr, yend + 1))
file_list = [os.path.join(data_dir, file_hgt_year.replace("YYYY", str(y))) for y in years]

ds3 = xr.open_mfdataset(file_list, combine="by_coords")
z250 = ds3["hgt"].sel(level=plev)
z250


# In[7]:


z250.isel(time=0).plot(cmap="viridis")
plt.title("250 hPa Geopotential Height – First Time Step")
plt.show()


# ## Approach 4: Downsampling High-Resolution SST Data
# 
# This method demonstrates how to load a high-resolution sea surface temperature (SST) dataset and reduce its spatial resolution to speed up processing and simplify visualization. This is especially useful for global daily SST data.
# 
# We use the NOAA OISST dataset `sst.oisst_high.198109-202504.nc`, which is approximately 0.25° in spatial resolution.
# 

# In[11]:


# === PARAMETERS ===
use_lowres = True
coarsen_factor = 4

# === Paths ===
data_path = os.path.join(data_dir, file_sst)
lowres_file = os.path.join(data_dir, file_sst.replace(".nc", ".low.nc"))

# === Load SST ===
if use_lowres:
    if os.path.exists(lowres_file):
        print(f"📁 Found existing low-res SST: {lowres_file}")
        ds = xr.open_dataset(lowres_file)
    else:
        print(f"⚙️ Creating low-resolution SST from: {data_path}")
        ds_full = xr.open_dataset(data_path)
        ds_lowres = ds_full.isel(
            lat=slice(None, None, coarsen_factor),
            lon=slice(None, None, coarsen_factor)
        ).resample(time="1MS").mean()

        ds_lowres.to_netcdf(lowres_file)
        print(f"✅ Saved low-res file to: {lowres_file}")
        ds = ds_lowres
else:
    print(f"📦 Loading full-resolution SST from: {data_path}")
    ds = xr.open_dataset(data_path)

# === Final variable: sst ===
sst = ds["sst"]
sst


# In[12]:


# === Step 6: Plot the first monthly SST map
sst.isel(time=0).plot(
    cmap="coolwarm", 
    figsize=(10, 5)
)
plt.title(f"SST (Low-Res) — {str(sst.time.values[0])[:10]}")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()


# In[ ]:




