# Virtual Environment with Conda

A virtual environment keeps your tools and packages isolated, ensuring your analysis is reproducible.

---

## ✅ Common Commands

### 🆕 Create a new environment

```bash
conda create -n geocat -c conda-forge geocat-comp geocat-viz
```

### 🚀 Activate the environment

```bash
conda activate geocat
```

### 📴 Deactivate the current environment

```bash
conda deactivate
```

---

## 📋 Manage Environments

### 🔍 List all environments

```bash
conda env list
```

This shows all existing environments and highlights the currently active one.

### ❌ Remove an environment

```bash
conda env remove -n geocat
```

Make sure you deactivate the environment before removing it.

---

## 💡 Tips

- Use descriptive environment names based on your project (e.g., `pyclm101`, `gcm_eval`).
- You can export an environment to a YAML file:

```bash
conda env export > environment.yml
```

- To recreate an environment from a YAML file:

```bash
conda env create -f environment.yml
```

This is useful for sharing your setup with collaborators or for reproducibility.

