from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.ioselite.com/search/?q=netmarble&quick=1")

hacktools = driver.find_elements_by_class_name("ipsContained")

for index, hacktool in enumerate(hacktools):
    # 뒤로가기 버튼 하나 만든 후 광고 빼고 찾기(구글 셀레니움에서 지우기 활용?)
    ActionChains(driver).key_down(Keys.CONTROL).click(hacktool).perform()
    if index == 0:
        driver.back()
        hacktool.click()

    time.sleep(3)
