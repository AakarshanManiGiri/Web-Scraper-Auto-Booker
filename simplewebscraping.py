from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import time

def wait_for_clickable(driver, by, value, timeout=30):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))

def sign_in(driver, email, password):
    sign_in_button = wait_for_clickable(driver, By.XPATH, "//button[contains(text(), 'Sign in')]")
    sign_in_button.click()
    email_input = wait_for_clickable(driver, By.ID, "email")
    email_input.send_keys(email)
    password_input = wait_for_clickable(driver, By.ID, "password")
    password_input.send_keys(password)
    submit_button = wait_for_clickable(driver, By.XPATH, "//button[contains(@class, 'btn-grad sign-in')]")
    submit_button.click()

def book_slot(email, password):
    service = Service('C:/chromedriver-win64/chromedriver.exe')
    chrome_options = Options()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    
    try:
        driver.get('https://dubaipublicparks.ae/home')
        sign_in(driver, email, password)
        time.sleep(1)
        back_to_home_button = wait_for_clickable(driver, By.XPATH, "//button[contains(@class, 'btn-grad') and text()='Back To Home']")
        back_to_home_button.click()
        time.sleep(5)
        sports_court_button = wait_for_clickable(driver, By.LINK_TEXT, "Sports Court")
        sports_court_button.click()
        search_input = wait_for_clickable(driver, By.ID, "fullText")
        search_input.send_keys("Abu Hail Football")
        search_input.send_keys(Keys.RETURN)
        search_input.send_keys(Keys.RETURN)
        search_input.send_keys(Keys.RETURN)
        time.sleep(0.5)
        arrow_button = wait_for_clickable(driver, By.XPATH, "//i[contains(@class, 'fas fa-arrow-right')]")
        arrow_button.click()
        date_input = wait_for_clickable(driver, By.CSS_SELECTOR, "input[formcontrolname='date']")
        date_input.click()
        date_button = wait_for_clickable(driver, By.XPATH, "//div[@role='gridcell' and @aria-label='Tuesday, December 24, 2024']")
        date_button.click()
        time_slot_button = wait_for_clickable(driver, By.XPATH, "//button[contains(text(), 'Time Slot')]")
        time_slot_button.click()
        time_slot = wait_for_clickable(driver, By.XPATH, "//button[contains(text(), '18:00 - 19:00')]")
        time_slot.click()
        reserve_button = wait_for_clickable(driver, By.XPATH, "//button[contains(text(), 'Reserve')]")
        reserve_button.click()
        time.sleep(5)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    your_email = "sample_email"
    your_password = "Samplepassword"
    book_slot(your_email, your_password)