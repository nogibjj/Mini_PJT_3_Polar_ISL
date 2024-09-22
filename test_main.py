import polars as pl
from main import ppl, age_mean, age_median, age_std


def test_age_statistics():
    expected_mean = ppl.select(pl.col("Age").mean()).item() 
    expected_median = ppl.select(pl.col("Age").median()).item()
    expected_std = ppl.select(pl.col("Age").std()).item()

    assert round(age_mean, 1) == round(
        expected_mean, 1
    ), f"Expected mean: {expected_mean}, but got: {age_mean}"
    assert (
        age_median == expected_median
    ), f"Expected median: {expected_median}, but got: {age_median}"
    assert age_std == expected_std, f"Expected std: {expected_std}, but got: {age_std}"

    print("Test_succeed")


if __name__ == "__main__":
    test_age_statistics()
