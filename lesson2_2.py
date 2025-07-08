from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select


try: 
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element(By.CSS_SELECTOR, "#num1").text
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2").text

    sum = int(x_element) + int(y_element)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(f"{sum}") 

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
