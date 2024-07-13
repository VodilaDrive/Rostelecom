import pytest
from selenium import webdriver as selenium_wd
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


BASE_URL = "https://lk.smarthome.rt.ru/"
USER_1 = "tygakizilov31@gmail.com"
PASSWORD_1 = "789V456l123ad"

USER_2 = "79034147947"
PASSWORD_2 = "974350VlaD"
LOGIN_ID = "rtkid_1717263576497"

@pytest.fixture(autouse=True)
def driver():

    driver = webdriver.Firefox()
    # Переходим на страницу авторизации
    driver.get('https://lk.smarthome.rt.ru/')

    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def selenium_driver(request):
    s = Service(executable_path=GeckoDriverManager().install())
    firefox_options = Options()
    driver = selenium_wd.Firefox(service=s, options=firefox_options)
    driver.maximize_window()
    driver.implicitly_wait(5)


