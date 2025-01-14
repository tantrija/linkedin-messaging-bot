import json
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  

CONFIG_FILE = "config.json"
def load_config():
    with open(CONFIG_FILE, "r") as file:
        return json.load(file) 

config = load_config()

EMAIL = config["email"]
PASSWORD = config["password"]
CHROME_DRIVER_PATH = config["chrome_driver_path"]

MESSAGE_TEMPLATE = """Hi {profile_name}, it's nice to connect with you. Have a good day."""

def login_to_linkedin(email, password, driver):
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
    time.sleep(5)

def send_message(driver, message_template):
    driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
    time.sleep(3)

    all_buttons = driver.find_elements(By.TAG_NAME, "button")
    message_buttons = [btn for btn in all_buttons if btn.text == "Message"]

    message_button = message_buttons[0].click()
    time.sleep(5)

    message_box = driver.find_element(By.XPATH, "//div[@aria-label='Write a message…']//p")

    profile_name = driver.find_element(By.XPATH, "//*[contains(@class, 'artdeco-pill__text')]").text
    personalised_message = message_template.format(profile_name=profile_name)

    message_box.send_keys(personalised_message)
    time.sleep(2)

    send_button = driver.find_element(By.XPATH, "//*[starts-with(@class, 'msg-form__send-button')]")
    send_button.click()

    time.sleep(10)


def main():
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    login_to_linkedin(EMAIL, PASSWORD, driver)
    send_message(driver, MESSAGE_TEMPLATE)

main()

