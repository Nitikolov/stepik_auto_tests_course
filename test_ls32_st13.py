import unittest
import time

# webdriver это и есть набор команд для управления браузером
#from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
#from selenium.webdriver.common.by import By


class TestForm(unittest.TestCase):

	def test_abs1(self):
		self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

	def test_abs2(self):
		self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

	def test_form(self):
		# webdriver это и есть набор команд для управления браузером
		from selenium import webdriver

		# импортируем класс By, который позволяет выбрать способ поиска элемента
		from selenium.webdriver.common.by import By

		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--disable-extensions")
		chrome_options.add_argument("--start-maximized")
		chrome_options.add_argument("--disable-gpu")
		chrome_options.add_argument("--no-sandbox")
		chrome_options.add_argument("--disable-dev-shm-usage")

		link = "http://suninjuly.github.io/registration1.html"
		#link = "http://suninjuly.github.io/registration2.html"

		# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
		# driver = webdriver.Chrome()
		browser = webdriver.Chrome(options=chrome_options)

		browser.get(link)

		input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
		#print(input1.get_attribute("placeholder"))
		input1.send_keys("Ivan")

		input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
		#print(input2.get_attribute("placeholder"))
		input2.send_keys("Petrov")

		input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
		#print(input3.get_attribute("placeholder"))
		input3.send_keys("email@eamil.com")

		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()

		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)

		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text

		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual (welcome_text, "Congratulations! + You have successfully registered!", "Should be Congrats!")

		# закрываем браузер после всех манипуляций
		browser.quit()



if __name__ == "__main__":
	unittest.main()
