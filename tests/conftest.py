import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src import locators_for_project


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 10)
    return wait


@pytest.fixture
def authorization(driver, wait, locators):
    driver.get(locators.URLS['log_in_url'])
    wait.until(expected_conditions.element_to_be_clickable(locators.REGISTRATION_EMAIL_INPUT_FIELD))
    # заполняю поле Email
    driver.find_element(*locators.REGISTRATION_EMAIL_INPUT_FIELD).clear()
    driver.find_element(*locators.REGISTRATION_EMAIL_INPUT_FIELD).send_keys(locators.EMAIL)
    # заполняю поле Пароль
    driver.find_element(*locators.REGISTRATION_PASSWORD_INPUT_FIELD).clear()
    driver.find_element(*locators.REGISTRATION_PASSWORD_INPUT_FIELD).send_keys(locators.PASSWORD)
    # нажимаю кнопку Войти
    driver.find_element(*locators.LOG_IN_SUBMIT_BUTTON).click()
    wait.until(expected_conditions.element_to_be_clickable(locators.MAIN_PAGE_PLACE_ORDER_BUTTON))
    return driver


@pytest.fixture
def locators():
    locators = locators_for_project.Locators()
    return locators
