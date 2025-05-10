# Reading CSV Files

CSV (Comma-Separated Values) files are a common format for station observations, climate indices, or manually processed data. They are simple text files organized in rows and columns and can be read using the `pandas` library.

## 📥 Reading a CSV File

Here's how to read a CSV file using `pandas`:

```python
import pandas as pd

# Read a simple CSV file
df = pd.read_csv("../data/precip_timeseries.csv")

# Display the first few rows
print(df.head())
```

## 🧠 Tips

- Use `parse_dates=['date']` if your file includes timestamps.
- Use `index_col='date'` if you want to treat the date as the DataFrame index.
- Use `sep="\t"` or `delimiter=','` to adjust for tab-delimited or nonstandard formats.

CSV is ideal for small datasets and quick exploratory work.


