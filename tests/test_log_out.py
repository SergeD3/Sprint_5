from selenium.webdriver.support import expected_conditions


class TestLogOut:

    def test_log_out(self, authorization, locators, wait):
        """Выход по кнопке «Выйти» в личном кабинете"""
        authorization.find_element(*locators.MENU_PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(locators.PA_TEXT))
        assert authorization.current_url == locators.URLS['account_profile_url']
        # нажимаю кнопку Выйти
        authorization.find_element(*locators.PA_LOGOUT_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(locators.LOG_IN_TITLE))
        assert authorization.current_url == locators.URLS['log_in_url']
