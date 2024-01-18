import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from termcolor import colored
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.binance.com/en"
driver.get(url)
driver.set_window_size(1920,1080)
time.sleep(1)

find=driver.find_element(By.ID, "onetrust-accept-btn-handler")
find.click()
find=driver.find_element(By.LINK_TEXT, "Markets")
find.click()
time.sleep(1)

print(colored("MAIN CRYPTOCURRENCIES: ", "blue"))
name=["Bitcoin","Ethereum","Solana"]
pricecss=['.css-vlibs4:nth-child(1) .body2[data-area="right"]','.css-vlibs4:nth-child(2) .body2[data-area="right"]','.css-vlibs4:nth-child(5) .body2[data-area="right"]'] 
percentagecss=['.css-vlibs4:nth-child(1) .body2[data-area="right"] + .body2','.css-vlibs4:nth-child(2) .body2[data-area="right"] + .body2','.css-vlibs4:nth-child(5) .body2[data-area="right"] + .body2']

for i,coin in enumerate(name):
    price_css = driver.find_element(By.CSS_SELECTOR, pricecss[i])
    percentage_css = driver.find_element(By.CSS_SELECTOR, percentagecss[i])
    price = price_css.text
    percentage = percentage_css.text
    print(colored(coin,"blue") + " Price: " + price)
    print(colored(coin,"blue") + " Percentage Change(24h): " + percentage)
    print("-----------------------")


for repeat in range(2):
    time.sleep(1)
    if repeat==0:
        print(colored("LOST THE MOST(24h): ", "red"))
    else:
        print(colored("TOP GAINERS(24h): ", "green"))
    find=driver.find_element(By.XPATH, '//div[text()="Change"]')
    find.click()
    elements = driver.find_elements(By.CLASS_NAME, "subtitle3")[:5]
    changes = []
    for element in elements:
        main = element.find_element(By.XPATH, "./ancestor::div[@class='css-cn2h2t']")
        coins_element = main.find_element(By.CLASS_NAME, "body3")
        coins = coins_element.text
        changes.append(coins)

    pricecss1=['.css-vlibs4:nth-child(1) .body2[data-area="right"]','.css-vlibs4:nth-child(2) .body2[data-area="right"]','.css-vlibs4:nth-child(3) .body2[data-area="right"]','.css-vlibs4:nth-child(4) .body2[data-area="right"]','.css-vlibs4:nth-child(5) .body2[data-area="right"]'] 
    percentagecss1=['.css-vlibs4:nth-child(1) .body2[data-area="right"] + .body2','.css-vlibs4:nth-child(2) .body2[data-area="right"] + .body2','.css-vlibs4:nth-child(3) .body2[data-area="right"] + .body2','.css-vlibs4:nth-child(4) .body2[data-area="right"] + .body2','.css-vlibs4:nth-child(5) .body2[data-area="right"] + .body2']

    for i,coin in enumerate(changes):
        price_css = driver.find_element(By.CSS_SELECTOR, pricecss1[i])
        percentage_css = driver.find_element(By.CSS_SELECTOR, percentagecss1[i])
        price = price_css.text
        percentage = percentage_css.text
        if repeat==0:
            print(colored(coin,"red") + " Price: " + price)
            print(colored(coin,"red") + " Percentage Change(24h): " + percentage)
            print("-----------------------")
        else:
            print(colored(coin,"green") + " Price: " + price)
            print(colored(coin,"green") + " Percentage Change(24h): " + percentage)
            print("-----------------------")


print(colored("NAME OF CRYPTOCURRENCY: ", "yellow"))
search=input()

find=driver.find_element(By.ID, "header_menu_search")
find.click()
time.sleep(2)
find=driver.find_element(By.CLASS_NAME, "bn-textField-input")
find.click()
find.send_keys(search)
time.sleep(2)

find=driver.find_element(By.CLASS_NAME, "explore-spot-item")
price_elements=find.find_elements(By.CLASS_NAME, "typography-Subtitle4")
price1 = price_elements[2].text
percentage1=find.find_element(By.CSS_SELECTOR, ".typography-Caption2").text


print(colored(search,"yellow") + " Price: " + price1)
print(colored(search,"yellow") + " Percentage Change(24h): " + percentage1)
print("-----------------------")
driver.quit()
