from selenium.webdriver.support import expected_conditions


class TestLogIn:

    @staticmethod
    def fill_log_in_form_fields(driver, locators):
        """Вспомогательный метод для заполнения полей формы входа."""
        # заполняю поле Email
        driver.find_element(*locators.REGISTRATION_EMAIL_INPUT_FIELD).clear()
        driver.find_element(*locators.REGISTRATION_EMAIL_INPUT_FIELD).send_keys(locators.EMAIL)
        # заполняю поле Пароль
        driver.find_element(*locators.REGISTRATION_PASSWORD_INPUT_FIELD).clear()
        driver.find_element(*locators.REGISTRATION_PASSWORD_INPUT_FIELD).send_keys(locators.PASSWORD)

    def test_log_in_via_enter_button(self, driver, locators, wait):
        """Вход по кнопке «Войти в аккаунт» на главной"""
        driver.get(locators.URLS['main_page_url'])
        wait.until(expected_conditions.element_to_be_clickable(locators.MAIN_PAGE_LOG_IN_BUTTON))
        # нажимаю кнопку Войти в аккаунт
        driver.find_element(*locators.MAIN_PAGE_LOG_IN_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable(locators.REGISTRATION_EMAIL_INPUT_FIELD))
        # заполняю поля формы
        self.fill_log_in_form_fields(driver, locators)
        # нажимаю кнопку Войти
        driver.find_element(*locators.LOG_IN_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable(locators.MAIN_PAGE_PLACE_ORDER_BUTTON))
        assert driver.find_element(*locators.MAIN_PAGE_PLACE_ORDER_BUTTON).text == 'Оформить заказ'

    def test_log_in_via_personal_account(self, driver, locators, wait):
        """Вход через кнопку Личный кабинет."""
        driver.get(locators.URLS['main_page_url'])
        wait.until(expected_conditions.element_to_be_clickable(locators.MENU_PERSONAL_ACCOUNT_BUTTON))
        # перехожу в личный кабинет
        driver.find_element(*locators.MENU_PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable(locators.REGISTRATION_EMAIL_INPUT_FIELD))
        # заполняю поля формы
        self.fill_log_in_form_fields(driver, locators)
        driver.find_element(*locators.LOG_IN_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable(locators.MAIN_PAGE_PLACE_ORDER_BUTTON))
        assert driver.find_element(*locators.MAIN_PAGE_PLACE_ORDER_BUTTON).text == 'Оформить заказ'

    def test_log_in_via_button_in_reg_form(self, driver, locators, wait):
        """Вход через кнопку в форме регистрации."""
        driver.get(locators.URLS['register_url'])
        wait.until(expected_conditions.element_to_be_clickable(locators.REGISTRATION_LOGIN_BUTTON))
        # нажимаю кнопку Войти на форме регистрации
        driver.find_element(*locators.REGISTRATION_LOGIN_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable(locators.REGISTRATION_EMAIL_INPUT_FIELD))
        # заполняю поля на форме
        self.fill_log_in_form_fields(driver, locators)
        # нажимаю кнопку Войти
        driver.find_element(*locators.LOG_IN_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable(locators.MAIN_PAGE_PLACE_ORDER_BUTTON))
        assert driver.find_element(*locators.MAIN_PAGE_PLACE_ORDER_BUTTON).text == 'Оформить заказ'

    def test_log_in_via_password_recovery(self, driver, locators, wait):
        """Вход через кнопку в форме восстановления пароля."""
        driver.get(locators.URLS['main_page_url'])
        wait.until(expected_conditions.element_to_be_clickable(locators.MENU_PERSONAL_ACCOUNT_BUTTON))
        # нажимаю кнопку Войти в аккаунт
        driver.find_element(*locators.MAIN_PAGE_LOG_IN_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable(locators.REGISTRATION_EMAIL_INPUT_FIELD))
        # заполняю поля формы
        self.fill_log_in_form_fields(driver, locators)
        # нажимаю кнопку Войти
        driver.find_element(*locators.LOG_IN_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable(locators.MAIN_PAGE_PLACE_ORDER_BUTTON))
        assert driver.find_element(*locators.MAIN_PAGE_PLACE_ORDER_BUTTON).text == 'Оформить заказ'
