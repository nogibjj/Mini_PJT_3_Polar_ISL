import pandas as pd
import matplotlib.pyplot as plt  
from main import ppl, age_mean, age_median, age_std  


def test_age_statistics():
    """
    Test to validate age statistics (mean, median, std).
    """
    expected_mean = ppl["Age"].mean()
    expected_median = ppl["Age"].median()
    expected_std = ppl["Age"].std()

    assert round(age_mean, 1) == round(
        expected_mean, 1
    ), f"Expected mean: {expected_mean}, but got: {age_mean}"
    assert (
        age_median == expected_median
    ), f"Expected median: {expected_median}, but got: {age_median}"
    assert age_std == expected_std, f"Expected std: {expected_std}, but got: {age_std}"

    print("All age statistics tests passed successfully.")


def test_age_histogram():
    """
    Test to visually validate the histogram of age distribution.
    """
    try:
        plt.figure(figsize=(8, 6))
        plt.hist(ppl["Age"], bins=10, edgecolor="black")
        plt.title("Average retirement age")
        plt.xlabel("Age")
        plt.ylabel("Frequency")
        plt.show()
        print("Histogram test: Success (Check visually)")
    except Exception as e:
        print(f"Histogram test failed: {e}")


if __name__ == "__main__":
    test_age_statistics()
    test_age_histogram()
