from selenium import webdriver
from bs4 import BeautifulSoup

LINK = "https://sudokutable.com"
HEADER = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/80.0.4170.72'
}

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)

class WSelenium:
    def __init__(self):
        driver = webdriver.Chrome(options=options)

        driver.get(LINK)
        driver.set_window_size(1110, 768)

        driver.find_element_by_id('agree_cookies').click()
        driver.find_element_by_class_name('dropdown').click()
        driver.find_element_by_xpath('//*[@id="difficulty"]/ul/li[4]').click()

        self.url = driver.page_source

    def BeautifulSoup(self):
        bs = BeautifulSoup(self.url, 'html.parser')
        return bs