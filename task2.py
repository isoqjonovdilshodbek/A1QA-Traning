from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import string, random

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def nav_to_main_page():
    if driver.get("https://store.steampowered.com/") == driver.get("https://store.steampowered.com/index/"):
         print("Main page: True")
    else:
         print("Main page: False")


def log_in():
    driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[5]/div[2]/div[3]/div[2]/div/div/a[1]/span").click()


def input():
    driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[5]/div/div[1]/div/div/div/div[2]/div/form/div[1]/input")\
        .send_keys(f"{random.choice(string.ascii_letters).upper()}{random.choice(string.ascii_letters).lower()}{random.choice(string.ascii_letters).lower()}"
                   f"{random.choice(string.ascii_letters).lower()}{random.choice(string.ascii_letters).lower()}{random.choice(string.ascii_letters).lower()}"
                   f"{random.choice(string.ascii_letters).lower()}{random.choice(string.ascii_letters).lower()}{random.choice(string.ascii_letters).lower()}")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[5]/div/div[1]/div/div/div/div[2]/div/form/div[2]/input").send_keys(random.randint(0,99999999))


def click():
    driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[5]/div/div[1]/div/div/div/div[2]/div/form/div[4]/button").click()


nav_to_main_page()
log_in()
input()
click()




