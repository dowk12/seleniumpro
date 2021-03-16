from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from math import ceil


class ResponsiveTester:
    def __init__(self, urls):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.urls = urls
        self.maximize_window()
        self.sizes = [480, 960, 1366, 1920]

    def screenshot(self, url):
        BROWSER_HEIGHT = 1056
        self.browser.get(url)
        for size in sizes:
            self.browser.set_window_size(size, BROWSER_HEIGHT)
            self.browser.execute_script("window.scrollTo(0, 0)")
            time.sleep(3)
            scroll_size = self.browser.execute_script(
                "return document.body.scrollHeight"
            )
            total_sections = ceil(scroll_size / BROWSER_HEIGHT)
            for section in range(total_sections):
                self.browser.execute_script(
                    f"window.scrollTo(0, {section * BROWSER_HEIGHT})"
                )
                time.sleep(2)
                self.browser.save_screenshot(f"screenshots/{size}x{section}.png")

    def start(self):
        for url in urls:
            self.screenshot(url)


tester = ResponsiveTester(["https://nomadcoders.co", "https://google.com"])
tester.start()
