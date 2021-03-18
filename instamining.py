import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(ChromeDriverManager().install())

INSTAGRAM_ID = "stonerl12"
INSTAGRAM_PW = "clzkseptM1!"

main_hashtag = "dog"

browser.get(f"https://www.instagram.com/accounts/login/")

time.sleep(5)

browser.find_element_by_name("username").send_keys(INSTAGRAM_ID)
browser.find_element_by_name("password").send_keys(INSTAGRAM_PW)
browser.find_elements_by_class_name("sqdOP")[1].send_keys(Keys.ENTER)

############ 로그인 완료 #######################

search_bar = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "XTCLo"))
)
search_bar.send_keys("#dog")

hashtags_list = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "fuqBx"))
)
hashtags = hashtags_list.find_elements_by_class_name("-qQT3")

for hashtag in hashtags:
    hashtag = hashtag.get_attribute("href")
    browser.execute_script(f"window.open('{hashtag}')")
    time.sleep(5)

browser.quit()
