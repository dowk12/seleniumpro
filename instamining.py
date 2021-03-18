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


def wait_for(locator):
    return WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator))


browser.get(f"https://www.instagram.com/accounts/login/")

time.sleep(5)

browser.find_element_by_name("username").send_keys(INSTAGRAM_ID)
browser.find_element_by_name("password").send_keys(INSTAGRAM_PW)
browser.find_elements_by_class_name("sqdOP")[1].send_keys(Keys.ENTER)

############ 로그인 완료 #######################

search_bar = wait_for((By.CLASS_NAME, "XTCLo"))

search_bar.send_keys("#dog")

hashtags_list = wait_for((By.CLASS_NAME, "fuqBx"))

hashtags = hashtags_list.find_elements_by_class_name("-qQT3")

for hashtag in hashtags:
    hashtag = hashtag.get_attribute("href")
    browser.execute_script(f"window.open('{hashtag}')")

for window in browser.window_handles[1:]:
    browser.switch_to.window(window)
    hashtag_name = wait_for((By.TAG_NAME, "h1"))
    post_count = wait_for((By.CLASS_NAME, "g47SY"))
    if post_count:
        post_count = int(post_count.text.replace(",", ""))
    if hashtag_name:
        hashtag_name = hashtag_name.text[1:]
    if hashtag_name and post_count:
        print(hashtag_name, post_count)

time.sleep(3)
browser.quit()
