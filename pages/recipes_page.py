import allure
from selenium.webdriver.support import expected_conditions as EC

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
        cards = self.driver.find_elements(*RecipesPageLocators.RECIPE_DETAIL_CARD)
        titles = self.driver.find_elements(
            *RecipesPageLocators.recipe_detail_title(title)
        )
        return bool(cards) and bool(titles)

    def _is_recipe_list_card_visible(self, title: str) -> bool:
        elements = self.driver.find_elements(
            *RecipesPageLocators.recipe_card_title(title)
        )
        return bool(elements) and elements[0].is_displayed()

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
