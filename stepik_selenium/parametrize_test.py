from selenium import webdriver
import time
import pytest
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# +
chrome_driver_path = r"C:\Users\AZaidulla\python code\chromedriver_win32\chromedriver.exe"
url_links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(chrome_driver_path)
    yield browser
    print("\nquit browser..")
    browser.quit()
    

@pytest.mark.parametrize('link',url_links)
def test_1(link,browser):
        #browser.implicitly_wait(10)
        browser.get(link)
        #time.sleep(15)
        browser_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea"))
        )
        answer = math.log(int(time.time()))
        browser_input.send_keys(str(answer))
        button = browser.find_element_by_css_selector(".submit-submission")
        button.click()
        
        browser_text = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.smart-hints__hint'))
                                    )[0].text
        if  browser_text != 'Correct!':
            print(browser_text)
        # Отправляем заполненную форму
        
        
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert 'Correct!' == browser_text,f"Кодовое слово: {browser_text}"

    #except Exception:
    #    print(f"Сайт: {link} - Ошибка!")
    #finally:
    #    browser.quit()
    #    
# -

if __name__ == "__main__":
    print('===========Начало проверки===========')
    print('===========Проверка завершена===========')
