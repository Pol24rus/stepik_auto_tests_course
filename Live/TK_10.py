from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import datetime
from datetime import datetime


link = "https://intranet-test.roslesinforg.ru/stream/"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    # авторизация
    login = driver.find_element(By.ID, "USER_LOGIN")
    login.send_keys("OK_RLI")
    password = driver.find_element(By.ID, "USER_PASSWORD")
    password.send_keys("OK_RLIOK_RLI")
    button1 = driver.find_element(By.CSS_SELECTOR, "input.btn")
    button1.click()
    #time.sleep(1)

    input_txt = datetime.now() # текст в поле, будет каждый раз разный
    
    #нахожу "Еще"
    driver.find_element(By.ID, "feed-add-post-form-link-text").click() 
    # нахожу "Благодарность"
    #driver.find_element(By.LINK_TEXT, "Благодарность").click()
    driver.find_element(By.CSS_SELECTOR, "span.menu-popup-item.menu-popup-no-icon.feed-add-post-form-grat.feed-add-post-form-grat-more > span.menu-popup-item-text").click()

    # текст сообщения
    iframe1: WebElement = driver.find_element(By.CSS_SELECTOR, "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
    driver.switch_to.frame(iframe1)
    input2 = driver.find_element(By.TAG_NAME, "body")
    input2.send_keys("Тест на объявление благодарности от ", str(input_txt))
    driver.switch_to.default_content() 

    #Ищу и нажимаю Добавить ещё
    driver.find_element(By.CSS_SELECTOR, ".ui-tag-selector-add-button-caption").click()
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
    # убираю Всем работникам
    driver.find_element(By.CSS_SELECTOR, "div.ui-tag-selector-tag-remove").click()

    #Найти "Кто награждается" и ввести ФИО
    driver.find_element(By.CSS_SELECTOR, "#entity-selector-dest-selector-blog-post-form-grat > div > div > div.ui-tag-selector-items > span > span").click()
    element_input2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#entity-selector-dest-selector-blog-post-form-grat > div > div > div.ui-tag-selector-items > input"))
        )
    time.sleep(1)
    element_input2.send_keys("Поладько")
    time.sleep(1)
    element_input2.send_keys(Keys.ENTER)

    button = driver.find_element(By.ID, "blog-submit-button-save")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла