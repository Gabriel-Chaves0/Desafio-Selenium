from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def open_page(driver, url):
    driver.get(url)
    time.sleep(10)

def main():
    url = "https://quotes.toscrape.com/js-delayed/"
    driver = setup_driver()

    try:
        open_page(driver, url)
    finally:
        driver.quit()

main()
