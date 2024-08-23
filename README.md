# **SWE Standard Practice AIPI 510**

## **Overview**
This project is designed to [briefly describe what your project does]. The main script reads a CSV file containing Bitcoin prices and prints the first five rows. Unit tests are provided to ensure the code functions as expected.

## **Prerequisites**
Before you begin, ensure you have the following installed on your machine:
- Python 3.x
- Git

## **Getting Started**

### **1. Clone the Repository**

To clone the repository from GitHub, open your terminal and run:


```bash
git clone https://github.com/lennox55555/AI-Sourcing-Data-For-Analytics.git
```


### **2. Navigate to the Project Directory**

Once you have cloned the repository or downloaded the ZIP file, navigate into the project directory:

```bash
cd AI-Sourcing-Data-For-Analytics
```

### **3. Set Up a Virtual Environment**

It is recommended to use a virtual environment to manage your dependencies. You can create and activate a virtual environment using the following commands:

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```
On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### **4. Install Dependencies**

After activating the virtual environment, install the necessary dependencies from the requirements.txt file:

```bash
pip install -r requirements.txt
```
### **5. Run the Python Script**

To run the main Python script, use the following command:

```bash
python main.py
```

### **6. Run Unit Tests**

To ensure everything is working correctly, you can run the unit tests using:

```bash
python -m unittest discover tests/
```
This command will discover and run all test files in the tests directory.
### **7. Deactivate the Virtual Environment**

After you're done working on the project, you can deactivate the virtual environment by running:

```bash
deactivate
```

### **8. Generate requirements.txt (Optional)**

If you make changes to the dependencies and want to update the requirements.txt file, you can generate it by running:

```bash
pip freeze > requirements.txt
```

## **Credits**
This project was made possible with the help of several valuable resources:

- SavvyCSV: Finding the perfect CSV file in seconds has never been easier! As a machine learning researcher, data analyst, and scientist, I used SavvyCSV to quickly locate relevant CSV files for this project.

- GPT Assistance: GPT-4 was instrumental in looking up documentation for unit testing and helping ensure that the testing practices used in this project were up to standard.

Special thanks to the developers and communities that contributed to the tools and libraries listed in the **requirements.txt file**, making this project possible.