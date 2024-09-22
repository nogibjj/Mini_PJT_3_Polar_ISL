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
