import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def scrape(amount):
    def write_to_file(name, content):
        f = open("input/" + name, "w")
        f.write(content)
        f.close()

    def create_filename(input_text):
        parts = input_text.split(' ')[1].replace('.', '_').removesuffix('_').split('_')
        return parts[1] + '_' + parts[0] + '.html'

    options = Options()

    options.add_argument('--no-sandbox')
    options.headless = True

    driver = webdriver.Chrome(options=options)

    driver.get('https://www.film.at/kinoprogramm/wien')

    select = Select(driver.find_element(By.ID, 'input0'))

    upper_bound = amount
    if len(select.options) - 1 < upper_bound:
        upper_bound = len(select.options) - 1

    for index in range(0, upper_bound):
        select.select_by_index(index)
        time.sleep(1)
        filename = create_filename(select.options[index].text)
        write_to_file(filename, driver.page_source)
        print('Scraped ' + filename)


