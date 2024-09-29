from behave import  given, when, then
from time import sleep

@given('Open Target App page')
def open_target_app(context):
    context.app.target_app_page.open_target_app()

@then('Store original window')
def store_window(context):
    #context.original_window = context.driver.current_window_handle
    context.original_window = context.app.target_app_page.get_current_window()

    print('Original window: ', context.original_window)


@then ('Click Privacy Policy Link')
def click_pp_link(context):
    context.app.target_app_page.click_pp_link()


@then ('Switch to new window')
def switch_to_new_window(context):
    context.app.target_app_page.switch_to_new_window()


@then('Verify Privacy Policy page opened')
def verify_pp_opened(context):
        context.app.target_app_page.verify_pp_opened()


@then('Close current page')
def close_page(context):
    context.app.target_app_page.close()

@then('Return to original window')
def switch_to_original(context):
        context.app.target_app_page.switch_to_window_by_id(context.original_window)
