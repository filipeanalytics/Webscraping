Download ChromeDriver from https://chromedriver.chromium.org/
Save it in a folder that you can find easily.

In the Python code, update the path to where you saved your chrome plugin (chromedriver.exe)
#  Connect to Browser
DRIVER_PATH = "C:/Users/filip/Documents/PythonFiles/chromedriver"
browser = webdriver.Chrome(DRIVER_PATH)

Install these 2 Python libraries:
pip install selenium
pip install webdriver-manager

Update the paths to the csv file to the folder where you want to save your file.
PATH = "C:/Users/filip/Documents/PythonFiles/"
CSV_FILE = "UdemyCourses.csv"
