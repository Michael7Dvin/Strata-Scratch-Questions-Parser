from getpass import getpass

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def create_driver(is_headless):
    options = Options()

    if is_headless:
        options.add_argument('--headless')

    chrome_driver = webdriver.Chrome(options=options)

    chrome_driver.set_window_size(1920, 1080)
    return chrome_driver


def authenticate():
    driver.get('https://www.stratascratch.com/')

    login_link = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
        (By.LINK_TEXT, 'Login')))
    login_link.click()

    email_input = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
        (By.NAME, 'username')))
    email_input.send_keys(email)

    email_input = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
        (By.NAME, 'password')))
    email_input.send_keys(password)

    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
        (By.CLASS_NAME, "AuthFormButton"))).click()

    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
        (By.CLASS_NAME, "HomeHero-module--titleBig--bc06d")))


def scrape_question(url):
    driver.get(url)
    scrape_question_description()
    scrape_question_tables()

def scrape_question_description():
    header = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, '.QuestionMetadata__h1'))).text

    metadata_element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, '.QuestionMetadata__metadata')))

    company_name = metadata_element.find_element(By.CSS_SELECTOR, 'div').text
    difficulty = metadata_element.find_element(By.CSS_SELECTOR, '[class^="QuestionDifficulty--"]').text

    description = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, '.QuestionMetadata__question'))).find_element(By.CSS_SELECTOR, 'p').text

    print(header)
    print(company_name, difficulty)
    print(description)
    print()


def scrape_question_tables():
    tables_names_elements = WebDriverWait(driver, 10).until(expected_conditions.presence_of_all_elements_located(
        (By.CLASS_NAME, "QuestionTables__table-name")))

    tables_columns_elements = WebDriverWait(driver, 10).until(expected_conditions.presence_of_all_elements_located(
        (By.CLASS_NAME, "DatasetTableTypes__container")))

    tables = []

    for i in range(0, len(tables_names_elements)):
        name = tables_names_elements[i].text
        columns = html_element_to_table_columns(tables_columns_elements[i])

        table = Table(name, columns)
        tables.append(table)

    for table in tables:
        table.display()


def html_element_to_table_columns(element):
    span_elements = element.find_elements(By.CSS_SELECTOR, 'span')

    columns = {}

    for i in range(0, len(span_elements), 2):
        key = span_elements[i].text
        key = key[:-1]

        value = span_elements[i + 1].text
        columns[key] = value

    return columns


class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns

    def display(self):
        print(f"Name: {self.name}")
        print("Columns:")
        for column_name, column_type in self.columns.items():
            print(f"  {column_name}: {column_type}")


email = 'idewishortcut@gmail.com'
password = getpass('Password: ')

driver = create_driver(True)

authenticate()

scrape_question("https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=3")
#scrape_question("https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=3")
#scrape_question("https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?code_type=3")

driver.quit()
