# Python Package Installation

Once Miniconda is installed, use it to create a dedicated environment for PyClm101.

## 🛠️ Create and Configure the Environment

```bash
    conda update conda
    conda create -n geocat -c conda-forge geocat-comp geocat-viz
    conda install -n geocat jupyter ncview
```

## 🐍 Activate the Environment

```bash
    conda activate geocat
```

## 📦 Optional: GRIB Support

If you'll be working with GRIB data (common in ECMWF datasets):

```bash
    conda install -c conda-forge cfgrib eccodes
```

> Note: These may take longer to install due to their dependencies.


