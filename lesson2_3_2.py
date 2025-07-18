from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
 
    button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary").click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x_element)

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
