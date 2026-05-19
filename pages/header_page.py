import allure

from locators.locators import HeaderLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step('Кнопка «Выход» отображается')
    def is_logout_visible(self) -> bool:
        return self.is_displayed(HeaderLocators.LINK_LOGOUT)

    @allure.step('Перейти на вкладку «Создать рецепт»')
    def go_to_create_recipe(self) -> None:
        self.click(HeaderLocators.LINK_CREATE_RECIPE)
