from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x_element)

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
  #  browser.execute_script("window.scrollBy(0, 150);")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
