# отредактировать сообщение в ленте одному. на основе ТК 6
import self
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
# import datetime
from datetime import datetime

link = "https://intranet-test.roslesinforg.ru/stream/"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    # авторизация
    login = driver.find_element(By.ID, 'USER_LOGIN')
    login.send_keys("OK_RLI")
    password = driver.find_element(By.ID, "USER_PASSWORD")
    password.send_keys("OK_RLIOK_RLI")
    button1 = driver.find_element(By.CSS_SELECTOR, "input.btn")
    button1.click()
    # time.sleep(1)
    """данный кейс ставить сразу после ТК_6, чтобы находить и редактировать сообщение одному."""
    """Для редактирования необходимо открывать фрейм (?) Буду не удалять текст, а добавлю слово, которое проверю 
    конактенацией. Фрейм открывать не буду, найду actual_text"""
    # ввожу дату и время, чтобы получить уникальность сообщения
    input_txt = datetime.now()
    # TK_5 (edit message to one)
    # нахожу поле где сообщение, использую три точки
    original_text = driver.find_element(By.XPATH, '(//div[@class="feed-post-right-top-corner"]/div)[1]')
    original_text.click()
    time.sleep(1)
    # original_text.send_keys(Keys.DOWN)  # не работает
    # original_text.send_keys(Keys.ARROW_DOWN)
    edit_field = driver.find_element(By.XPATH, '//div[@class="popup-window"]/div/div/div/a[2]')
    time.sleep(2)
    edit_field.click()

    iframe1: WebElement = driver.find_element(By.CSS_SELECTOR,
                                              "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm."
                                              "bxhtmled-iframe-cnt > iframe")
    driver.switch_to.frame(iframe1)
    input5 = driver.find_element(By.TAG_NAME, "body")
    input5.send_keys("Edited ")
    input5_1 = input5.text
    input5.send_keys(Keys.CONTROL + Keys.ENTER)
    driver.switch_to.default_content()
    # нажимаю кнопку Отправить, заменил поиск кнопки нажатием Ctrl+Enter выше
    # send_key = (driver.find_element(By.ID, 'blog-submit-button-save'))
    # send_key.click()

    """ создам переменную, буду искать новый, отредактированный текст по части предложения. Это будет actual_text
    # contains(text() - метод поиска по части текста
    # пример # user_name = driver.find_element(By.XPATH, "//h4[contains(text(), 'Password for all ')]")
    # требуемый текст, как описать только часть требуемого текста?"""

    time.sleep(2)
    actual_text = driver.find_element(By.XPATH, "//div[contains(text(), 'Edited')]").text
    # print("input5_1 - ", input5_1)
    # print("actual_text - ", actual_text)
    # (//div[@class="feed-post-text"])[1]
    assert actual_text == input5_1

    # # driver.implicitly_wait(5)
    # # Ищу и нажимаю Добавить ещё
    # ok = driver.find_element(By.CSS_SELECTOR,
    #                          '.ui-tag-selector-add-button-caption')
    # ok.click()
    # element_input = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR,
    #                                 "input.ui-tag-selector-item.ui-tag-selector-text-box"))
    # )
    # time.sleep(1)
    # element_input.send_keys("Поладько")
    # time.sleep(1)
    # element_input.send_keys(Keys.ENTER)
    # # убираю Всем работникам
    # # driver.find_element(By.CSS_SELECTOR, "div.ui-tag-selector-tag-remove").click()
    # # теперь её нет в строке
    # # time.sleep(3)
    # driver.find_element(By.CSS_SELECTOR,
    #                     "input.ui-tag-selector-item.ui-tag-selector-text-box").click()
    #
    # button = driver.find_element(By.ID, "blog-submit-button-save")  # кнопка отправить
    # button.click()
    #
    # # driver.implicitly_wait(5)
    # time.sleep(1)
    # # actual_text = driver.find_element(By.XPATH, '(//div[@class="feed-post-text"])[1]')
    # actual_text = driver.find_element(By.XPATH, '(//*[@class="feed-post-text-block"]/div/div/div)[1]')
    # needed_text = input6_1
    # print("actual_text = ", actual_text.text)
    # print("needed_text = ", needed_text)
    # assert actual_text.text == needed_text
    # # self.assertEqual(needed_text, actual_text, "Не тот текст")
    # time.sleep(3)

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла
