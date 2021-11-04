# Imports required:
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://sudokutable.com/")
driver.maximize_window()
link = driver.page_source

bs = BeautifulSoup(link, 'html.parser')
actions =ActionChains(driver)
wait = WebDriverWait(driver,30)

# Close Cookie pop-up
wait.until(EC.element_to_be_clickable((By.ID,"agree_cookies"))).click()

# Find empty cells and use indexing to fill them up
for i in range(0,9):
    num = []
    xlist = [str(i) for i in range(1,10)]
    print(f"Estamos no quadrante {i+1}")

    for j in range(0,9):
        group = bs.findAll('div', attrs={'class':'game-grid__group'})[i]
        ggcell = group.findChildren('div', attrs={'class':'game-grid__cell'})[j]
        cell = driver.find_elements_by_xpath(f"//div[@class='game-grid__group'][{i+1}]/div/*[name()='svg' and @class='']")

        tt = ggcell.find('svg')['class']

        if len(tt) > 0:
            num.append(ggcell.findChild('svg', attrs={'class','default'}).get_text().replace('\n',''))
            print(f"Aqui ja tem o numero: {num}")
        else:
            print("Ta livre irmao")

    for tst in num:
        xlist.remove(tst)

    print(f"Iremos colocar {xlist}")

    for x in range(len(cell)):
        for aaa in xlist:
            try:
                actions.move_to_element(cell[x]).click().send_keys(aaa).perform()
                x+=1
            except IndexError:
                break
        break