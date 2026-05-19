import allure
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import SignupPageLocators
from pages.base_page import BasePage


class SignupPage(BasePage):
    @allure.step('Заполнить форму регистрации')
    def fill_signup_form(
        self,
        first_name: str,
        last_name: str,
        username: str,
        email: str,
        password: str,
    ) -> None:
        self.send_keys(SignupPageLocators.INPUT_FIRST_NAME, first_name)
        self.send_keys(SignupPageLocators.INPUT_LAST_NAME, last_name)
        self.send_keys(SignupPageLocators.INPUT_USERNAME, username)
        self.send_keys(SignupPageLocators.INPUT_EMAIL, email)
        self.send_keys(SignupPageLocators.INPUT_PASSWORD, password)

    @allure.step('Нажать кнопку «Создать аккаунт»')
    def submit_signup(self) -> None:
        self.wait.until(
            lambda _: self.driver.find_element(
                *SignupPageLocators.BUTTON_CREATE_ACCOUNT
            ).is_enabled()
        )
        self.click(SignupPageLocators.BUTTON_CREATE_ACCOUNT)

    @allure.step('Зарегистрировать пользователя')
    def signup(
        self,
        first_name: str,
        last_name: str,
        username: str,
        email: str,
        password: str,
    ) -> None:
        self.fill_signup_form(first_name, last_name, username, email, password)
        self.submit_signup()

    @allure.step('Дождаться перехода на страницу авторизации')
    def wait_redirect_to_signin(self) -> None:
        self.wait.until(EC.url_contains("/signin"))
