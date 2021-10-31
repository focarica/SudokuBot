from selenium import webdriver
from bs4 import BeautifulSoup

class WSelenium:
    def __init__(self):
        driver = webdriver.Chrome()
        driver.get("https://sudokutable.com")

WSelenium()