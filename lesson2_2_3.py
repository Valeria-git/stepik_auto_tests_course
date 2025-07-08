from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 


try: 


    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 


    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    browser.find_element(By.NAME, "firstname").send_keys("firstname")
    browser.find_element(By.NAME, "lastname").send_keys("lastname")
    browser.find_element(By.NAME, "email").send_keys("email")


    input_field = browser.find_element(By.ID, "file")
    input_field.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
