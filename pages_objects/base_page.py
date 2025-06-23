from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_clickable(locator, time)
        self._scroll_to_element(locator)
        self._find(locator).click()

    def _scroll_to_element(self, locator: tuple):
        """
        Desplaza la vista del navegador para que el elemento especificado
        esté en el centro de la pantalla.
        """
        element = self._find(locator)
        self._driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    def _select_dropdown_by_visible_text(self, locator: tuple, value: str):
        self._wait_until_element_is_visible(locator)
        dropdown = self._find(locator)
        self._scroll_to_element(locator)
        select = Select(dropdown)
        select.select_by_visible_text(value)

    def _get_text(self, locator: tuple) -> str:
        self._wait_until_element_is_visible(locator)
        return self._find(locator).text.lower()

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def is_displayed(self, locator: tuple, time: int = 10) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_url(self, url: str):
      self._driver.get(url)