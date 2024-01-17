from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def scrape_question_name(url):
    driver = webdriver.Chrome()
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    class_name = 'QuestionMetadata__h1'
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))

    question_name = element.text
    print("Question Name:", question_name)

    driver.quit()


scrape_question_name("https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=3")
