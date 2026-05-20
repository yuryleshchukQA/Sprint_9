import allure

from data import Urls
from helpers import TestDataBuilder


@allure.suite("Создание аккаунта")
class TestSignup:
    @allure.title("Регистрация нового пользователя и переход на страницу авторизации")
    def test_create_account_redirects_to_signin(self, pages):
        user = TestDataBuilder.build_unique_user()
        pages.signin.open_signin(Urls.SIGNIN)
        pages.signin.go_to_signup()
        pages.signup.signup(
            user["first_name"],
            user["last_name"],
            user["username"],
            user["email"],
            user["password"],
        )
        pages.signup.wait_redirect_to_signin()
        assert pages.signin.current_url_contains("/signin")
        assert pages.signin.is_signin_form_displayed()
