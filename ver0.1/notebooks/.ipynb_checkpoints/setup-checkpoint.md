# Setup Instructions

This page provides step-by-step instructions for setting up a Python environment for climate data analysis using Miniconda, GeoCAT tools, and Jupyter. It also includes how to run JupyterLab on a remote server and access it from your local machine.

---

## Miniconda Installation

First, install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) for your operating system (macOS, Linux, or Windows).

---

## Package Installation

Update conda and create a new environment with the required packages:

```
conda update conda
conda create -n geocat -c conda-forge geocat-comp geocat-viz
conda install -n geocat jupyter
```

---

## Under `geocat` Environment

Activate the environment:

```
conda activate geocat
```

---

## GRIB Support (Takes Longer)

Install additional tools to read GRIB files:

```
conda install -c conda-forge cfgrib eccodes
```

---

## JupyterLab Notebook

### On Remote Server (`zion`)

Log in and launch JupyterLab or Notebook:

```
ssh user@zion.serv.usu.edu
conda activate geocat

nohup jupyter lab --no-browser --port=8888 --ip=0.0.0.0 > jupyter.log 2>&1 &
# or
nohup jupyter notebook --no-browser --port=8888 --ip=0.0.0.0 > jupyter_notebook.log 2>&1 &
```

---

### On Local Computer (Mac)

Create an SSH tunnel from your local machine to the remote server:

```
ssh -L 8888:localhost:8888 chika44@zion.serv.usu.edu
```

Then open a web browser and visit:

```
http://localhost:8888
```

---

## Convert from Jupyter to Python Code

To convert a notebook to a `.py` script:

```
jupyter nbconvert --to script file.ipynb
```


