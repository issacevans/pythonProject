from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def make_webdriver() -> Chrome:
    options = create_options()
    # s = Service(ChromeDriverManager().install())
    driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def create_options() -> Options:
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--start-maximized")
    return options


if __name__ == '__main__':
    url = "https://admin.vir777.net/login"
    _driver = make_webdriver()
    _driver.get(url=url)
    lan_dropdown = WebDriverWait(_driver, 5).until(EC.presence_of_element_located(By.CLASS_NAME, "el-select_el-dropdown"))
    # lan_dropdown = _driver.find_element(By.CLASS_NAME, "el-dropdown-link")
    lan_dropdown.click()

    _driver.quit()
