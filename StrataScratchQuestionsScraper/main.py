from getpass import getpass

import db_operations
from scraper import Scraper

email = 'idewishortcut@gmail.com'
password = getpass('Password: ')

scraper = Scraper(False)

scraper.authenticate(email, password)

question1 = scraper.scrape_question\
    ("https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=3")

question1.display()

db_operations.add_question_to_db(question1)

scraper.quit_driver()
db_operations.close_connection()
