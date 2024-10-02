from selenium.webdriver.support import expected_conditions

from faker import Faker
from src import helpers


class TestRegistrationForm:
    faker = Faker()

    def fill_reg_form_fields(self, driver, locators, passwrd_length: int = 6):
        # заполняю поле Имя
        driver.find_element(*locators.REGISTRATION_NAME_INPUT_FIELD).clear()
        driver.find_element(*locators.REGISTRATION_NAME_INPUT_FIELD).send_keys(self.faker.name_male())
        # заполняю поле Email
        driver.find_element(*locators.REGISTRATION_EMAIL_INPUT_FIELD).clear()
        driver.find_element(*locators.REGISTRATION_EMAIL_INPUT_FIELD).send_keys(helpers.generate_email())
        # заполняю поле Пароль
        driver.find_element(*locators.REGISTRATION_PASSWORD_INPUT_FIELD).clear()
        driver.find_element(
            *locators.REGISTRATION_PASSWORD_INPUT_FIELD).send_keys(helpers.get_random_password(passwrd_length))

    def test_registration_success(self, driver, locators, wait):
        driver.get(locators.URLS['register_url'])
        wait.until(expected_conditions.element_to_be_clickable(locators.REGISTRATION_NAME_INPUT_FIELD))
        self.fill_reg_form_fields(driver, locators, passwrd_length=10)
        # нажимаю кнопку Зарегестрироваться
        driver.find_element(*locators.REGISTRATION_SIGN_UP_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(locators.LOG_IN_TITLE))

        assert driver.current_url == locators.URLS['log_in_url']

    def test_registration_wrong_password(self, driver, locators, wait):
        driver.get(locators.URLS['register_url'])
        wait.until(expected_conditions.element_to_be_clickable(locators.REGISTRATION_NAME_INPUT_FIELD))
        self.fill_reg_form_fields(driver, locators, passwrd_length=4)
        # нажимаю кнопку Зарегистрироваться
        driver.find_element(*locators.REGISTRATION_SIGN_UP_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(locators.REGISTRATION_INPUT_ERROR))
        assert driver.current_url == locators.URLS['register_url']
        text = driver.find_element(*locators.REGISTRATION_INPUT_ERROR).text
        assert text == 'Некорректный пароль'
