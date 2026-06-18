from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def create_driver():
    options = webdriver.ChromeOptions()
    options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    return driver


def inject_cookies(driver, cookies):
    driver.get("https://app.rocketseat.com.br")

    for cookie in cookies:
        driver.add_cookie(cookie)