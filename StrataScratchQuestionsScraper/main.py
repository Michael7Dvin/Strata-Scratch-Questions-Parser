from getpass import getpass

from scraper import Scraper

email = 'idewishortcut@gmail.com'
password = getpass('Password: ')

scraper = Scraper(False)

scraper.scrape_question("https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=3")
#scrape_question("https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=3")
#scrape_question("https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?code_type=3")

scraper.quit_driver()
