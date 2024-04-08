# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.get('https://sbis.ru/')
browser.maximize_window()
try:
    header = browser.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
    header.click()
    tensor_site = browser.find_element(By.CSS_SELECTOR, '[href="https://tensor.ru/"]')
    tensor_site.click()
    handles = browser.window_handles
    browser.switch_to.window(handles[1])
    sleep(3)
    article = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    browser.execute_script("return arguments[0].scrollIntoView(true);", article)
    assert article.is_displayed() == True, 'Элемент отсутствует!'
    sleep(3)
    tensor_about = browser.find_element(By.CSS_SELECTOR, '[href="/about"]')
    tensor_about.click()
    assert browser.current_url == 'https://tensor.ru/about', 'Неверный адрес'
    sleep(5)
finally:
    browser.quit()
