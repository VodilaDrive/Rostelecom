import time
from selenium.webdriver.common.by import By


def test_auth_with_email(driver):
    # Переходим на страницу авторизации
    driver.implicitly_wait(40)
    # Нажимаем кнопку войти с паролем
    driver.find_element(By.XPATH, '//*[@id="standard_auth_btn"]').click()
    # Нажимаем на кнопку Почта
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    # Вводим корректную почту
    driver.find_element(By.ID, 'username').send_keys('tygakizilov31@gmail.com')
    # Вводим корректный пароль
    driver.find_element(By.ID, 'password').send_keys('789V456l123ad')
    # Нажимаем на поле запомнить меня
    driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/span[1]').click()

    driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/span[1]').click()
    # Нажимаем на кнопку Войти
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    # Проверяем что перешли на главную страницу личного кабинета
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/section[1]/h2').text == "Это домашний экран"


def test_auth_with_phone_number(driver):
    # Переходим на страницу авторизации
    driver.implicitly_wait(50)
    # Нажимаем кнопку войти с паролем
    driver.find_element(By.XPATH, '//*[@id="standard_auth_btn"]').click()
    # Нажимаем на кнопку Телефон
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()
    # Вводим корректный номер телефона
    driver.find_element(By.ID, 'username').send_keys('79034147947')
    # Вводим корректный пароль
    driver.find_element(By.ID, 'password').send_keys('974350VlaD')
    # Нажимаем на поле запомнить меня
    driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/span[1]').click()

    driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/span[1]').click()
    # Нажимаем на кнопку Войти
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    # Проверяем что перешли на главную страницу личного кабинета
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/section[1]/h2').text == "Это домашний экран"


def test_auth_with_login(driver):
    # Переходим на страницу авторизации
    driver.implicitly_wait(50)
    # Нажимаем кнопку войти с паролем
    driver.find_element(By.XPATH, '//*[@id="standard_auth_btn"]').click()
    # Нажимаем на кнопку Логин
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()
    # Вводим корректный логин
    driver.find_element(By.ID, 'username').send_keys('rtkid_1717263576497')
    # Вводим корректный пароль
    driver.find_element(By.ID, 'password').send_keys('789V456l123ad')
    # Нажимаем на поле запомнить меня
    driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/span[1]').click()

    driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/span[1]').click()
    # Нажимаем на кнопку Войти
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    # Проверяем что перешли на главную страницу личного кабинета
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/section[1]/h2').text == "Это домашний экран"


def test_auth_with_code(driver):
    # Переходим на страницу авторизации по коду
    driver.implicitly_wait(70)
    # Вводим корректный номер телефона
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('79034147947')
    # Нажимаем на кнопку Получить код
    driver.find_element(By.XPATH, '//*[@id="otp_get_code"]').click()
    # Вручную вводим код
    time.sleep(15)
    # Проверяем что перешли на главную страницу личного кабинета
    assert driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/section[1]/h2').text == "Это домашний экран"


def test_recover_password_by_email(driver):
    # Переходим на страницу авторизации
    driver.implicitly_wait(90)
    # Нажимаем кнопку войти с паролем
    driver.find_element(By.XPATH, '//*[@id="standard_auth_btn"]').click()
    # Нажимаем на кнопку Забыли пароль
    driver.find_element(By.XPATH, '//*[@id="forgot_password"]').click()
    # Нажимаем на кнопку Почта
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    # Вводим корректную почту
    driver.find_element(By.ID, 'username').send_keys('tygakizilov31@gmail.com')
    # Нажимаем на поле для ввода символов
    driver.find_element(By.XPATH, '//*[@id="captcha"]').click()
    # Вручную вводим символы
    time.sleep(15)
    # Нажимаем на кнопку Продолжить
    driver.find_element(By.XPATH, '//*[@id="reset"]').click()
    # Вводим полученный код
    time.sleep(15)
    # Создаем новый пароль
    driver.find_element(By.XPATH, '//*[@id="reset"]').send_keys('951357vLaD')
    # Нажимаем на глаз, чтобы проверить какой пароль мы создаем
    driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div/div[1]/div/div[2]/svg').click()
    # Повторяем пароль, что и введеный ранее
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('951357vLaD')
    # Нажимаем на глаз, чтобы проверить правильно ли совпали пароли
    driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div/div[2]/div/div[2]/svg').click()
    # Нажимаем на кнопку
    driver.find_element(By.XPATH, '//*[@id="t-btn-reset-pass"]').click()
    # Переходим на страницу авторизации
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Авторизация"


def test_recover_password_by_phone_number(driver):
    # Переходим на страницу авторизации
    driver.implicitly_wait(90)
    # Нажимаем кнопку войти с паролем
    driver.find_element(By.XPATH, '//*[@id="standard_auth_btn"]').click()
    # Нажимаем на кнопку Забыли пароль
    driver.find_element(By.XPATH, '//*[@id="forgot_password"]').click()
    # Нажимаем на кнопку Телефон
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()
    # Вводим корректный номер телефона
    driver.find_element(By.ID, 'username').send_keys('79034147947')
    # Нажимаем на поле для ввода символов
    driver.find_element(By.XPATH, '//*[@id="captcha"]').click()
    # Вручную вводим символы
    time.sleep(15)
    # Нажимаем на кнопку Продолжить
    driver.find_element(By.XPATH, '//*[@id="reset"]').click()
    # Вводим полученный код
    time.sleep(15)
    # Создаем новый пароль
    driver.find_element(By.XPATH, '//*[@id="password-new"]').send_keys('951357vLaD')
    # Нажимаем на глаз, чтобы проверить какой пароль мы создаем
    driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div/div[1]/div/div[2]/svg').click()
    # Повторяем пароль, что и введенный ранее
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('753159WlaD')
    # Нажимаем на глаз, чтобы проверить правильно ли совпали пароли
    driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div/div[2]/div/div[2]/svg').click()
    # Нажимаем на кнопку
    driver.find_element(By.XPATH, '//*[@id="t-btn-reset-pass"]').click()
    # Переходим на страницу авторизации
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Авторизация"


def test_recover_password_by_login(driver):
    # Переходим на страницу авторизации
    driver.implicitly_wait(90)
    # Нажимаем кнопку войти с паролем
    driver.find_element(By.XPATH, '//*[@id="standard_auth_btn"]').click()
    # Нажимаем на кнопку Забыли пароль
    driver.find_element(By.XPATH, '//*[@id="forgot_password"]').click()
    # Нажимаем на кнопку Логин
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()
    # Вводим корректный логин
    driver.find_element(By.ID, 'username').send_keys('rtkid_1717263576497')
    # Нажимаем на поле для ввода символов
    driver.find_element(By.XPATH, '//*[@id="captcha"]').click()
    # Вручную вводим символы
    time.sleep(15)
    # Нажимаем на кнопку Продолжить
    driver.find_element(By.XPATH, '//*[@id="reset"]').click()
    # Вводим полученный код
    time.sleep(15)
    # Создаем новый пароль
    driver.find_element(By.XPATH, '//*[@id="password-new"]').send_keys('852479GlAd')
    # Нажимаем на глаз, чтобы проверить какой пароль мы создаем
    driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div/div[1]/div/div[2]/svg').click()
    # Повторяем пароль, что и введенный ранее
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('852479GlAd')
    # Нажимаем на глаз, чтобы проверить правильно ли совпали пароли
    driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div/div[2]/div/div[2]/svg').click()
    # Нажимаем на кнопку
    driver.find_element(By.XPATH, '//*[@id="t-btn-reset-pass"]').click()
    # Переходим на страницу авторизации
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Авторизация"
