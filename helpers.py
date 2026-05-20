import uuid

from data import TestData


class TestDataBuilder:
    @staticmethod
    def build_unique_user() -> dict[str, str]:
        uid = uuid.uuid4().hex[:8]
        return {
            "first_name": TestData.SIGNUP_FIRST_NAME,
            "last_name": TestData.SIGNUP_LAST_NAME,
            "username": f"user_{uid}",
            "email": f"user_{uid}@test.com",
            "password": TestData.SIGNUP_PASSWORD,
        }

    @staticmethod
    def build_unique_recipe_title() -> str:
        return f"TestRecipe_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def build_recipe_form_data() -> dict[str, str]:
        return {
            "title": TestDataBuilder.build_unique_recipe_title(),
            "search_text": TestData.RECIPE_INGREDIENT_SEARCH,
            "ingredient_name": TestData.RECIPE_INGREDIENT_NAME,
            "amount": TestData.RECIPE_INGREDIENT_AMOUNT,
            "cooking_time": TestData.RECIPE_COOKING_TIME,
            "description": TestData.RECIPE_DESCRIPTION,
            "photo_path": str(TestData.PHOTO_PATH),
        }
