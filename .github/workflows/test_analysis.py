import pandas as pd

def test_dataset_not_empty():
    df = pd.read_csv("netflix_titles.csv")
    assert len(df) > 0
