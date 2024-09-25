from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")



@given('Open target product {product_id} page')
def open_target(context, product_id):
    #context.driver.get(f'https://www.target.com/p/{product_id}')
    context.driver.get(f'https://www.target.com/p/journee-collection-womens-genevive-tru-comfort-foam-ankle-strap-flat-sandals/-/A-88457542?preselect=88457672#lnk=sametab{product_id}')
    sleep(3)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['black', 'brown', 'grey', 'mustard', 'orange']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(f"Found {len(colors)} color options.")


    for color in colors:
        print(color)
        color.click()                 #What's wrong with this line???????????

        sleep(3)

    selected_color = context.driver.find_element(*SELECTED_COLOR).text
    print('Current color text', selected_color)

    selected_color = selected_color.split('\n')[0].strip().lower()
    actual_colors.append(selected_color)


    print('actual_colors list: ', actual_colors)

    assert [color.lower() for color in expected_colors] == [color.lower() for color in actual_colors],f'Expected {expected_colors} did not match actual {actual_colors}'