# Setup Instructions

This page provides step-by-step instructions for setting up a Python environment for climate data analysis using Miniconda, the GeoCAT tool suite, and Jupyter. It also covers how to run JupyterLab on a remote server and securely access it from your local computer.

---

## 🐍 Install Miniconda

Download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) for your operating system (macOS, Linux, or Windows). Follow the installer instructions to complete the setup.

---

## 📦 Create a Conda Environment with GeoCAT Tools

Update Conda and create a new environment named `geocat` with the required packages:

```bash
 conda update conda
 conda create -n geocat -c conda-forge geocat-comp geocat-viz
```

Additional package installation:

```bash
 conda install -n geocat jupyter
 conda install -n geocat ncview
```



Then activate the environment:

```bash
 conda activate geocat
```

---

###  Optional: Add GRIB File Support

If you plan to work with GRIB-format datasets (e.g., from ECMWF), install the following:

```bash
 conda install -c conda-forge cfgrib eccodes
```

> ⏳ This step may take longer due to larger package dependencies.

---

## 🚀 Running JupyterLab on a Remote Server

### 1. Connect to the Server

Log in to the remote server via SSH:

```bash
 ssh your_username@your.server.address.edu
```

> 🔑 **Note**: Replace `your_username` with your assigned login name, and replace `your.server.address.edu` with the actual server address provided by your instructor.

### 2. Start JupyterLab or Notebook

After logging in the remote server:

```bash
 conda activate geocat
```

Option A: Start JupyterLab

```bash
 nohup jupyter lab --no-browser --port=8888 --ip=0.0.0.0 > jupyter.log 2>&1 &
```

Option B: Start Jupyter Notebook

```bash
 nohup jupyter notebook --no-browser --port=8888 --ip=0.0.0.0 > jupyter_notebook.log 2>&1 &
```

This launches the server in the background and logs output to a file.

---

### 3. Accessing the Remote Jupyter Session from Your Local Machine (macOS)

On your local computer, create an SSH tunnel to the remote server:

```bash
 ssh -L 8888:localhost:8888 your_username@your.server.address.edu
```

Once connected, open a browser and navigate to:

```
http://localhost:8888
```

> 🔐 If prompted for a token, you can find it in the `jupyter.log` file on the server.

---

## 🔁 Convert Jupyter Notebooks to Python Scripts

To convert a `.ipynb` notebook to a plain `.py` script:

```bash
 jupyter nbconvert --to script file.ipynb
```

This is useful for sharing code or version control.

---

