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

def get_all_quotes(driver):
    quotes_data = []
    quotes = driver.find_elements(By.CLASS_NAME, "quote")

    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, "text").text 
        author = quote.find_element(By.CLASS_NAME, "author").text 
        tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, "tag")]
        quotes_data.append({"Citação": text, "Autor": author, "Tags": tags} )

    return quotes_data

def main():
    url = "https://quotes.toscrape.com/js-delayed/"
    driver = setup_driver()

    try:
        open_page(driver, url)
        quotes = get_all_quotes(driver)
        for quote in quotes:
            print(f"Citação: {quote['Citação']}")
            print(f"Autor: {quote['Autor']}")
            print(f"Tags: {quote['Tags']}")
            print("-" * 40)
    finally:
        driver.quit()

main()
