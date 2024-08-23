import unittest
import time
from main import firstFiveRows
import os
import pandas as pd


class TestMain(unittest.TestCase):

    def setUp(self):
        # Ensure the 'tests' directory exists
        if not os.path.exists('tests'):
            os.makedirs('tests')

        # Set up a sample DataFrame to use in testing
        self.sample_data = {
            'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
            'Price': [40000, 41000, 42000, 43000, 44000]
        }
        self.df = pd.DataFrame(self.sample_data)

        # Write the sample data to a CSV file
        self.df.to_csv('tests/sample_bitcoinPrices.csv', index=False)

    def tearDown(self):
        # Clean up the test CSV file after the tests run
        os.remove('tests/sample_bitcoinPrices.csv')

    def test_read_and_print_first_five_rows(self):
        # Start the timer
        start_time = time.time()

        try:
            # Call the function with the test CSV file
            firstFiveRows('tests/sample_bitcoinPrices.csv')

            # Test passed
            print("Test passed")
        except Exception as e:
            # Test failed
            print(f"Test failed: {e}")

        # Stop the timer and calculate the elapsed time
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {elapsed_time:.4f} seconds")


if __name__ == '__main__':
    unittest.main()
