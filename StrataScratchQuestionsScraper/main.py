from getpass import getpass

import db_operations
from scraper import Scraper

email = 'idewishortcut@gmail.com'
password = getpass('Password: ')

scraper = Scraper(False)

scraper.authenticate(email, password)


urls = \
    [
        'https://platform.stratascratch.com/coding/10159-ranking-most-active-guests?code_type=1',
        'https://platform.stratascratch.com/coding/10156-number-of-units-per-nationality?code_type=1',
        'https://platform.stratascratch.com/coding/10303-top-percentile-fraud?code_type=1',
        'https://platform.stratascratch.com/coding/10300-premium-vs-freemium?code_type=1',
        'https://platform.stratascratch.com/coding/10299-finding-updated-records?code_type=1',
    ]

for url in urls:
    question = scraper.scrape_question(url)
    question.display()
    db_operations.add_question_to_db(question)

scraper.quit_driver()
db_operations.close_connection()
