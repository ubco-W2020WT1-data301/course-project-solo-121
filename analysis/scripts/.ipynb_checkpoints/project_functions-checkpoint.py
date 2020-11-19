import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_profiling

def load_and_process(path_to_csv):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv("../../data/raw/netflix_titles.csv")
          .rename(columns={"listed_in": "categories"})
          .dropna()
          # etc...
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .drop(['description'], axis=1)
      )

    # Make sure to return the latest dataframe

    return df2 
