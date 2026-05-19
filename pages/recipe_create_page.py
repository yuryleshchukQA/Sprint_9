import allure
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import RecipeCreatePageLocators
from pages.base_page import BasePage


class RecipeCreatePage(BasePage):
    @allure.step('Открыть страницу создания рецепта')
    def open_create_recipe(self, url: str) -> None:
        self.open(url)
        self.wait.until(
            EC.presence_of_element_located(RecipeCreatePageLocators.INPUT_INGREDIENT_NAME)
        )

    @allure.step('Заполнить название рецепта')
    def fill_title(self, title: str) -> None:
        self.send_keys(RecipeCreatePageLocators.INPUT_TITLE, title)

    @allure.step('Добавить ингредиент из списка')
    def add_ingredient_from_list(
        self,
        search_text: str,
        ingredient_name: str,
        amount: str,
    ) -> None:
        ingredient_input = self.find_visible(RecipeCreatePageLocators.INPUT_INGREDIENT_NAME)
        ingredient_input.click()
        ingredient_input.send_keys(search_text)
        self.click(RecipeCreatePageLocators.ingredient_suggestion(ingredient_name))
        self.send_keys(RecipeCreatePageLocators.INPUT_INGREDIENT_AMOUNT, amount)
        self.click(RecipeCreatePageLocators.BUTTON_ADD_INGREDIENT)
        self.wait.until(
            EC.presence_of_element_located(RecipeCreatePageLocators.INGREDIENTS_ADDED_BLOCK)
        )

    @allure.step('Заполнить время приготовления')
    def fill_cooking_time(self, minutes: str) -> None:
        self.send_keys(RecipeCreatePageLocators.INPUT_COOKING_TIME, minutes)

    @allure.step('Заполнить описание рецепта')
    def fill_description(self, description: str) -> None:
        self.send_keys(RecipeCreatePageLocators.TEXTAREA_DESCRIPTION, description)

    @allure.step('Загрузить фото рецепта')
    def upload_photo(self, photo_path: str) -> None:
        self.driver.find_element(*RecipeCreatePageLocators.INPUT_PHOTO).send_keys(photo_path)

    @allure.step('Нажать кнопку «Создать рецепт»')
    def submit_recipe(self) -> None:
        self.wait.until(
            EC.element_to_be_clickable(RecipeCreatePageLocators.BUTTON_CREATE_RECIPE)
        )
        self.click(RecipeCreatePageLocators.BUTTON_CREATE_RECIPE)
        self.wait.until(
            lambda driver: "/recipes/" in driver.current_url
            and "/recipes/create" not in driver.current_url
        )

    @allure.step('Создать рецепт с заполнением всех полей')
    def create_recipe(
        self,
        title: str,
        search_text: str,
        ingredient_name: str,
        amount: str,
        cooking_time: str,
        description: str,
        photo_path: str,
    ) -> None:
        self.fill_title(title)
        self.add_ingredient_from_list(search_text, ingredient_name, amount)
        self.fill_cooking_time(cooking_time)
        self.fill_description(description)
        self.upload_photo(photo_path)
        self.submit_recipe()
