import time
import math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
# driver = webdriver.Chrome()
	browser = webdriver.Chrome(options=chrome_options)

	browser.get(link)

	b = WebDriverWait(browser, 12).until(
        	EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

	button = browser.find_element(By.ID, "book")
	button.click()

	input_value = browser.find_element(By.CSS_SELECTOR, ".form-group "+"#"+"input_value")
	print("X :]\t", input_value.text)

	input1 = browser.find_element(By.ID, "answer")
	print("Calc:\t", calc(input_value.text))
	input1.send_keys(calc(input_value.text))

	button = browser.find_element(By.ID, "solve")
	button.click()

	alert = browser.switch_to.alert
	print(alert.text)
	alert.accept()

finally:
# После выполнения всех действий мы должны не забыть закрыть окно браузера
	browser.quit()


