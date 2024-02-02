from getpass import getpass

import db_operations
from scraper import Scraper

email = 'idewishortcut@gmail.com'
password = getpass('Password: ')

scraper = Scraper(False)

scraper.authenticate(email, password)


urls = \
    [
        'https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=3',
        # 'https://platform.stratascratch.com/coding/10356-finding-doctors?code_type=3',
        # 'https://platform.stratascratch.com/coding/10355-employees-with-same-birth-month?code_type=3',
        # 'https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=3',
        # 'https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=3',
        # 'https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code_type=3',
    ]

for url in urls:
    question = scraper.scrape_question(url)
    question.display()
    db_operations.add_question_to_db(question)

scraper.quit_driver()
db_operations.close_connection()
