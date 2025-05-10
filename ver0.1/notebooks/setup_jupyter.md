# Jupyter Notebook

This section explains three typical workflows for using Jupyter in the PyClm101 environment:

- Run JupyterLab locally
- Run JupyterLab on a remote server (via SSH)
- Convert a Jupyter notebook to a Python script

---

## 🖥️ Using Jupyter on Your Local Machine

First, activate your environment:

```bash
conda activate geocat
```

Then start JupyterLab (recommended):

```bash
jupyter lab
```

Or launch the classic Jupyter Notebook interface:

```bash
jupyter notebook
```

Your browser should open automatically. If not, visit the URL printed in the terminal (typically http://localhost:8888).

---

## 🌐 Using Jupyter on a Remote Server

This is useful when working on a high-performance computing (HPC) cluster or university server.

### 🔐 Step 1: SSH into the remote server

```bash
ssh your_username@your.server.address.edu
```

> Replace `your_username` and `your.server.address.edu` with the credentials provided to you.

### 🚀 Step 2: Launch Jupyter on the remote server

Activate your conda environment:

```bash
conda activate geocat
```

Start JupyterLab in the background:

```bash
nohup jupyter lab --no-browser --port=8888 --ip=0.0.0.0 > jupyter.log 2>&1 &
```

Or start Jupyter Notebook:

```bash
nohup jupyter notebook --no-browser --port=8888 --ip=0.0.0.0 > jupyter_notebook.log 2>&1 &
```

### 🧩 Step 3: Tunnel to the remote Jupyter server from your local machine

Open a new terminal on your local machine and run:

```bash
ssh -L 8888:localhost:8888 your_username@your.server.address.edu
```

Then visit the following URL in your web browser:

```
http://localhost:8888
```

> If a token is required, you can find it inside `jupyter.log` on the remote server.

---

## 🔁 Converting Jupyter Notebooks to Python Scripts

To convert a notebook (.ipynb) to a plain Python script:

```bash
jupyter nbconvert --to script my_notebook.ipynb
```

This will generate `my_notebook.py` in the same directory — useful for sharing, version control, or running as a batch script.

