import os

import pytest
from selenium import webdriver

from data import TestData, Urls
from pages.header_page import HeaderPage
from pages.recipe_create_page import RecipeCreatePage
from pages.recipes_page import RecipesPage
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage


class Pages:
    def __init__(self, driver):
        self.signin = SigninPage(driver)
        self.signup = SignupPage(driver)
        self.header = HeaderPage(driver)
        self.recipe_create = RecipeCreatePage(driver)
        self.recipes = RecipesPage(driver)


@pytest.fixture(scope="function", params=("chrome",))
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if os.getenv("CI"):
        options.add_argument("--headless=new")

    remote_url = request.config.getoption("--remote-url", default=None)
    if remote_url:
        drv = webdriver.Remote(command_executor=remote_url, options=options)
    else:
        drv = webdriver.Chrome(options=options)

    yield drv
    drv.quit()


@pytest.fixture
def pages(driver):
    return Pages(driver)


@pytest.fixture
def authenticated_user(pages):
    pages.signin.open_signin(Urls.SIGNIN)
    pages.signin.signin(TestData.USER_EMAIL, TestData.USER_PASSWORD)
    pages.signin.wait_redirect_to_recipes()
    return {
        "email": TestData.USER_EMAIL,
        "password": TestData.USER_PASSWORD,
    }


@pytest.fixture
def open_recipe_create_page(authenticated_user, pages):
    pages.recipe_create.open_create_recipe(Urls.RECIPE_CREATE)
    return authenticated_user


def pytest_addoption(parser):
    parser.addoption(
        "--remote-url",
        action="store",
        default=None,
        help="URL Selenium Grid / Selenoid, например http://selenoid:4444/wd/hub",
    )
