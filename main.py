import pandas as pd
import matplotlib.pyplot as plt  # 수정: matplotlib.pyplot으로 변경

# Load dataset
ppl = pd.read_csv("HR.csv", index_col="EmployeeNumber", encoding="utf-8")

# Calculate statistics for Age
age_mean = ppl["Age"].mean()
age_median = ppl["Age"].median()
age_std = ppl["Age"].std()

# Plot histogram for Age
plt.figure(figsize=(8, 6))
plt.hist(ppl["Age"], bins=10, edgecolor="black")
plt.title("Average retirement age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Print statistics
print(f"Average retirement age is {round(age_mean, 1)}")
print(f"Median retirement age is {age_median}")
print(f"Standard Deveiation of retirement age is {age_std}")
