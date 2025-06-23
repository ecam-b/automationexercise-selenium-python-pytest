import os

from selenium.common import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """
    Clase base para la interacción con páginas web usando Selenium.
    """

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        """
        Encuentra un elemento y lo desplaza a la vista.
        """
        element = self._driver.find_element(*locator)
        self._scroll_to_element(element)
        return element

    def _type(self, locator: tuple, text: str, time: int = 10):
        """
        Escribe texto en un campo después de esperar su visibilidad.
        """
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 10):
        """
        Hace clic en un elemento después de esperar que sea clickeable.
        """
        self._wait_until_element_is_clickable(locator, time)
        self._find(locator).click()

    def _scroll_to_element(self, element: WebElement):
        """
        Desplaza el elemento especificado a la vista en el centro de la pantalla.
        """
        self._driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        """
        Espera hasta que un elemento esté visible en la página.
        """
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10):
        """
        Espera hasta que un elemento sea clickeable.
        """
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    def _select_dropdown_by_visible_text(self, locator: tuple, value: str):
        """
        Selecciona una opción de un menú desplegable por su texto visible.
        """
        self._wait_until_element_is_visible(locator)
        dropdown = self._find(locator)
        select = Select(dropdown)
        select.select_by_visible_text(value)

    def _get_text(self, locator: tuple) -> str:
        """
        Obtiene el texto de un elemento después de esperar su visibilidad, y lo retorna en minúsculas.
        """
        self._wait_until_element_is_visible(locator)
        return self._find(locator).text.lower()

    @property
    def current_url(self) -> str:
        """
        Obtiene la URL actual de la página.
        """
        return self._driver.current_url

    def is_displayed(self, locator: tuple, time: int = 10) -> bool:
        """
        Verifica si un elemento está visible en la página.
        """
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_url(self, url: str):
        """
        Navega a una URL específica.
        """
        self._driver.get(url)

    def _select_file(self, locator, file_name: str):
        """
        Adjunta un archivo a un campo de subida de archivos en la página.
        """
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_script_dir)  # retrocede de 'pages' a la raíz
        file_path = os.path.join(project_root, "resources", "images", file_name)
        if not os.path.exists(file_path):
            print(f"File path: {file_path}")
            raise FileNotFoundError(f"The file '{file_name}' was not found at '{file_path}'")

        self._type(locator, file_path)

    def _switch_to_alert(self, time: int = 10) -> Alert:
        """
        Cambia el foco del driver a una alerta JavaScript.
        """
        wait = WebDriverWait(self._driver, time)
        return wait.until(ec.alert_is_present())

    def _accept_alert(self, time: int = 10):
        """
        Acepta una alerta JavaScript.
        """
        alert = self._switch_to_alert(time)
        alert.accept()

    def _dismiss_alert(self, time: int = 10):
        """
        Rechaza (cierra) una alerta JavaScript.
        """
        alert = self._switch_to_alert(time)
        alert.dismiss()