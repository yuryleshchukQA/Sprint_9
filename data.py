from pathlib import Path


class Urls:
    BASE = "https://foodgram-frontend-1.foodgram.education-services.ru"
    SIGNIN = f"{BASE}/signin"
    SIGNUP = f"{BASE}/signup"
    RECIPES = f"{BASE}/recipes"
    RECIPE_CREATE = f"{BASE}/recipes/create"


class TestData:
    USER_EMAIL = "YuryL1"
    USER_PASSWORD = "YuryL12345678"
    SIGNUP_PASSWORD = "TestPass12345"

    SIGNUP_FIRST_NAME = "Тест"
    SIGNUP_LAST_NAME = "Пользователь"

    RECIPE_INGREDIENT_NAME = "мука"
    RECIPE_INGREDIENT_SEARCH = "мук"
    RECIPE_INGREDIENT_AMOUNT = "100"
    RECIPE_COOKING_TIME = "30"
    RECIPE_DESCRIPTION = "Описание тестового рецепта"
    PHOTO_PATH = Path(__file__).resolve().parent / "resources" / "photo_for_recept.jpg"
