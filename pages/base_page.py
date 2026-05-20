from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 15):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def current_url_equals(self, url: str) -> bool:
        return self.get_current_url().rstrip("/") == url.rstrip("/")

    def current_url_contains(self, part: str) -> bool:
        return part in self.get_current_url()

    def wait_url_contains(self, part: str) -> None:
        self.wait.until(EC.url_contains(part))

    def wait_url_to_be(self, url: str) -> None:
        self.wait.until(EC.url_to_be(url))

    def wait_url_is_recipe_after_create(self) -> None:
        self.wait.until(
            lambda _: "/recipes/" in self.get_current_url()
            and "/recipes/create" not in self.get_current_url()
        )

    def wait_presence(self, locator) -> None:
        self.wait.until(EC.presence_of_element_located(locator))

    def wait_clickable(self, locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_until_enabled(self, locator) -> None:
        self.wait.until(lambda _: self.is_enabled(locator))

    def find_visible(self, locator) -> WebElement:
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_clickable(self, locator) -> WebElement:
        self.wait.until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def find_elements(self, locator) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def is_enabled(self, locator) -> bool:
        return self.driver.find_element(*locator).is_enabled()

    def is_any_displayed(self, locator) -> bool:
        elements = self.find_elements(locator)
        return bool(elements) and elements[0].is_displayed()

    def are_elements_present(self, locator) -> bool:
        return bool(self.find_elements(locator))

    def click(self, locator) -> None:
        element = self.find_clickable(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element,
        )
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text: str) -> None:
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def upload_file(self, locator, file_path: str) -> None:
        self.driver.find_element(*locator).send_keys(file_path)

    def text(self, locator) -> str:
        return self.find_visible(locator).text

    def is_displayed(self, locator) -> bool:
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).is_displayed()
