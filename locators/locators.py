from selenium.webdriver.common.by import By


class SigninPageLocators:
    INPUT_EMAIL = (By.NAME, "email")
    INPUT_PASSWORD = (By.NAME, "password")
    BUTTON_SIGNIN = (By.XPATH, "//button[normalize-space()='Войти']")
    LINK_CREATE_ACCOUNT = (By.XPATH, "//a[normalize-space()='Создать аккаунт']")


class SignupPageLocators:
    INPUT_FIRST_NAME = (By.NAME, "first_name")
    INPUT_LAST_NAME = (By.NAME, "last_name")
    INPUT_USERNAME = (By.NAME, "username")
    INPUT_EMAIL = (By.NAME, "email")
    INPUT_PASSWORD = (By.NAME, "password")
    BUTTON_CREATE_ACCOUNT = (
        By.XPATH,
        "//button[normalize-space()='Создать аккаунт']",
    )


class HeaderLocators:
    LINK_LOGOUT = (By.XPATH, "//a[normalize-space()='Выход']")
    LINK_CREATE_RECIPE = (
        By.XPATH,
        "//a[normalize-space()='Создать рецепт' and contains(@href,'/recipes/create')]",
    )


class RecipeCreatePageLocators:
    INPUT_TITLE = (
        By.XPATH,
        "//form[contains(@class,'styles_form__3XFkE')]"
        "//input[@type='text' and contains(@class,'styles_inputField__3eqTj') "
        "and not(contains(@class,'ingredients'))][1]",
    )
    INPUT_INGREDIENT_NAME = (
        By.CSS_SELECTOR,
        "input.styles_ingredientsInput__1zzql",
    )
    INPUT_INGREDIENT_AMOUNT = (
        By.CSS_SELECTOR,
        "input.styles_ingredientsAmountValue__2matT",
    )
    BUTTON_ADD_INGREDIENT = (By.CSS_SELECTOR, "motion-div.styles_ingredientAdd__3fc32, div.styles_ingredientAdd__3fc32")
    INGREDIENTS_ADDED_BLOCK = (
        By.CSS_SELECTOR,
        "motion-div.styles_ingredientsAdded__35vNf, div.styles_ingredientsAdded__35vNf",
    )
    INPUT_COOKING_TIME = (
        By.XPATH,
        "//div[contains(@class,'cookingTimeLabel')]/following-sibling::input",
    )
    TEXTAREA_DESCRIPTION = (By.CSS_SELECTOR, "textarea.styles_textareaField__1wfhC")
    INPUT_PHOTO = (By.CSS_SELECTOR, "input.styles_fileInput__3HjP3")
    BUTTON_CREATE_RECIPE = (
        By.XPATH,
        "//button[normalize-space()='Создать рецепт']",
    )

    @staticmethod
    def ingredient_suggestion(name: str) -> tuple[str, str]:
        return (
            By.XPATH,
            "//div[contains(@class,'styles_ingredientsInputs')]"
            "//div[contains(@class,'styles_container__3ukwm')]"
            f"//div[normalize-space()='{name}']",
        )


class RecipesPageLocators:
    RECIPE_DETAIL_CARD = (
        By.CSS_SELECTOR,
        "motion-div.styles_single-card__1yTTj, div.styles_single-card__1yTTj",
    )

    @staticmethod
    def recipe_card_title(title: str) -> tuple[str, str]:
        return (
            By.XPATH,
            f"//a[contains(@class,'style_card__title') and normalize-space()='{title}']",
        )

    @staticmethod
    def recipe_detail_title(title: str) -> tuple[str, str]:
        return (
            By.XPATH,
            f"//h1[contains(@class,'single-card__title') and normalize-space()='{title}']",
        )
