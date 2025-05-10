# Read NetCDF Data

Climate datasets are commonly stored in NetCDF (Network Common Data Form), a flexible format designed for storing array-oriented scientific data. Efficiently reading and managing these files is a critical first step in climate data analysis.

In this chapter, we introduce several practical methods for loading NetCDF files using the Python `xarray` library, which provides convenient tools for working with labeled multi-dimensional arrays.

## What You'll Learn

- How to load a single consolidated NetCDF file
- How to combine multiple files using wildcards or file templates
- How to build file lists programmatically using year ranges
- How to downsample high-resolution data for faster analysis

The accompanying notebook provides hands-on examples for each method, and the overview page summarizes their typical use cases and limitations.

> 📂 All example data files are assumed to be located in the `../data/` directory relative to the notebook.


