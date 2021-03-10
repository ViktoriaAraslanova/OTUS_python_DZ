import pytest
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
import platform,os


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "edge"],
                     default="firefox", help="Browser")
    parser.addoption("--url", default="https://demo.opencart.com/", help="Request base url")


@pytest.fixture(scope='module')
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope='module')
def browser(request):
    maximized = request.config.getoption("--maximized")
    headless = request.config.getoption("--headless")
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:options.headless = True
        driver = webdriver.Chrome(options=options)
    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if platform.system() == "Windows":
            local_data = os.getenv('LOCALAPPDATA', None)
            options.binary_location = os.path.join(local_data, r"Mozilla Firefox\firefox.exe")
        if headless: options.headless = True
        driver = webdriver.Firefox(options=options)
    if browser == "edge":
        options = EdgeOptions()
        if headless:
            options.use_chromium = True;
            options.headless = True
        driver = Edge(executable_path=r"C:/projects/drivers/MicrosoftWebDriver.exe", options=options)
    if maximized:
        driver.maximize_window()

    def fin():
        driver.quit()
        print(f'Test {request.node.name} is over')

    request.addfinalizer(fin)
    return driver
