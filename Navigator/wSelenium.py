from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://sudokutable.com')
driver.set_window_size(1110, 768)