from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    # Открыть страницу http://suninjuly.github.io/get_attribute.html
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами
    chest = browser.find_element_by_id('treasure')

    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
    valuex = int(chest.get_attribute('valuex'))

    # Посчитать математическую функцию от x (сама функция остаётся неизменной)
    x = calc(valuex)

    # Ввести ответ в текстовое поле
    field_for_answer = browser.find_element_by_id('answer')
    field_for_answer.send_keys(x)

    # Отметить checkbox "I'm the robot"
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    # Выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()

    # Нажать на кнопку "Submit"
    submit_button = browser.find_element_by_xpath('//button[text()="Submit"]')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()