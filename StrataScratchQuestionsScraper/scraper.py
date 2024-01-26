from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class Scraper:
    def __init__(self, is_headless):
        self.driver = self.create_driver(is_headless)

    def create_driver(self, is_headless):
        options = Options()

        if is_headless:
            options.add_argument('--headless')

        chrome_driver = webdriver.Chrome(options=options)

        chrome_driver.set_window_size(1920, 1080)
        return chrome_driver

    def authenticate(self, email, password):
        self.driver.get('https://www.stratascratch.com/')

        login_link = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.LINK_TEXT, 'Login')))
        login_link.click()

        email_input = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.NAME, 'username')))
        email_input.send_keys(email)

        password_input = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.NAME, 'password')))
        password_input.send_keys(password)

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CLASS_NAME, "AuthFormButton"))).click()

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CLASS_NAME, "HomeHero-module--titleBig--bc06d")))

    def scrape_question(self, url):
        self.driver.get(url)
        description = self.scrape_question_description()
        tables = self.scrape_question_tables()

        return self.Question(description, tables)

    def scrape_question_description(self):
        name = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, '.QuestionMetadata__h1'))).text

        metadata_element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, '.QuestionMetadata__metadata')))

        company = metadata_element.find_element(By.CSS_SELECTOR, 'div').text
        difficulty = metadata_element.find_element(By.CSS_SELECTOR, '[class^="QuestionDifficulty--"]').text

        description = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, '.QuestionMetadata__question'))).find_element(By.CSS_SELECTOR, 'p').text

        question_description = self.Description(name, company, difficulty, description)

        return question_description

    def scrape_question_tables(self):
        names_elements = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located(
            (By.CLASS_NAME, "QuestionTables__table-name")))

        columns_elements = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located(
            (By.CLASS_NAME, "DatasetTableTypes__container")))

        tables = []

        for i in range(0, len(names_elements)):
            name = names_elements[i].text
            columns = self.html_element_to_table_columns(columns_elements[i])

            table = self.Table(name, columns)
            tables.append(table)

        return tables

    def html_element_to_table_columns(self, element):
        span_elements = element.find_elements(By.CSS_SELECTOR, 'span')

        columns = {}

        for i in range(0, len(span_elements), 2):
            key = span_elements[i].text
            key = key[:-1]

            value = span_elements[i + 1].text
            columns[key] = value

        return columns

    def quit_driver(self):
        self.driver.quit()

    class Description:
        def __init__(self, name, company, difficulty, description):
            self.name = name
            self.company = company
            self.difficulty = difficulty
            self.description = description

    class Table:
        def __init__(self, name, columns):
            self.name = name
            self.columns = columns

        def display_columns(self):
            for column_name, column_type in self.columns.items():
                print(f"  {column_name}: {column_type}")

    class Question:
        def __init__(self, description, tables):
            self.description = description
            self.tables = tables

        def display(self):
            print()
            print(f"-----{self.description.name}-----")
            print(f"{self.description.company}"
                  f"{' ' * (len(self.description.name) + 10 - len(self.description.company) - len(self.description.difficulty))}"
                  f"{self.description.difficulty}")

            for table in self.tables:
                print()
                print(table.name)
                table.display_columns()
