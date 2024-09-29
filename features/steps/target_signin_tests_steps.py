from behave import  given, when, then

@given ('Open Target "sign in" page')
def open_target_signin(context):
    context.app.sign_in_page.open_target_signin()


@when ('Store original window')
def store_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()
    print('Original window: ' ,context.original_window)

@when ('Click on Target terms and conditions link')
def click_term_link(context):
    context.app.sign_in_page.click_term_link()

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.sign_in_page.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_term_link_opened(context):
    context.app.sign_in_page.verify_term_link_opened()

@then('User can close new window and switch back to original')
def verify_close_window(context):
    context.app.sign_in_page.close()