import pandas as pd
import polars as pl
import time

# Load dataset (Assume HR.csv is the dataset)
csv_file = "HR.csv"

# Measure time for Pandas
start_time = time.time()
ppl_pandas = pd.read_csv(csv_file)
age_mean_pandas = ppl_pandas["Age"].mean()
age_median_pandas = ppl_pandas["Age"].median()
age_std_pandas = ppl_pandas["Age"].std()
end_time = time.time()
pandas_time = end_time - start_time

# Measure time for Polars
start_time = time.time()
ppl_polars = pl.read_csv(csv_file)
age_mean_polars = ppl_polars.select(pl.col("Age").mean()).item()
age_median_polars = ppl_polars.select(pl.col("Age").median()).item()
age_std_polars = ppl_polars.select(pl.col("Age").std()).item()
end_time = time.time()
polars_time = end_time - start_time

# Print performance results
print(f"Pandas processing time: {pandas_time:.4f} seconds")
print(f"Polars processing time: {polars_time:.4f} seconds")

if pandas_time > polars_time:
    speed_improvement1 = (1 - (polars_time / pandas_time)) * 100
    print(f"Polars processing is {speed_improvement1:.2f}% faster than Pandas")
else:
    speed_improvement2 = (1 - (pandas_time / polars_time)) * 100
    print(f"Pandas processing is {speed_improvement2:.2f}% faster than Polars")
