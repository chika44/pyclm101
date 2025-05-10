# Auto-Naming Output Figure Files

When generating visualizations programmatically, it's useful to automatically name the output image file to match the script or notebook that created it. This improves reproducibility and organization of output files.

## 📁 Example: Generate a PNG with the Same Name as the Script or Notebook

You can use the following function to automatically detect the filename of the current Python script or Jupyter notebook:

```python
import os
import ipynbname

# Auto-detect Output Figure Filename
def get_filename():
    try:
        # If __file__ is defined, we're running a .py script.
        filename = os.path.splitext(os.path.basename(__file__))[0]
    except NameError:
        # If __file__ is not defined, we're in a Jupyter Notebook.
        nb_path = ipynbname.path()  # Get the notebook path
        filename = os.path.splitext(os.path.basename(str(nb_path)))[0]
    return filename

fnFIG = get_filename() + ".png"
print(f"Figure filename: {fnFIG}")
```

This ensures the figure output matches the file that generated it.

## 💾 Save the Figure

Once your plot is ready, use `plt.savefig()` with the auto-generated filename:

```python
plt.tight_layout()
plt.savefig(fnFIG, dpi=300, bbox_inches="tight")
plt.show()
```

This workflow helps you keep output files consistent and reduces manual file naming errors.
