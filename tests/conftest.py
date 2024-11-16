import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_argument(f"--lang={language}")  # Устанавливаем язык браузера

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en", help="Set the language for the test"
    )
