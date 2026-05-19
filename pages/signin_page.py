import allure
from selenium.webdriver.support import expected_conditions as EC

from data import URL_RECIPES
from locators.locators import SigninPageLocators
from pages.base_page import BasePage


class SigninPage(BasePage):
    @allure.step('Открыть страницу авторизации')
    def open_signin(self, url: str) -> None:
        self.open(url)

    @allure.step('Перейти на страницу регистрации')
    def go_to_signup(self) -> None:
        self.click(SigninPageLocators.LINK_CREATE_ACCOUNT)

    @allure.step('Заполнить форму авторизации')
    def fill_signin_form(self, email: str, password: str) -> None:
        self.send_keys(SigninPageLocators.INPUT_EMAIL, email)
        self.send_keys(SigninPageLocators.INPUT_PASSWORD, password)

    @allure.step('Нажать кнопку «Войти»')
    def submit_signin(self) -> None:
        self.click(SigninPageLocators.BUTTON_SIGNIN)

    @allure.step('Авторизовать пользователя')
    def signin(self, email: str, password: str) -> None:
        self.fill_signin_form(email, password)
        self.submit_signin()

    @allure.step('Дождаться перехода на главную страницу')
    def wait_redirect_to_recipes(self) -> None:
        self.wait.until(EC.url_to_be(URL_RECIPES))

    @allure.step('Открыта главная страница с рецептами')
    def is_on_recipes_main_page(self) -> bool:
        return self.driver.current_url.rstrip("/") == URL_RECIPES.rstrip("/")

    @allure.step('Форма авторизации отображается')
    def is_signin_form_displayed(self) -> bool:
        return self.is_displayed(SigninPageLocators.INPUT_EMAIL)
