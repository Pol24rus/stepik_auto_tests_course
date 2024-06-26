# тест включает ТКейсы №№ 2,3,4
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from datetime import datetime
import unittest

link = "https://intranet-test.roslesinforg.ru/stream/"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()  # чтобы браузер не закрывался
driver = webdriver.Chrome(options=options, service=g)
driver.get(link)
driver.maximize_window()

# авторизация
login = driver.find_element(By.ID, "USER_LOGIN")
login.send_keys("OK_RLI")
password = driver.find_element(By.ID, "USER_PASSWORD")
password.send_keys("OK_RLIOK_RLI")
button1 = driver.find_element(By.CSS_SELECTOR, "input.btn")
button1.click()
#time.sleep(1)
input_txt = datetime.now()  #переменная, вставляю в текст, чтобы текст был разный


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        input1_3 = driver.find_element(By.ID, "microoPostFormLHE_blogPostForm_inner")  #работает, клик в поле
        input1_3.click()
        # текст сообщения
        iframe1: WebElement = driver.find_element(By.CSS_SELECTOR,
                                                  "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled"
                                                  "-iframe-cnt > iframe")
        driver.switch_to.frame(iframe1)
        input2_1 = driver.find_element(By.TAG_NAME, "body")
        input2_1.send_keys("Тест сообщение двум, от ", str(input_txt))
        input2_2 = input2_1.text
        # print("input =", input2_2)
        driver.switch_to.default_content()

        #Ищу и нажимаю Добавить ещё
        ok = driver.find_element(By.CSS_SELECTOR, ".ui-tag-selector-add-button-caption")
        ok.click()
        # ищу и ввожу Поладько и Отдел кадров
        element_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input.ui-tag-selector-item.ui-tag-selector-text-box"))
        )
        time.sleep(1)
        element_input.send_keys("Поладько")
        time.sleep(1)
        element_input.send_keys(Keys.ENTER)
        time.sleep(1)
        element_input.send_keys("Отдел")
        time.sleep(1)
        element_input.send_keys(Keys.ENTER)
        time.sleep(1)
        element_input.click()
        # клик в Отправить
        button = driver.find_element(By.ID, "blog-submit-button-save")
        button.click()
        time.sleep(1)
        # находим элемент, содержащий текст
        actual_text = driver.find_element(By.XPATH, '(//*[@class="feed-post-text"])[1]').text
        # needed_text = "22Тест сообщение двум, от ",str(input_txt)  # ответ приходит со скобками и запятой,
        # отличается. Видимо из-за того, что в 45-й строке отправляется текст со значением (value)
        """Для сравнения брал переменную (текст) который вкладывал в поле (стр 46), и сравнивал с тем, что прочел в
        Живой ленте. Корректно ли это? С другой стороны, вкладывать это одно, но не факт что оно же и возьмется потом
        с итоговой страницы, так что верно"""
        # print("выходное значение (сообщение двоим =", input2_2)
        needed_text = input2_2
        self.assertEqual(needed_text, actual_text, "Не тот текст")
        time.sleep(3)

    def test_abs4(self):
        # TK_6 (message to one)
        # клик в поле где будет сообщение
        input1 = driver.find_element(By.ID, "microoPostFormLHE_blogPostForm_inner")
        input1.click()
        # текст сообщения
        iframe1: WebElement = driver.find_element(By.CSS_SELECTOR,
                                                  "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm."
                                                  "bxhtmled-iframe-cnt > iframe")
        driver.switch_to.frame(iframe1)
        input6 = driver.find_element(By.TAG_NAME, "body")
        input6.send_keys("Тест сообщения одному, от ", str(input_txt))
        input6_1 = input6.text
        driver.switch_to.default_content()

        # driver.implicitly_wait(5)
        # Ищу и нажимаю Добавить ещё
        ok = driver.find_element(By.CSS_SELECTOR,
                                 '.ui-tag-selector-add-button-caption')
        ok.click()
        element_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "input.ui-tag-selector-item.ui-tag-selector-text-box"))
        )
        time.sleep(1)
        element_input.send_keys("Поладько")
        time.sleep(1)
        element_input.send_keys(Keys.ENTER)
        # time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,
                            "input.ui-tag-selector-item.ui-tag-selector-text-box").click()

        button = driver.find_element(By.ID, "blog-submit-button-save")  # кнопка отправить
        button.click()

        # driver.implicitly_wait(5)
        time.sleep(1)
        # actual_text = driver.find_element(By.XPATH, '(//div[@class="feed-post-text"])[1]')
        actual_text = driver.find_element(By.XPATH, '(//*[@class="feed-post-text-block"]/div/div/div)[1]')
        needed_text = input6_1
        # assert actual_text.text == needed_text
        self.assertEqual(needed_text, actual_text.text, "Не тот текст")
        time.sleep(3)

    def test_abs14(self):
        # TK_14 (add user in comment)
        # нахожу поле комментария, кликаю сразу в него, не нажимая кнопку Коментировать
        comment_field = driver.find_element(By.XPATH, "(//a[@class='feed-com-add-link'])[1]")
        comment_field.click()
        time.sleep(2)
        """нажимаю кнопку Отметить человека"""
        input14 = driver.find_element(By.XPATH, "(//div[@data-id='mention'])[2]")
        input14.click()
        time.sleep(1)
        """ввожу ФИО в открывшееся поле"""
        input14_name = driver.find_element(By.XPATH,
                                           "//input[@class='ui-tag-selector-item ui-tag-selector-text-box']")  # работает, но нужны паузы
        time.sleep(1)
        input14_name.send_keys("Поладько")
        input14_name.send_keys(Keys.RETURN)
        time.sleep(1)
        """Нажимаю Отправить"""
        input14_sendKey = driver.find_element(By.XPATH,
                                              "(//div[@class='feed-add-post-buttons --no-wrap']/button[@class='ui-btn ui-btn-sm ui-btn-primary'])[2]")
        input14_sendKey.click()

        # Работает, оставлю на утро. Сменил слипы на 1 сек, не проверял

        """ Проверка по ФИО. Это будет actual_text"""
        actual_text = driver.find_element(By.XPATH, "//span[contains(text(), 'Поладько')]").text
        print("actual_text - ", actual_text)
        needed_text = "Поладько Дмитрий"
        assert actual_text == needed_text
        self.assertEqual(needed_text, actual_text, "Не тот текст")


if __name__ == "__main__":
    unittest.main()
    print("All tests passed!")

# не забываем оставить пустую строку в конце файла
