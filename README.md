This Python application scrapes Udemy website to collect 9 course details like course title and price. It does that by locating the search field and passing two searches (Python and Data Analytics), one at a time. Then it scrapes the courses content with the help of a user defined function and some further cleansing for the price. 

With a cleansed data, the application saves all course details in a Dataframe and then in a list of objects of a user defined Class (Course). Lastly the application prints all courses details and stores the Dataframe in a csv file.

Download ChromeDriver from https://chromedriver.chromium.org/
Save it in a folder that you can find easily.

In the Python code, update the path to where you saved your chrome plugin (chromedriver.exe)
DRIVER_PATH = "C:/Users/filip/Documents/PythonFiles/chromedriver"
browser = webdriver.Chrome(DRIVER_PATH)

Install these 2 Python libraries:
pip install selenium
pip install webdriver-manager

Update the paths to the csv file to the folder where you want to save your file.
PATH = "C:/Users/filip/Documents/PythonFiles/"
CSV_FILE = "UdemyCourses.csv"
