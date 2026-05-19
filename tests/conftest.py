import os

import pytest
from selenium import webdriver

from data import (
    PHOTO_PATH,
    RECIPE_COOKING_TIME,
    RECIPE_DESCRIPTION,
    RECIPE_INGREDIENT_AMOUNT,
    RECIPE_INGREDIENT_NAME,
    RECIPE_INGREDIENT_SEARCH,
    TEST_USER_EMAIL,
    TEST_USER_PASSWORD,
    URL_RECIPE_CREATE,
    URL_SIGNIN,
    build_unique_recipe_title,
    build_unique_user,
)
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

    drv.implicitly_wait(0)
    yield drv
    drv.quit()


@pytest.fixture
def pages(driver):
    return Pages(driver)


@pytest.fixture
def unique_user():
    return build_unique_user()


@pytest.fixture
def unique_recipe_title():
    return build_unique_recipe_title()


@pytest.fixture
def authenticated_user(pages):
    pages.signin.open_signin(URL_SIGNIN)
    pages.signin.signin(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    pages.signin.wait_redirect_to_recipes()
    return {
        "email": TEST_USER_EMAIL,
        "password": TEST_USER_PASSWORD,
    }


@pytest.fixture
def recipe_form_data(unique_recipe_title):
    return {
        "title": unique_recipe_title,
        "search_text": RECIPE_INGREDIENT_SEARCH,
        "ingredient_name": RECIPE_INGREDIENT_NAME,
        "amount": RECIPE_INGREDIENT_AMOUNT,
        "cooking_time": RECIPE_COOKING_TIME,
        "description": RECIPE_DESCRIPTION,
        "photo_path": str(PHOTO_PATH),
    }


@pytest.fixture
def open_recipe_create_page(authenticated_user, pages):
    pages.recipe_create.open_create_recipe(URL_RECIPE_CREATE)
    return authenticated_user


def pytest_addoption(parser):
    parser.addoption(
        "--remote-url",
        action="store",
        default=None,
        help="URL Selenium Grid / Selenoid, например http://selenoid:4444/wd/hub",
    )
