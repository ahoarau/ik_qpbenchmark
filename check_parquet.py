import pandas as pd

try:
    df = pd.read_parquet("data/ik_qpbenchmark.parquet", engine="pyarrow")
    print("Columns:", df.columns)
    print("Index:", df.index)
    print("First 5 rows index:", df.index[:5])
    if 'name' in df.columns:
        print("First 5 names:", df['name'].head())
except Exception as e:
    print("Error:", e)
