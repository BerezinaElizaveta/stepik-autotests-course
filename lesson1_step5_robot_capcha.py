from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/math.html'

try:
    # Открыть страницу http://suninjuly.github.io/math.html
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    x_field = browser.find_element_by_css_selector('.nowrap#input_value')
    x = int(x_field.text)
    # Посчитать математическую функцию от x
    answer = calc(x)

    # Ввести ответ в текстовое поле
    field_for_answer = browser.find_element_by_id('answer')
    field_for_answer.send_keys(answer)

    # Отметить checkbox "I'm the robot"
    checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    checkbox.click()

    # Выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element_by_css_selector('[for="robotsRule"]')
    radiobutton.click()

    # Нажать на кнопку Submit.
    submit_button = browser.find_element_by_css_selector('.btn[type="submit"]')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()