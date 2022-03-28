from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    
    def test_1(self,link = 'http://suninjuly.github.io/registration1.html'):
       # try: 
            chrome_driver_path = r"G:\chromedriver_win32\chromedriver.exe"
            browser = webdriver.Chrome(chrome_driver_path)
            browser.get(link)

            input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
            input1.send_keys("Test")
            input1 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
            input1.send_keys("Test")
            input1 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
            input1.send_keys("Test")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text,f"Сайт: {link} - Провалено!")

        #except Exception:
        #    print(f"Сайт: {link} - Ошибка!")
        #finally:
        #    browser.quit()
        #    
    def test_2(self,link = 'http://suninjuly.github.io/registration2.html'):
        #try: 
            chrome_driver_path = r"G:\chromedriver_win32\chromedriver.exe"
            browser = webdriver.Chrome(chrome_driver_path)
            browser.get(link)

            input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
            input1.send_keys("Test")
            input1 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
            input1.send_keys("Test")
            input1 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
            input1.send_keys("Test")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text,f"Сайт: {link} - Провалено!")

        #except Exception:
        #    print(f"Сайт: {link} - Ошибка!")
        #finally:
        #    browser.quit()

if __name__ == "__main__":
    print('===========Начало проверки===========')
    unittest.main()
    print('===========Проверка завершена===========')
