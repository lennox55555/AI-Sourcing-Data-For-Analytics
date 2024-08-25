# because these files are in python standard library, we don't include in requirements.txt
import unittest
import time
from main import firstFiveRows
import os
import pandas as pd


class TestMain(unittest.TestCase):

    def setUp(self):
        # ensure the tests directory exists use os to access file struc
        if not os.path.exists('tests'):
            os.makedirs('tests')

        # set up a sample df to use in testing
        self.sample_data = {
            'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
            'Price': [40000, 41000, 42000, 43000, 44000]
        }
        # convert the sample data into a pandas DataFrame
        self.df = pd.DataFrame(self.sample_data)

        # write the sample data to a CSV file
        """
        This test function writes to a CSV file and then deletes it after the test.

        why is this good practice?:
        
        writing to and deleting a CSV file in a test simulates real world file operations, 
        ensuring the code correctly handles file I/O. In this case we delete it to not clutter the file path. 
        """
        self.df.to_csv('tests/sample_bitcoinPrices.csv', index=False)

    def tearDown(self):
        # clean up the test CSV file after the tests run
        os.remove('tests/sample_bitcoinPrices.csv')

    def test_read_and_print_first_five_rows(self):
        # start the timer
        start_time = time.time()

        try:
            # call the function with the test CSV file
            firstFiveRows('tests/sample_bitcoinPrices.csv')

            # if test passed
            print("Test passed")
        except Exception as e:
            # if test failed
            print(f"Test failed: {e}")

        # stop the timer and calculate the elapsed time using start
        elapsed_time = time.time() - start_time
        # formatted to 4 decimal places using an fstring
        print(f"Elapsed time: {elapsed_time:.4f} seconds")


# this is the only script ran
if __name__ == '__main__':
    unittest.main()
