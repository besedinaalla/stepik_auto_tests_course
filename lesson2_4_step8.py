import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
book = browser.find_element(By.ID, "book")
book.click()

a_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
a = a_element.text
y = calc(a)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

submit = browser.find_element(By.ID, "solve")
submit.click()


time.sleep(20)
browser.quit()
