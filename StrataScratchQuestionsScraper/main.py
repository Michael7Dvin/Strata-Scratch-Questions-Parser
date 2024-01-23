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


def scrape_question_description(url):
    driver.get(url)

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


email = 'idewishortcut@gmail.com'
password = getpass('Password: ')

driver = create_driver(True)

authenticate()

scrape_question_description("https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=3")
scrape_question_description("https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=3")
scrape_question_description("https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?code_type=3")

driver.quit()
