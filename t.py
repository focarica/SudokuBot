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
actions = ActionChains(driver)
wait = WebDriverWait(driver,30)

# Close Cookie pop-up
wait.until(EC.element_to_be_clickable((By.ID,"agree_cookies"))).click()

def RemoveAlready(listWithNum:list ,numToRemove:list):
    for i in numToRemove:
        listWithNum.remove(i)
    
    return listWithNum

board = [
    [7,8,5,4,3,9,1,2,6],
    [6,1,2,8,7,5,3,4,9],
    [4,9,3,6,2,1,5,7,8],
    [8,5,7,9,4,3,2,6,1],
    [2,6,1,7,5,8,9,3,4],
    [9,3,4,1,6,2,7,8,5],
    [5,7,8,3,9,4,6,1,2],
    [1,2,6,5,8,7,4,9,3],
    [3,4,9,2,1,6,8,5,7]
]
# Find empty cells and use indexing to fill them up
for i in range(0,9):
    num = []
    xlist = board[i]
    print(f"Estamos no quadrante {i+1}")

    for j in range(0,9):
        group = bs.findAll('div', attrs={'class':'game-grid__group'})[i]
        ggcell = group.findAll('div', attrs={'class':'game-grid__cell'})[j]
        xsx = driver.find_elements_by_xpath(f"//div[@class='game-grid__group'][{i+1}]/div/*[name()='svg' and @class='']")

        tt = ggcell.find('svg')['class']
        
        if len(tt) > 0:
            numToAppend = ggcell.findChild('svg', attrs={'class','default'}).get_text().replace('\n','')
            num.append(int(numToAppend))
            print(f"Aqui ja tem o numero: {num}")
        else:
            continue

    for tsr in num:
        xlist.remove(tsr)

    print(f"Iremos colocar {xlist}")

    for x in range(len(xsx)):
        for aaa in xlist:
            try:
                actions.move_to_element(xsx[x]).click().send_keys(aaa).perform()
                x+=1
            except IndexError:
                break
        break