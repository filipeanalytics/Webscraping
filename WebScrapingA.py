import time  # to use sleep function to allow website to load
from selenium import webdriver  # to connect to a browser and access an URL
from bs4 import BeautifulSoup  # to remove HTML tags from HTML content
from selenium.webdriver.common.keys import Keys  # so I can press the Enter Key in the search fields
import pandas as pd


class Course:
    courseTitle = ""
    courseDescription = ""
    courseInstructor = ""
    courseRating = ""
    courseTotalRates = ""
    courseLength = ""
    courseNumberOfLectures = ""
    courseLevel = ""
    coursePrice = ""

    def __init__(self, courseTitle, courseDescription, courseInstructor, courseRating,
                 courseTotalRates, courseLength, courseNumberOfLectures, courseLevel, coursePrice):
        self.courseTitle = courseTitle
        self.courseDescription = courseDescription
        self.courseInstructor = courseInstructor
        self.courseRating = courseRating

        self.courseTotalRates = courseTotalRates
        self.courseLength = courseLength
        self.courseNumberOfLectures = courseNumberOfLectures
        self.courseLevel = courseLevel
        self.coursePrice = coursePrice

    def showDetails(self):
        print("Title:       " + self.courseTitle)
        print("Description: " + self.courseDescription)
        print("Instructor:  " + self.courseInstructor)
        print("Rating:      " + self.courseRating)
        print("Rates:       " + self.courseTotalRates)
        print("Length:      " + self.courseLength)
        print("Lectures:    " + self.courseNumberOfLectures)
        print("Level:       " + self.courseLevel)
        print("Price:       " + self.coursePrice)
        print("")

def HTMLtoText(HTMLelement):
    textContent = HTMLelement.get_attribute('innerHTML')
    # Beautiful soup removes HTML tags from content, if it exists.
    soup = BeautifulSoup(textContent, features="lxml")
    rawString = soup.get_text().strip()  # Leading and trailing whitespaces are removed
    return rawString

#  Connect to Browser
DRIVER_PATH = "C:/Users/filip/Documents/PythonFiles/chromedriver"
browser = webdriver.Chrome(DRIVER_PATH)

URL = "https://www.udemy.com"
#  Access website
browser.get(URL)

# Give the browser time to load all content.
time.sleep(5)

# searches to be passed to search field
SEARCH_TERM = ["Python", "Data Analytics"]

courseList = []

# Create dataframe with named columns.
df = pd.DataFrame(columns=['courseTitle', 'courseDescription', 'courseInstructor', 'courseRating', 'courseTotalRates',
                           'courseLength', 'courseNumberOfLectures', 'courseLevel', 'coursePrice'])

# Navigate through 2 pages
for i in range(0,2):

    # Locate search field
    search = browser.find_element_by_css_selector(".js-header-search-field")

    # Clear search field
    search.clear()

    # Pass search text to search field
    search.send_keys(SEARCH_TERM[i])

    # Press enter key after typing search text
    search.send_keys(Keys.RETURN)

    # Give the browser time to load all content.
    time.sleep(3)

    # content = browser.find_elements_by_css_selector(".course-card--has-price-text--1Ikr0")
    # Couldn't use like this as resulting text had no spaces, so couldn't split contents dynamically.

    # Store website content.
    courseTitleLIST = browser.find_elements_by_css_selector\
        (".popper--popper-hover--4YJ5J .course-card--course-title--2f7tE")
    courseDescriptionLIST = browser.find_elements_by_css_selector\
        (".course-card--course-headline--yIrRk")
    courseInstructorLIST = browser.find_elements_by_css_selector\
        (".popper--popper-hover--4YJ5J .course-card--instructor-list--lIA4f")
    courseRatingLIST = browser.find_elements_by_css_selector\
        (".popper--popper-hover--4YJ5J .star-rating--rating-number--3lVe8")
    courseTotalRatesLIST = browser.find_elements_by_css_selector\
        (".popper--popper-hover--4YJ5J .course-card--reviews-text--12UpL")
    courseLengthLIST = browser.find_elements_by_css_selector\
        (".course-card--large--1BVxY .course-card--row--1OMjg:nth-child(1)")
    courseNumberOfLecturesLIST = browser.find_elements_by_css_selector\
        (".course-card--large--1BVxY .course-card--row--1OMjg:nth-child(2)")
    courseLevelLIST = browser.find_elements_by_css_selector\
        (".course-card--large--1BVxY .course-card--row--1OMjg~ .course-card--row--1OMjg+ .course-card--row--1OMjg")
    coursePriceLIST = browser.find_elements_by_css_selector\
        (".course-card--price-text-container--2sb8G")

    # Read and store each course details in a courseLIST.
    for j in range(len(courseTitleLIST)):

        title = HTMLtoText(courseTitleLIST[j])
        description = HTMLtoText(courseDescriptionLIST[j])
        instructor = HTMLtoText(courseInstructorLIST[j])
        rating = HTMLtoText(courseRatingLIST[j])
        totalRates = HTMLtoText(courseTotalRatesLIST[j])
        length = HTMLtoText(courseLengthLIST[j])
        numberOfLect = HTMLtoText(courseNumberOfLecturesLIST[j])

        try:
            level = HTMLtoText(courseLevelLIST[j])
        except Exception as e:
            level = "N/A"

        # price needs further manipulation:
        # treating for when price is null
        try:
            price = HTMLtoText(coursePriceLIST[j])
            startIndex = price.index('R$')  # starts reading from this point
            cutOffIndex = price.index('O')  # cuts the string at [O]riginal Price
            price = price[startIndex:cutOffIndex]
        except Exception as e:
            # print("Price not available")
            price = "Price not available"

        # adding one course info into a dictionary
        courseDict = {'courseTitle': title, 'courseDescription': description,
                      'courseInstructor': instructor, 'courseRating': rating,
                      'courseTotalRates': totalRates, 'courseLength': length,
                      'courseNumberOfLectures': numberOfLect, 'courseLevel': level,
                      'coursePrice': price}
        # appending course by course into a DataFrame
        df = df.append(courseDict, ignore_index=True)

        # Creating course objects
        course = Course(title, description, instructor,
                        rating,totalRates, length,
                        numberOfLect,level, price)

        # appending course by course into an Object's List.
        courseList.append(course)

# Print all courses found
for c in courseList:
    c.showDetails()

# Save DataFrame into a CSV File
PATH = "C:/Users/filip/Documents/PythonFiles/"
CSV_FILE = "UdemyCourses.csv"
df.to_csv(PATH+CSV_FILE, sep=',')

# Set up DataFrame printing options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option("display.colheader_justify","left")

# Read CSV file and print first and last two rows
readCsv = pd.read_csv(PATH+CSV_FILE, sep=',')
print("First two rows: \n", readCsv.head(2), "\n\nLast two rows: \n", readCsv.tail(2))






