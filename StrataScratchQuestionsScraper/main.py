from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    return webdriver.Chrome(options=chrome_options)


def scrape_question_data(url):
    driver = create_driver()
    driver.get(url)

    header = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.CSS_SELECTOR, '.QuestionMetadata__h1'))).text

    metadata_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.CSS_SELECTOR, '.QuestionMetadata__metadata')))

    company_name = metadata_element.find_element(By.CSS_SELECTOR, 'div').text
    difficulty = metadata_element.find_element(By.CSS_SELECTOR, '[class^="QuestionDifficulty--"]').text

    description = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.CSS_SELECTOR, '.QuestionMetadata__question'))).find_element(By.CSS_SELECTOR, 'p').text

    print(header)
    print(company_name, difficulty)
    print(description)
    print()

    driver.quit()


scrape_question_data("https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=3")
scrape_question_data("https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=3")
scrape_question_data("https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?code_type=3")
