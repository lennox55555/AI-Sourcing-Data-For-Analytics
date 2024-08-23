
import pandas as pd


def firstFiveRows(file_path):
    """
    Reads a CSV file and returns the first 5 rows.

    Input/Param:
    - file_path (str): The path to the CSV file.

    Returns:
    - pd.DataFrame: The first 5 rows of the CSV file as a DataFrame.
    """
    df = pd.read_csv(file_path)
    print(df.head(5))
    return df.head(5)


if __name__ == "__main__":

    firstFiveRows('data/bitcoinPrices.csv')



