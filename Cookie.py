from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    url = 'http://pythonscraping.com'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    print(driver.get_cookies())
    driver.close()

if __name__ == '__main__':
    main()