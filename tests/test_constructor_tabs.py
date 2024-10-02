from selenium.webdriver.support import expected_conditions


class TestConstructorTabs:
    desired_class = 'tab_tab_type_current__2BEPc'

    def test_bun_tab(self, driver, locators, wait):
        """Переход к разделу Булки."""
        driver.get(locators.URLS['main_page_url'])
        wait.until(expected_conditions.element_to_be_clickable(locators.CONS_SAUCES))
        # нажимаю на вкладку Соусы
        driver.find_element(*locators.CONS_SAUCES).click()
        # нажимаю на вкладку Булки
        driver.find_element(*locators.CONS_BUNS).click()
        get_class = driver.find_element(*locators.CONS_BUNS).get_attribute('class')
        assert self.desired_class in get_class

    def test_sauces_tab(self, driver, locators, wait):
        """Переход к разделу Соусы."""
        driver.get(locators.URLS['main_page_url'])
        wait.until(expected_conditions.element_to_be_clickable(locators.CONS_SAUCES))
        # нажимаю на вкладку Соусы
        driver.find_element(*locators.CONS_SAUCES).click()
        get_class = driver.find_element(*locators.CONS_SAUCES).get_attribute('class')
        assert self.desired_class in get_class

    def test_stuffings_tab(self, driver, locators, wait):
        """Переход к разделу Начинки."""
        driver.get(locators.URLS['main_page_url'])
        wait.until(expected_conditions.element_to_be_clickable(locators.CONS_SAUCES))
        # нажимаю на вкладку Начинки
        driver.find_element(*locators.CONS_STUFFINGS).click()
        get_class = driver.find_element(*locators.CONS_STUFFINGS).get_attribute('class')
        assert self.desired_class in get_class
