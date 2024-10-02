from selenium.webdriver.common.by import By


class Locators:
    URLS = {
        'main_page_url': 'https://stellarburgers.nomoreparties.site/',
        'register_url': 'https://stellarburgers.nomoreparties.site/register',
        'log_in_url': 'https://stellarburgers.nomoreparties.site/login',
        'account_profile_url': 'https://stellarburgers.nomoreparties.site/account/profile'
    }
    EMAIL = 'сергей_чичкань_14_589@yandex.ru'
    PASSWORD = 'MyL6&@stGn'

    # форма регистрации
    REGISTRATION_NAME_INPUT_FIELD = (By.XPATH, '//label[ text()="Имя" ]/parent::div/input')  # поле Имя
    REGISTRATION_EMAIL_INPUT_FIELD = (By.XPATH, '//label[ text()="Email" ]/parent::div/input')  # поле Email
    REGISTRATION_PASSWORD_INPUT_FIELD = (By.XPATH, '//label[ text()="Пароль" ]/parent::div/input')  # поле Пароль
    REGISTRATION_SIGN_UP_SUBMIT_BUTTON = (
        By.XPATH,
        '//form/button[contains(text(), "Зарегистрироваться")]'
    )  # кнопка Зарегестрироваться
    REGISTRATION_INPUT_ERROR = (By.CSS_SELECTOR, '.input__error')  # текст валидации поля пароль
    REGISTRATION_LOGIN_BUTTON = (By.XPATH, '//a[@href="/login"]')  # кнопка Войти на форме регистрации

    # форма Входа
    LOG_IN_TITLE = (By.XPATH, '//main/div/h2[contains(text(), "Вход")]')  # заголовок формы
    LOG_IN_SUBMIT_BUTTON = (
        By.XPATH,
        '//form[@class="Auth_form__3qKeq mb-20"]/button[text()="Войти"]'
    )  # кнопка Войти

    # элементы основной страницы сайта
    MAIN_PAGE_LOG_IN_BUTTON = (
        By.XPATH,
        '//div[@class="BurgerConstructor_basket__container__2fUl3 mt-10"]/button[contains(text(), "Войти в аккаунт")]'
    )  # кнопка Войти в аккаунт
    MAIN_PAGE_PLACE_ORDER_BUTTON = (
        By.XPATH, '//div[@class="BurgerConstructor_basket__container__2fUl3 mt-10"]/button[text()="Оформить заказ"]'
    )  # кнопка Оформить заказ
    MAIN_PAGE_BURGER_TITLE = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')  # заголовок конструктора

    # элементы меню
    MENU_PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH,
        '//nav/a/p[@class="AppHeader_header__linkText__3q_va ml-2"]'
    )  # кнопка меню Личный кабинет
    MENU_CONSTRUCTOR_BUTTON = (
        By.XPATH, '//a[@class="AppHeader_header__link__3D_hX"]/p[contains(text(), "Конструктор")]'
    )  # кнопка меню Конструктор
    MENU_LOGO = (By.XPATH, '//nav/div[@class="AppHeader_header__logo__2D0X2"]/a')  # логотип

    # элементы Личного кабинета
    PA_TEXT = (By.CSS_SELECTOR, '.Account_text__fZAIn')  # информационный текст страницы
    PA_LOGOUT_BUTTON = (
        By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]'
    )  # кнопка Выход

    # вкладки конструктора
    CONS_BUNS = (By.XPATH, '//div/span[contains(text(), "Булки")]/parent::div')  # раздел Булки
    CONS_SAUCES = (By.XPATH, '//div/span[contains(text(), "Соусы")]/parent::div')  # раздел Соусы
    CONS_STUFFINGS = (By.XPATH, '//div/span[contains(text(), "Начинки")]/parent::div')  # раздел Начинки
