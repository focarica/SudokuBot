from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver
from bs4 import BeautifulSoup

LINK = "https://sudokutable.com"
HEADER = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/80.0.4170.72'
}

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

class navigator:
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.actions =ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver,30)


        self.driver.get(LINK)
        self.driver.set_window_size(1110, 768)

        self.wait.until(EC.element_to_be_clickable((By.ID, "agree_cookies")))
        self.driver.find_element_by_class_name('dropdown').click()
        self.driver.find_element_by_xpath('//*[@id="difficulty"]/ul/li[4]').click()

        self.url = self.driver.page_source

    def BeautifulSoup(self):
        bs = BeautifulSoup(self.url, 'html.parser')
        return bs
    
    def GetDriver(self):
        return self.driver
    

    def FillCells(self, ListNum:list):
        bs = self.BeautifulSoup()
        driver = self.GetDriver()
        #All boxs
        for box in range(0,9): 
            alreadyHere = []
            resultList = ListNum[box]
            
            print(resultList)
            for cell in range(0,9):
                group = bs.findAll('div', attrs={'class':'game-grid__group'})[box]
                ggCell = group.findAll('div', attrs={'class':'game-grid__cell'})[cell]
                allCell = driver.find_elements_by_xpath(f"//div[@class='game-grid__group'][{box+1}]/div/*[name()='svg' and @class='']")

                cellEmpty = ggCell.find('svg')['class']

                if len(cellEmpty) > 0:
                    numToAppend = ggCell.find('svg', attrs={'class','default'}).get_text().replace('\n','')
                    alreadyHere.append(int(numToAppend))
                else:
                    continue
            
            for i in alreadyHere:
                resultList.remove(i)

            #Move to every cell and fill
            for box in range(len(allCell)):
                for num in resultList:
                    try:
                        self.actions.move_to_element(allCell[box]).click().send_keys(num).perform()
                        box+=1
                    except IndexError:
                        break
                break