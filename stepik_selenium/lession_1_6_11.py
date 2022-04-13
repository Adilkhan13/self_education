from selenium import webdriver
import time

browser = webdriver.Chrome()

def auto_test(link):
    try: 
        browser = webdriver.Chrome()
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
        if "Congratulations! You have successfully registered!" == welcome_text:
            print(f"Сайт: {link} - Успешно!")
        else:
            print(f"Сайт: {link} - Провалено!")

    except Exception:
        print(f"Сайт: {link} - Ошибка!")
    finally:
        browser.quit()

if __name__ == "__main__":
    print('===========Начало проверки===========')
    auto_test('http://suninjuly.github.io/registration1.html')
    auto_test('http://suninjuly.github.io/registration2.html')
    print('===========Проверка завершена===========')
