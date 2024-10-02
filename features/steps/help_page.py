from behave import given, when, then

@given ('Open help page for return')
def click_cart(context):
    context.app.help_page.open_help_returns()

@when ('Select Help topic Promotion & Coupons')
def select_topic(context):
    context.app.help_page.select_topic()

@then('Verify help Return page opened')
def verify_returns_opened(context):
    context.app.help_page.verify_returns_opened()

@then('Verify help Current promotion page opened')
def verify_promotions_opened(context):
    context.app.help_page.verify_promotions_opened()