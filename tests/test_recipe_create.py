import allure


@allure.suite("Создание рецепта")
class TestRecipeCreate:
    @allure.title("Создание рецепта и отображение карточки с названием")
    def test_create_recipe_shows_card_with_title(
        self,
        pages,
        open_recipe_create_page,
        recipe_form_data,
    ):
        data = recipe_form_data
        pages.recipe_create.create_recipe(
            data["title"],
            data["search_text"],
            data["ingredient_name"],
            data["amount"],
            data["cooking_time"],
            data["description"],
            data["photo_path"],
        )
        pages.recipes.wait_recipe_card_with_title(data["title"])
        assert pages.recipes.is_recipe_card_visible(data["title"])
        assert pages.recipes.recipe_card_title_text(data["title"]) == data["title"]
