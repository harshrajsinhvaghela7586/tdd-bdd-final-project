from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "http://localhost:5000"

@given('I start on the "{page}"')
def step_start_page(context, page):
    context.browser.get(BASE_URL)

@when('I set "{field}" to "{value}"')
def step_set_field(context, field, value):
    input_element = context.browser.find_element(By.NAME, field)
    input_element.clear()
    input_element.send_keys(value)

@when('I press the "{button}" button')
def step_press_button(context, button):
    btn = context.browser.find_element(By.ID, button)
    btn.click()

@when('I copy the "{field}" field')
def step_copy_field(context, field):
    elem = context.browser.find_element(By.NAME, field)
    context.clipboard = elem.get_attribute('value')

@when('I paste the "{field}" field')
def step_paste_field(context, field):
    elem = context.browser.find_element(By.NAME, field)
    elem.clear()
    elem.send_keys(context.clipboard)

@then('I should see "{text}" in the "{field}" field')
def step_see_in_field(context, text, field):
    elem = context.browser.find_element(By.NAME, field)
    assert elem.get_attribute('value') == text, f'Expected {text}, got {elem.get_attribute("value")}'

@then('I should see the message "{message}"')
def step_see_message(context, message):
    alert_elem = context.browser.find_element(By.ID, "message")
    assert message in alert_elem.text

@then('I should see "{text}"')
def step_see_text(context, text):
    assert text in context.browser.page_source

@then('I should not see "{text}"')
def step_not_see_text(context, text):
    assert text not in context.browser.page_source

@when('I set "{field}" in dropdown to "{value}"')
def step_set_dropdown(context, field, value):
    select = Select(context.browser.find_element(By.NAME, field))
    select.select_by_visible_text(value)
