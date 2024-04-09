# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep

try:
    browser = webdriver.Chrome()
    browser.get('https://fix-online.sbis.ru/')
    browser.maximize_window()

    user_login, user_password = 'pers_zp', 'pers_zp654321'
    log_field = browser.find_element(By.CSS_SELECTOR, '.auth-AdaptiveLoginForm__inputBlock .controls-Field')
    log_field.send_keys(user_login, Keys.ENTER)
    pass_field = browser.find_element(By.CSS_SELECTOR, '.auth-AdaptiveLoginForm__password .controls-Field')
    pass_field.send_keys(user_password, Keys.ENTER)
    sleep(10)

    contacts = browser.find_element(By.CSS_SELECTOR, '.NavigationPanels-Accordion__title_level-1')
    contacts.click()
    contacts.click()
    sleep(3)

    plus = browser.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]')
    plus.click()
    sleep(3)
    cont_field = browser.find_element(By.CSS_SELECTOR, '.controls_popupTemplate_theme-default .controls-Field')
    cont_field.send_keys('крюков борис', Keys.ENTER)
    sleep(3)
    user_name = browser.find_element(By.CSS_SELECTOR, '.controls-StackTemplate__content-area .controls-Scroll-containerBase_userContent')
    user_name.click()
    sleep(3)
    text = browser.find_element(By.CSS_SELECTOR, '.textEditor_base_editor .textEditor_slate_Field')
    mes = 'Приветик'
    text.send_keys(mes, Keys.ENTER)
    sleep(3)
    accept = browser.find_element(By.CSS_SELECTOR, '.msg-send-editor__send .controls-Button_clickable')
    accept.click()
    sleep(3)
    new_mes = browser.find_element(By.CSS_SELECTOR, '.msg-dialogs-item_unread [title="Крюков Борис Викторович"]')
    assert new_mes.is_displayed(), 'Нет сообщения'

    action_chains = ActionChains(browser)
    action_chains.move_to_element(new_mes)
    action_chains.context_click(new_mes)
    action_chains.perform()
    sleep(3)
    delete = browser.find_element(By.CSS_SELECTOR, '.controls-ListViewV__itemsContainer--newRender [data-target="menu_item_deleteToArchive"]')
    delete.click()
    sleep(4)
    assert browser.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item_unread [title="Крюков Борис Викторович"]') == [], 'Сообщение не удалено'

finally:
    browser.quit()
