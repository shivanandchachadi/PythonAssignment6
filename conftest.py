import pytest
from selenium import webdriver


@pytest.fixture()
def init_driver(request):
    driver = webdriver.Chrome('C:\\ChromeDriver\\chromedriver_win32 (1)\\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    print("end of the test case")
    driver.quit()


@pytest.fixture(params=[("ind","shivanand")])
def data_provide(request):
    return request.param