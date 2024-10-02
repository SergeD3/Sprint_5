from selenium.webdriver.support import expected_conditions


class TestWebsitePagesNavigation:

    def test_navigation_to_personal_acc_by_click(self, driver, locators, wait):
        """Переход по клику на «Личный кабинет»"""
        driver.get(locators.URLS['main_page_url'])
        wait.until(expected_conditions.element_to_be_clickable(locators.MENU_PERSONAL_ACCOUNT_BUTTON))
        # кликаю по Личному кабинету
        driver.find_element(*locators.MENU_PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable(locators.LOG_IN_SUBMIT_BUTTON))

        assert driver.current_url == locators.URLS['log_in_url']

    def test_navigation_to_constructor_by_click(self, authorization, locators, wait):
        """Переход по клику на «Конструктор»"""
        authorization.find_element(*locators.MENU_PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(locators.PA_TEXT))
        assert authorization.current_url == locators.URLS['account_profile_url']
        authorization.find_element(*locators.MENU_CONSTRUCTOR_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_BURGER_TITLE))
        assert authorization.current_url == locators.URLS['main_page_url']

    def test__navigation_to_logo_by_click(self, authorization, locators, wait):
        """Переход по клику на логотип Stellar Burgers"""
        authorization.find_element(*locators.MENU_PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(locators.PA_TEXT))
        assert authorization.current_url == locators.URLS['account_profile_url']
        # кликаю на лого
        authorization.find_element(*locators.MENU_LOGO).click()
        wait.until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_BURGER_TITLE))
        assert authorization.current_url == locators.URLS['main_page_url']
