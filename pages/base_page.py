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

    def find_visible(self, locator) -> WebElement:
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_clickable(self, locator) -> WebElement:
        self.wait.until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

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

    def text(self, locator) -> str:
        return self.find_visible(locator).text

    def is_displayed(self, locator) -> bool:
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).is_displayed()

    def wait_url_contains(self, part: str) -> None:
        self.wait.until(EC.url_contains(part))

    def current_url_contains(self, part: str) -> bool:
        return part in self.driver.current_url
