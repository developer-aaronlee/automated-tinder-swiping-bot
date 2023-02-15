from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time

username = "pythoncoderoom@gmail.com"
# username = "automations.python@gmail.com"
password = "lsr211425"

chrome_driver = Service("/Applications/chromedriver")
driver = webdriver.Chrome(service=chrome_driver)

driver.get("https://tinder.com/")

main_window = driver.window_handles[0]
print(driver.title)
print(driver.window_handles[0])

time.sleep(2)
login_button = driver.find_element(By.LINK_TEXT, "Log in")
login_button.click()

time.sleep(2)
facebook_login = driver.find_element(By.XPATH, '//*[@id="t-1917074667"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_login.click()

time.sleep(2)
login_window = driver.window_handles[1]
driver.switch_to.window(login_window)
print(driver.title)
print(driver.window_handles[1])

time.sleep(1)
username_input = driver.find_element(By.ID, "email")
username_input.send_keys(username)

time.sleep(1)
password_input = driver.find_element(By.ID, "pass")
password_input.send_keys(password)

time.sleep(1)
password_input.send_keys(Keys.ENTER)

time.sleep(3)
driver.switch_to.window(main_window)
print(driver.title)
print(driver.window_handles[0])

time.sleep(3)
location_button = driver.find_element(By.XPATH, '//*[@id="t-1917074667"]/main/div/div/div/div[3]/button[1]')
location_button.click()

time.sleep(3)
notification_button = driver.find_element(By.XPATH, '//*[@id="t-1917074667"]/main/div/div/div/div[3]/button[2]')
notification_button.click()

time.sleep(3)
cookie_button = driver.find_element(By.XPATH, '//*[@id="t-188693591"]/div/div[2]/div/div/div[1]/div[1]/button')
cookie_button.click()

for x in range(50):
    try:
        time.sleep(3)
        slide_cards = driver.find_element(By.TAG_NAME, "body")
        slide_cards.send_keys(Keys.ARROW_RIGHT)
        print(f"Liked - {x} times")

    except ElementClickInterceptedException:
        print("There's a match")
        time.sleep(3)
        back_button = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
        back_button.click()

    except NoSuchElementException:
        print("Like button loading")
        continue



