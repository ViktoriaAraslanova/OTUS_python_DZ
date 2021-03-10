from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_find_elements_on_general_page(browser, base_url):
    browser.get(base_url)
    assert browser.find_elements(By.LINK_TEXT, "OpenCart")
    assert browser.find_elements(By.LINK_TEXT, "Your Store")
    assert browser.find_elements(By.CSS_SELECTOR, "#search input")
    assert browser.find_elements(By.CSS_SELECTOR, "#search button")
    assert browser.find_elements(By.CSS_SELECTOR, "#cart button")

    navbar_items = browser.find_elements(By.CSS_SELECTOR, ".navbar-nav > li")
    assert len(navbar_items) == 8, "Неверное количество элементов в панели навигации"

    assert browser.find_elements(By.CSS_SELECTOR, "#slideshow0")


def test_find_elements_on_catalog_page(browser, base_url):
    browser.get(f'{base_url}/index.php?route=product/category&path=20')

    group_items = browser.find_elements(By.CSS_SELECTOR, "#column-left .list-group-item")
    assert len(group_items) == 10, "Неверное количество категорий в списке слева"

    product_items = browser.find_elements(By.CSS_SELECTOR, ".product-layout")
    assert len(product_items) == 12, "Неверное количество товаров в каталоге"

    sort_items = browser.find_elements(By.CSS_SELECTOR, "#input-sort option")
    assert len(sort_items) == 9, "Неверное количество вариантов сортировки"

    limit_page_items = browser.find_elements(By.CSS_SELECTOR, "#input-limit option")
    assert len(limit_page_items) == 5, "Неверное количество лимитов на отображение элементов"

    buttons_products = browser.find_elements(By.CSS_SELECTOR, ".product-thumb button")
    assert len(buttons_products) == 36, "Неверное количество кнопок у продукта"


def test_find_elements_on_products_page(browser, base_url):
    browser.get(f'{base_url}/index.php?route=product/product&path=57&product_id=49')
    assert browser.find_element(By.LINK_TEXT, "Samsung Galaxy Tab 10.1")
    assert browser.find_element(By.XPATH, "//h1[text()='Samsung Galaxy Tab 10.1']")
    assert browser.find_element(By.CSS_SELECTOR, "#button-cart")

    image_items = browser.find_elements(By.CSS_SELECTOR, ".thumbnails .thumbnail")
    assert len(image_items) == 7, "Неверное количество картинок на странице"

    assert browser.find_elements(By.CSS_SELECTOR, "#form-review")


def test_find_elements_on_login_page(browser, base_url):
    browser.get(f'{base_url}/index.php?route=account/login')
    assert browser.find_element(By.LINK_TEXT, "Login")
    assert browser.find_element(By.XPATH, "//h2[text()='New Customer']")
    assert browser.find_element(By.XPATH, "//h2[text()='Returning Customer']")
    assert browser.find_element(By.LINK_TEXT, "Continue")
    assert browser.find_element(By.CSS_SELECTOR, "[value='Login']")
    assert browser.find_element(By.CSS_SELECTOR, "[name='email']")
    assert browser.find_element(By.CSS_SELECTOR, "[name='password']")
    assert browser.find_element(By.LINK_TEXT, "Forgotten Password")
    group_items = browser.find_elements(By.CSS_SELECTOR, ".list-group a")
    assert len(group_items) == 13, "Неверное количество категорий в списке справа"


def test_find_elements_on_login_admin_page(browser, base_url):
    browser.get(f'{base_url}/admin/')
    assert browser.find_element(By.CSS_SELECTOR, "[title='OpenCart']")
    assert browser.find_element(By.CSS_SELECTOR, "#input-username")
    assert browser.find_element(By.CSS_SELECTOR, "#input-password")
    assert browser.find_element(By.LINK_TEXT, "Forgotten Password")
    assert browser.find_elements(By.CSS_SELECTOR, "button[type='submit']")
    assert browser.find_element(By.XPATH, "//h1[text()=' Please enter your login details.']")


def test_go_to_products_in_admin_section(browser, base_url):
    browser.get(f'{base_url}/admin/')
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    browser.find_element(By.CSS_SELECTOR, "[href='#collapse1']").click()
    wait = WebDriverWait(browser, 5)
    el = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Products")))
    el.click()
    assert browser.find_element(By.CSS_SELECTOR, "#form-product")


def test_go_to_layouts_in_admin_section(browser, base_url):
    browser.get(f'{base_url}/admin/')
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    design_elements = browser.find_elements(By.CSS_SELECTOR, "#collapse20 a")
    assert len(design_elements) == 5

    browser.find_element(By.CSS_SELECTOR, "[href='#collapse20']").click()
    wait = WebDriverWait(browser, 5)
    el = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Layouts")))
    el.click()
    assert browser.find_element(By.CSS_SELECTOR, ".panel-heading")


def test_go_to_admin_profile(browser, base_url):
    browser.get(f'{base_url}/admin/')
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    browser.find_element(By.CSS_SELECTOR, ".dropdown-toggle").click()
    browser.find_element(By.LINK_TEXT, "Your Profile").click()
    assert browser.find_element(By.CSS_SELECTOR, ".panel-title")






