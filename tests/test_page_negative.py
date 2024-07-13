import pytest
from selenium.webdriver.firefox import webdriver
from pages.auth_page import AuthPage, AuthRegistration
import time
from pages.locators import AuthLocators
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_auth_with_not_correct_email_and_password(driver):
    # Переходим на страницу авторизации
    driver.implicitly_wait(70)
    # Нажимаем на кнопку войти с паролем
    driver.find_element(By.XPATH, '//*[@id="standard_auth_btn"]').click()
    # Нажимаем на кнопку Почта
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    # Вводим некорректную почту
    driver.find_element(By.ID, 'username').send_keys('driver@mail.com')
    # Вводим некорректный пароль
    driver.find_element(By.ID, 'password').send_keys('1234567890')
    # Нажимаем на кнопку Войти
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    # Выводится сообщение Неверный логин или пароль
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, '//*[@id="form-error-message"]').text == "Неверный логин или пароль"

def test_auth_with_correct_email_but_not_correct_password(driver):
    # Переходим на страницу авторизации
    driver.implicitly_wait(70)
    # Нажимаем на кнопку войти с паролем
    driver.find_element(By.XPATH, '//*[@id="standard_auth_btn"]').click()
    # Нажимаем на кнопку Почта
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    # Вводим корректную почту
    driver.find_element(By.ID, 'username').send_keys('tygakizilov31@gmail.com')
    # Вводим некорректный пароль
    driver.find_element(By.ID, 'password').send_keys('1234567890')
    # Нажимаем на кнопку Войти
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    # Выводится сообщение Неверный логин или пароль
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, '//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_auth_with_not_correct_phone_number_but_correct_password(driver):
    # Переходим на страницу авторизации
    driver.implicitly_wait(70)
    # Нажимаем на кнопку войти с паролем
    driver.find_element(By.XPATH, '//*[@id="standard_auth_btn"]').click()
    # Нажимаем на кнопку Телефон
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()
    # Вводим некорректный номер телефона
    driver.find_element(By.ID, 'username').send_keys('79990000000')
    # Вводим некорректный пароль
    driver.find_element(By.ID, 'password').send_keys('974350VlaD')
    # Нажимаем на кнопку Войти
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    # Выводится сообщение Неверный логин или пароль
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, '//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_auth_with_not_correct_phone_number_and_password(driver):
    # Переходим на страницу авторизации
    driver.implicitly_wait(70)
    # Нажимаем на кнопку войти с паролем
    driver.find_element(By.XPATH, '//*[@id="standard_auth_btn"]').click()
    # Нажимаем на кнопку Телефон
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()
    # Вводим некорректный номер телефона
    driver.find_element(By.ID, 'username').send_keys('79990000000')
    # Вводим корректный пароль
    driver.find_element(By.ID, 'password').send_keys('1234567890')
    # Нажимаем на кнопку Войти
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    # Выводится сообщение Неверный логин или пароль
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, '//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_auth_with_not_correct_login_and_password(driver):
    # Переходим на страницу авторизации
    driver.implicitly_wait(70)
    # Нажимаем на кнопку войти с паролем
    driver.find_element(By.XPATH, '//*[@id="standard_auth_btn"]').click()
    # Нажимаем на кнопку Логин
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()
    # Вводим некорректный логин
    driver.find_element(By.ID, 'username').send_keys('rtkid_1234567890')
    # Вводим некорректный пароль
    driver.find_element(By.ID, 'password').send_keys('789V456l123ad')
    # Нажимаем на кнопку Войти
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    # Выводится сообщение Неверный логин или пароль
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, '//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_auth_with_not_correct_login_but_correct_password(driver):
    # Переходим на страницу авторизации
    driver.implicitly_wait(70)
    # Нажимаем на кнопку войти с паролем
    driver.find_element(By.XPATH, '//*[@id="standard_auth_btn"]').click()
    # Нажимаем на кнопку Логин
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()
    # Вводим некорректный логин
    driver.find_element(By.ID, 'username').send_keys('rtkid_1234567890')
    # Вводим корректный пароль
    driver.find_element(By.ID, 'password').send_keys('1234567890')
    # Нажимаем на кнопку Войти
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    # Выводится сообщение Неверный логин или пароль
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, '//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_auth_with_not_correct_code(driver):
    # Вход с помощью кода
    # Переходим на страницу авторизации
    driver.implicitly_wait(80)
    # Нажимаем на поле мобильный телефон и вводим данные
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('79034147947')
    # Нажимаем на кнопку Получить код
    driver.find_element(By.XPATH, '//*[@id="otp_get_code"]').click()
    # Вводим вручную полученный код
    time.sleep(15)
    # Выводится сообщение, что код неверный
    assert driver.find_element(By.XPATH, '//*[@id="form-error-message"]').text == "Неверный код. Повторите попытку"


def test_registration_with_exist_data(driver):
    # Переходим на страницу авторизации
    driver.implicitly_wait(100)
    # Нажимаем на кнопку войти с паролем
    driver.find_element(By.XPATH, '//*[@id="standard_auth_btn"]').click()
    # Нажимаем кнопку Эарегистрироваться
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    # Вводим имя
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[1]/div[1]/div/input').send_keys('Владимир')
    # Вводим фамилию
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[1]/div[2]/div/input').send_keys('Кизилов')
    # Выбираем регион
    driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[2]/div[1]/div/input').click()
    time.sleep(15)
    # Вводим номер телефона
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('79034147947')
    # Вводим пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('974350VlaD')
    # Подтверждаем введенный пароль
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('974350VlaD')
    # Нажимаем на кнопку Зарегистрироваться
    driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/button').click()
    # Проверяем что выводится окно, о том что учетная запись уже существует и просит нас войти, либо зарегистрироваться с новыми данными
    assert driver.find_element(By.XPATH,
                               '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[1]/div/div/h2').text == "Учетная запись уже существует"