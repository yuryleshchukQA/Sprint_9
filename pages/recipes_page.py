import allure

from locators.locators import RecipesPageLocators
from pages.base_page import BasePage


class RecipesPage(BasePage):
    def __init__(self, driver, timeout: int = 30):
        super().__init__(driver, timeout=timeout)

    @allure.step('Дождаться отображения карточки созданного рецепта')
    def wait_recipe_card_with_title(self, title: str) -> None:
        self.wait.until(
            lambda _: self._is_recipe_detail_visible(title)
            or self._is_recipe_list_card_visible(title)
        )

    def _is_recipe_detail_visible(self, title: str) -> bool:
        return self.are_elements_present(
            RecipesPageLocators.RECIPE_DETAIL_CARD
        ) and self.are_elements_present(
            RecipesPageLocators.recipe_detail_title(title)
        )

    def _is_recipe_list_card_visible(self, title: str) -> bool:
        return self.is_any_displayed(RecipesPageLocators.recipe_card_title(title))

    @allure.step('Карточка рецепта с указанным названием отображается')
    def is_recipe_card_visible(self, title: str) -> bool:
        return self._is_recipe_detail_visible(title) or self._is_recipe_list_card_visible(
            title
        )

    @allure.step('Получить название рецепта на карточке')
    def recipe_card_title_text(self, title: str) -> str:
        if self._is_recipe_detail_visible(title):
            return self.text(RecipesPageLocators.recipe_detail_title(title))
        return self.text(RecipesPageLocators.recipe_card_title(title))
