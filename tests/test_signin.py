import allure

from data import TestData, Urls


@allure.suite("Авторизация")
class TestSignin:
    @allure.title("Авторизация пользователя и переход на главную страницу")
    def test_signin_redirects_to_main_page(self, pages):
        pages.signin.open_signin(Urls.SIGNIN)
        pages.signin.signin(TestData.USER_EMAIL, TestData.USER_PASSWORD)
        pages.signin.wait_redirect_to_recipes()
        assert pages.signin.is_on_recipes_main_page()
        assert pages.header.is_logout_visible()
