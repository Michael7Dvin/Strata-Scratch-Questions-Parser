from getpass import getpass

from scraper import Scraper

email = 'idewishortcut@gmail.com'
password = getpass('Password: ')

scraper = Scraper(True)

scraper.authenticate(email, password)

question1 = scraper.scrape_question("https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=3")
#scrape_question("https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=3")
#scrape_question("https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?code_type=3")

question1.display()

scraper.quit_driver()
