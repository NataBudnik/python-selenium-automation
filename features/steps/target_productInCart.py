from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target page')
def open_page(context):
 context.driver.get('https://www.target.com/')
 sleep(3)


@when('Search a product {product}')
def searchProduct(context, product):
 search_box = context.driver.find_element(By.ID, 'search')
 search_box.send_keys(product)
 context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(4)

@when('Select the first product form the search results')
def select_first_product(context):
 context.driver.find_element(By.XPATH, "//div[@data-test='product-grid']//a").click()
sleep(4)



@when('Hover favorite icon')
def hover_favorites(context):
    context.app.search_results_page.hover_favorites()

@then('Favorites tooltip is shown')
def verify_favorites(context):
    context.app.search_results_page.hover_favorites()




@when('Add product to the cart')
def add_product_to_cart(context):
 #context.driver.find_element(By.XPATH, "//button[contains(text(), 'Add to cart')]").click()
 context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()
sleep(3)

@then('Verify that product is in the cart')
def verify_product_in_cart(context):

 context.driver.find_element(By.XPATH, "//a[@aria-label='cart']").click()



 cart_item = context.driver.find_element(By.XPATH, "//div[@data-test='cart-item-count']").text
 assert int(cart_item) > 0, f"Expected at least 1 item in the cart, but found {cart_item}"

 context.driver.quit()
