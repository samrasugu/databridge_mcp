import pandas as pd
# read the CSV
df = pd.read_csv("data/sample.csv")
# save as Parquet
df.to_parquet("data/sample.parquet", index=False)