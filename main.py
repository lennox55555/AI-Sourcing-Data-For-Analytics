
import pandas as pd


def firstFiveRows(filePath):
    """
    Reads a CSV file and prints/returns the first 5 rows .

    Input/Param:
        path to the CSV file.

    Output/Returns:
        first 5 rows of the CSV file of a DataFrame.
    """
    df = pd.read_csv(filePath)
    print(df.head(5))
    return df.head(5)

def lastFiveRows(filePath):
    """
        Reads a CSV file and prints/returns the last 5 rows .

        Input/Param:
            path to the CSV file.

        Output/Returns:
            last 5 rows of the CSV file of a DataFrame.
        """
    df = pd.read_csv(filePath)
    print(df.tail(5))
    return df.tail(5)


if __name__ == "__main__":

    firstFiveRows('data/bitcoinPrices.csv')
    lastFiveRows('data/bitcoinPrices.csv')



