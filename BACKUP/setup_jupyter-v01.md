# Jupyter Notebook 

This section explains how to run JupyterLab or Notebook on a remote server and access it from your local computer.

## 🔐 Step 1: SSH to Remote Server

```bash
    ssh your_username@your.server.address.edu
```

Replace `your_username` and `your.server.address.edu` with your actual credentials.

## 🚀 Step 2: Start Jupyter Server

Activate your environment:

```bash
    conda activate geocat
```

Then choose either JupyterLab or Notebook:

```bash
    nohup jupyter lab --no-browser --port=8888 --ip=0.0.0.0 > jupyter.log 2>&1 &
```
    # or

```bash
    nohup jupyter notebook --no-browser --port=8888 --ip=0.0.0.0 > jupyter_notebook.log 2>&1 &
```

## 🖥️ Step 3: Tunnel from Your Local Machine

On your Mac or local terminal:

```bash
    ssh -L 8888:localhost:8888 your_username@your.server.address.edu
```

Then open:

```
    http://localhost:8888
```

If prompted for a token, check the `jupyter.log` file on the server.

## 🔁 Optional: Convert Notebook to Script

To convert `.ipynb` to `.py`:

```bash
    jupyter nbconvert --to script my_notebook.ipynb
```

