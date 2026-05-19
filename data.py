import uuid
from pathlib import Path

BASE_URL = "https://foodgram-frontend-1.foodgram.education-services.ru"

URL_SIGNIN = f"{BASE_URL}/signin"
URL_SIGNUP = f"{BASE_URL}/signup"
URL_RECIPES = f"{BASE_URL}/recipes"
URL_RECIPE_CREATE = f"{BASE_URL}/recipes/create"

TEST_USER_EMAIL = "YuryL1"
TEST_USER_PASSWORD = "YuryL12345678"

RECIPE_INGREDIENT_NAME = "мука"
RECIPE_INGREDIENT_SEARCH = "мук"
RECIPE_INGREDIENT_AMOUNT = "100"
RECIPE_COOKING_TIME = "30"
RECIPE_DESCRIPTION = "Описание тестового рецепта"

PHOTO_PATH = Path(__file__).resolve().parent / "resources" / "photo_for_recept.jpg"

SIGNUP_PASSWORD = "TestPass12345"


def build_unique_user() -> dict[str, str]:
    uid = uuid.uuid4().hex[:8]
    return {
        "first_name": "Тест",
        "last_name": "Пользователь",
        "username": f"user_{uid}",
        "email": f"user_{uid}@test.com",
        "password": SIGNUP_PASSWORD,
    }


def build_unique_recipe_title() -> str:
    return f"TestRecipe_{uuid.uuid4().hex[:8]}"
