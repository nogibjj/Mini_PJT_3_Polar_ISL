import polars as pl
import matplotlib.pyplot as plt

# Load dataset using Polars
ppl = pl.read_csv("HR.csv")

# Calculate statistics for Age
full_desc = ppl.describe()
age_mean = ppl.select(pl.col("Age").mean()).item()
age_median = ppl.select(pl.col("Age").median()).item()
age_std = ppl.select(pl.col("Age").std()).item()

# Convert Polars dataframe to a list for plotting
ages = ppl.select("Age").to_series().to_list()

# Plot histogram for Age
plt.figure(figsize=(8, 6))
plt.hist(ages, bins=10, edgecolor="black")
plt.title("Average retirement age of company A")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Print statistics
print(f"Average retirement age of company A is {round(age_mean, 1)}")
print(f"Median retirement age of company A is {age_median}")
print(f"Standard Deviation of retirement of company A age is {age_std}")
print(full_desc)

# import pandas as pd
# import polars as pl
# import time

# # Load dataset (Assume HR.csv is the dataset)
# csv_file = "HR.csv"

# # Measure time for Pandas
# start_time = time.time()
# ppl_pandas = pd.read_csv(csv_file)
# age_mean_pandas = ppl_pandas["Age"].mean()
# age_median_pandas = ppl_pandas["Age"].median()
# age_std_pandas = ppl_pandas["Age"].std()
# end_time = time.time()
# pandas_time = end_time - start_time

# # Measure time for Polars
# start_time = time.time()
# ppl_polars = pl.read_csv(csv_file)
# age_mean_polars = ppl_polars.select(pl.col("Age").mean()).item()
# age_median_polars = ppl_polars.select(pl.col("Age").median()).item()
# age_std_polars = ppl_polars.select(pl.col("Age").std()).item()
# end_time = time.time()
# polars_time = end_time - start_time

# # Print performance results
# print(f"Pandas processing time: {pandas_time:.4f} seconds")
# print(f"Polars processing time: {polars_time:.4f} seconds")


# import pandas as pd
# import matplotlib.pyplot as plt

# # Load dataset
# ppl = pd.read_csv("HR.csv", index_col="EmployeeNumber", encoding="utf-8")

# # Calculate statistics for Age
# full_desc = ppl.describe()
# age_mean = ppl["Age"].mean()
# age_median = ppl["Age"].median()
# age_std = ppl["Age"].std()

# # Plot histogram for Age
# plt.figure(figsize=(8, 6))
# plt.hist(ppl["Age"], bins=10, edgecolor="black")
# plt.title("Average retirement age")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

# # Print statistics
# print(f"Average retirement age is {round(age_mean, 1)}")
# print(f"Median retirement age is {age_median}")
# print(f"Standard Deveiation of retirement age is {age_std}")
# print(full_desc)
