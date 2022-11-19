import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en or es or fr")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")  # получаем параметр командной строки browser_name
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.set_preference('intl.accept_languages', user_language)
        print("\nstart fr browser for test..")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

